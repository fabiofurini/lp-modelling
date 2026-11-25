"""Chapter 8 — The Newsvendor and its variants (scenario-based stochastic LP).

Case study: a bakery deciding how many artisan panettoni to produce.
Price p = 15 €, cost c = 6 €, salvage v = 2 € -> Cu = 9, Co = 4.
Demand: 10 equally likely scenarios, nine regular ones from 50 to 130 and an exceptional one of 190.

Contents:
  1. Quantile rule on the scenarios: f* = 9/13 = 0.6923 -> q* = 110 (7th scenario)
  2. Scenario LP: it coincides with the empirical quantile
  3. Value of the stochastic solution (VSS); stability of the empirical quantile
     (a separate illustration, with larger samples from a normal distribution)
  4. Service levels (cycle service level, fill rate)
  5. Risk aversion: mean cost - CVaR_0.8 frontier (the 2 worst scenarios)
  6. Multi-product with a shared budget
"""
import gurobipy as gp
import numpy as np
import pandas as pd
from gurobipy import GRB
from scipy import stats

from stile import (ARANCIO, GRIGIO, ROSSO, TEAL, intestazione, plt, salva_dat,
                   salva_dati, salva_figura)

p, c, v = 15.0, 6.0, 2.0
Cu, Co = p - c, c - v                 # 9 and 4

# ----------------------------------------------------------------------
# 1. DATA AND QUANTILE RULE ON THE SCENARIOS
# ----------------------------------------------------------------------
intestazione("Quantile rule on the 10 scenarios")
# nine regular seasons (from 50 to 130) and an exceptional one (190): the right tail
dom = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 190], dtype=float)
S = len(dom)                          # equally likely scenarios, w_s = 1/S
salva_dati(pd.DataFrame({"scenario": range(1, S + 1), "demand": dom}), "newsvendor_scenari")


def costo_atteso(q, d=dom):
    """Expected cost over the equally likely scenarios: mean of Co(q-d)^+ + Cu(d-q)^+."""
    return float(np.mean(Co * np.maximum(q - d, 0) + Cu * np.maximum(d - q, 0)))


def quantile_empirico(d, f):
    """The smallest value d_s with F(d_s) >= f (discrete quantile rule)."""
    ordinati = np.sort(d)
    return ordinati[int(np.ceil(f * len(d) - 1e-9)) - 1]


f_star = Cu / (Cu + Co)
q_star = quantile_empirico(dom, f_star)
print(f"Critical fractile f* = Cu/(Cu+Co) = {Cu:.0f}/{Cu + Co:.0f} = {f_star:.4f}")
print(f"{'d_s':>5} {'F(d_s)':>7} {'C(d_s)':>8}")
for k, d in enumerate(np.sort(dom), start=1):
    print(f"{d:5.0f} {k / S:7.1f} {costo_atteso(d):8.1f}" + ("   <- q*" if d == q_star else ""))
print(f"q* = the smallest d_s with F(d_s) >= {f_star:.4f}: {q_star:.0f} units "
      f"(mean = {dom.mean():.0f}, cost at q = mean: {costo_atteso(dom.mean()):.1f} €)")

# the expected cost is piecewise linear with its vertices at the scenarios: the vertices suffice
qq = np.concatenate([[40.0], np.sort(dom), [200.0]])
salva_dat(pd.DataFrame({"q": qq, "cost": [costo_atteso(q) for q in qq]}), "cap08_costo")

# ----------------------------------------------------------------------
# 2. SCENARIO LP
# ----------------------------------------------------------------------
intestazione(f"Scenario LP (k = {S}: {1 + 2 * S} variables, {2 * S} constraints)")


def newsvendor_lp(dom_s, prob=None, lam=0.0, alpha_cvar=0.80):
    """LP: min (1-lam)·expected cost + lam·CVaR_alpha(cost). lam=0 -> risk neutral."""
    Sn = len(dom_s)
    pi = np.full(Sn, 1 / Sn) if prob is None else prob
    m = gp.Model("newsvendor")
    m.Params.OutputFlag = 0
    q = m.addVar(name="q")
    o = m.addVars(Sn, name="o")                 # overage
    u = m.addVars(Sn, name="u")                 # underage
    m.addConstrs((o[s] >= q - dom_s[s] for s in range(Sn)), name="over")
    m.addConstrs((u[s] >= dom_s[s] - q for s in range(Sn)), name="under")
    costo_s = {s: Co * o[s] + Cu * u[s] for s in range(Sn)}
    atteso = gp.quicksum(pi[s] * costo_s[s] for s in range(Sn))
    if lam > 0:
        eta = m.addVar(lb=-GRB.INFINITY, name="eta")
        xi = m.addVars(Sn, name="xi")
        m.addConstrs((xi[s] >= costo_s[s] - eta for s in range(Sn)), name="cvar")
        cvar = eta + gp.quicksum(pi[s] * xi[s] for s in range(Sn)) / (1 - alpha_cvar)
        m.setObjective((1 - lam) * atteso + lam * cvar, GRB.MINIMIZE)
    else:
        m.setObjective(atteso, GRB.MINIMIZE)
    m.optimize()
    assert m.Status == GRB.OPTIMAL
    costi = np.array([Co * max(q.X - d, 0) + Cu * max(d - q.X, 0) for d in dom_s])
    return q.X, float(costi @ pi), costi


q_lp, costo_lp, costi_s = newsvendor_lp(dom)
print(f"optimal q of the LP: {q_lp:.2f}  |  empirical quantile at {f_star:.2%}: {q_star:.2f}")
print(f"Expected cost: {costo_lp:.2f} €")
print(f"{'s':>3} {'d_s':>5} {'o_s':>5} {'u_s':>5} {'cost':>6}")
for s in range(S):
    print(f"{s + 1:3d} {dom[s]:5.0f} {max(q_lp - dom[s], 0):5.0f} {max(dom[s] - q_lp, 0):5.0f} {costi_s[s]:6.0f}")

# ----------------------------------------------------------------------
# 3. VSS AND STABILITY
# ----------------------------------------------------------------------
intestazione("Value of the stochastic solution (VSS)")
costo_det = costo_atteso(dom.mean())
print(f"'Naive' decision q = E[D] = {dom.mean():.0f}: expected cost {costo_det:.2f} €")
print(f"Stochastic decision q = {q_lp:.0f}     : expected cost {costo_lp:.2f} €")
print(f"VSS = {costo_det - costo_lp:.2f} € per selling cycle "
      f"({(costo_det - costo_lp) / costo_lp:.1%} of the cost)")

# A separate illustration, with its own sample, larger than the 10 scenarios: if the scenarios
# are drawn from a normal demand with mean 100 and standard deviation 20, how much does the
# empirical quantile (that is, the q of the LP) change from one sample to another?
intestazione("Stability: empirical quantile of k scenarios drawn from a normal (100, 20)")
rng = np.random.default_rng(42)
mu_d, sigma_d = 100.0, 20.0
q_teorico = stats.norm.ppf(f_star, mu_d, sigma_d)
print(f"theoretical quantile of the normal: F^-1({f_star:.4f}) = {q_teorico:.2f}")
righe = []
for Sn in [10, 30, 100, 300, 1000, 3000]:
    stime = [quantile_empirico(np.maximum(rng.normal(mu_d, sigma_d, Sn), 0), f_star)
             for rep in range(30)]
    righe.append((Sn, np.mean(stime), np.std(stime)))
    print(f"  k = {Sn:5d}: mean q {np.mean(stime):7.2f}, std. dev. over 30 replications {np.std(stime):5.2f}")
stab = pd.DataFrame(righe, columns=["S", "q_mean", "q_std"])
salva_dat(stab, "cap08_stabilita")

# ----------------------------------------------------------------------
# 4. SERVICE LEVELS
# ----------------------------------------------------------------------
intestazione("Service levels")


def carenza_attesa(q, d=dom):
    return float(np.mean(np.maximum(d - q, 0)))


print(f"{'q':>5} {'P(D<=q)':>8} {'fill rate':>10} {'cost':>7}")
for q in [100, 110, 120, 130, 140, 190]:
    print(f"{q:5.0f} {np.mean(dom <= q):8.0%} {1 - carenza_attesa(q) / dom.mean():10.0%} "
          f"{costo_atteso(q):7.1f}")
for beta in [0.90, 0.95]:
    q_sl = quantile_empirico(dom, beta)
    print(f"  cycle service level {beta:.0%}: q = {q_sl:5.0f} "
          f"(cost +{costo_atteso(q_sl) - costo_lp:6.2f} € over the economic optimum)")
# fill rate 95%: the expected shortage, piecewise linear and decreasing in q, must drop to 0.05·E[D]
vertici = np.sort(dom)
car = np.array([carenza_attesa(q) for q in vertici])
q_fr = float(np.interp(0.05 * dom.mean(), car[::-1], vertici[::-1]))
print(f"  fill rate 95%           : q = {q_fr:5.0f} (cost +{costo_atteso(q_fr) - costo_lp:6.2f} €)")
print(f"  at q* = {q_star:.0f}: fill rate {1 - carenza_attesa(q_star) / dom.mean():.0%}, "
      f"probability of no stock-out {np.mean(dom <= q_star):.0%}")

# ----------------------------------------------------------------------
# 5. RISK AVERSION: cost-CVaR frontier
# ----------------------------------------------------------------------
alpha_cv = 0.80               # with 10 scenarios the tail 1 - alpha = 0.2 is the 2 most expensive scenarios
intestazione(f"Mean cost - CVaR frontier (alpha = {alpha_cv:.2f}: the {round((1 - alpha_cv) * S)} "
             f"worst scenarios out of {S})")


def var_cvar(costi, alpha):
    """VaR_alpha and exact CVaR_alpha of k equally likely scenarios.

    VaR = alpha quantile (the (ceil(alpha*k))-th cost in increasing order);
    CVaR = VaR + 1/((1-alpha) k) * sum_s max(c_s - VaR, 0), the value of the
    Rockafellar-Uryasev formula: the exact mean of the (1-alpha) k most expensive scenarios.
    """
    ordinati = np.sort(costi)
    k = len(ordinati)
    var_ = ordinati[int(np.ceil(alpha * k - 1e-9)) - 1]
    return var_, var_ + np.maximum(ordinati - var_, 0).sum() / ((1 - alpha) * k)


front = []
for lam in [0, 0.25, 0.5, 0.75, 1.0]:
    q_l, cm, costi_l = newsvendor_lp(dom, lam=lam, alpha_cvar=alpha_cv)
    _, cvar_l = var_cvar(costi_l, alpha_cv)
    front.append((lam, q_l, cm, cvar_l))
    print(f"  r = {lam:4.2f}: q = {q_l:6.1f}, mean cost = {cm:6.2f}, "
          f"CVaR80 = {cvar_l:6.2f}")
front = pd.DataFrame(front, columns=["lam", "q", "mean_cost", "cvar"])
salva_dat(front, "cap08_frontiera_cvar")

# the jumps of q*: the optimum is a vertex of the frontier and moves to the next one when
# (1-r)·mean cost + r·CVaR becomes equal at the two vertices
vertici_f = front.drop_duplicates("q").reset_index(drop=True)
print("Thresholds of r where q* changes:")
for a, b in zip(vertici_f.itertuples(), vertici_f.iloc[1:].itertuples()):
    dE, dC = b.mean_cost - a.mean_cost, a.cvar - b.cvar
    print(f"  from q = {a.q:.0f} to q = {b.q:.0f} for r > {dE:.0f}/({dE:.0f} + {dC:.0f}) = {dE / (dE + dC):.3f}")
print("Increasing r means ordering more: it costs on average, it protects in the worst scenarios.")

# ----------------------------------------------------------------------
# 6. MULTI-PRODUCT WITH A SHARED BUDGET
# ----------------------------------------------------------------------
intestazione("Multi-product: 3 cakes on the same 10 scenarios, production budget 1250 €")
nomi_p = ["panettone", "pandoro", "torrone"]
# demands in the same scenarios: good and bad seasons are good and bad for all three cakes
dom_m = np.array([dom,
                  [40, 40, 50, 60, 70, 80, 90, 90, 100, 150],
                  [30, 40, 40, 50, 50, 60, 70, 70, 80, 110]], dtype=float)
costi_c = np.array([6.0, 5.0, 4.0])
Cu_m = np.array([9.0, 7.0, 5.0])
Co_m = np.array([4.0, 3.5, 2.5])
budget = 1250.0
P3 = range(3)

mm = gp.Model("newsvendor_multi")
mm.Params.OutputFlag = 0
qm = mm.addVars(3, name="q")
om = mm.addVars(3, S, name="o")
um = mm.addVars(3, S, name="u")
mm.addConstrs((om[i, s] >= qm[i] - dom_m[i, s] for i in P3 for s in range(S)))
mm.addConstrs((um[i, s] >= dom_m[i, s] - qm[i] for i in P3 for s in range(S)))
v_bud = mm.addConstr(gp.quicksum(costi_c[i] * qm[i] for i in P3) <= budget, name="budget")
mm.setObjective(gp.quicksum((Co_m[i] * om[i, s] + Cu_m[i] * um[i, s]) / S
                            for i in P3 for s in range(S)), GRB.MINIMIZE)
mm.optimize()
assert mm.Status == GRB.OPTIMAL
print(f"{'product':>10} | {'q no budget':>14} | {'q w/ budget':>12}")
q_solo = [quantile_empirico(dom_m[i], Cu_m[i] / (Cu_m[i] + Co_m[i])) for i in P3]
for i in P3:
    print(f"{nomi_p[i]:>10} | {q_solo[i]:14.1f} | {qm[i].X:12.2f}")
spesa = sum(costi_c[i] * qm[i].X for i in P3)
print(f"Spend without budget: {costi_c @ np.array(q_solo):.0f} €  |  with the budget: {spesa:.2f} / {budget:.0f} €")
print(f"Expected cost: {mm.ObjVal:.2f} €  |  shadow price of the budget: {v_bud.Pi:.4f} "
      f"(reduction of the expected cost per 1 € of extra budget)")

# ----------------------------------------------------------------------
# 7. FIGURES
# ----------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax1.plot(qq, [costo_atteso(q) for q in qq], color=TEAL, lw=2, marker="o", ms=3.5,
         label="expected cost $C(q)$")
ax1.axvline(dom.mean(), color=GRIGIO, ls="--", label=f"mean = {dom.mean():.0f}")
ax1.axvline(q_star, color=ROSSO, ls="-.", label=f"$q^*$ = {q_star:.0f} (7th scenario)")
ax1.set_xlabel("ordered quantity $q$"); ax1.set_ylabel("expected cost (€)")
ax1.set_title("On the 10 scenarios the minimum is at 110, not at the mean")
ax1.legend(fontsize=8, loc="upper right")
ax2.errorbar(stab["S"], stab["q_mean"], yerr=stab["q_std"], fmt="-o", color=TEAL,
             capsize=3, label="mean ± std. dev. over 30 replications")
ax2.axhline(q_teorico, color=ROSSO, ls="-.", label=f"quantile of the normal = {q_teorico:.2f}")
ax2.set_xscale("log")
ax2.set_xlabel("number of scenarios $k$ drawn from the normal (100, 20)"); ax2.set_ylabel("optimal $q$")
ax2.set_title("Stability of the empirical quantile (separate sample)")
ax2.legend(fontsize=8)
salva_figura(fig, "cap08_quantile_stabilita")

fig, ax = plt.subplots()
# as in the lab app: same curve, same labels, legend in the empty top-right corner
weights = ", ".join(f"{w:g}" for w in front["lam"])
ax.plot(front["cvar"], front["mean_cost"], "-o", color=TEAL, label=f"frontier ($r$ = {weights})")
# the weights with the same order (same point) in a single label
# (the labels of the middle points above the polyline, the others to the right of the point)
gruppi = list(front.groupby("q", sort=False))
for k, (qv, g) in enumerate(gruppi):
    pesi_g = ", ".join(f"{w:.2f}" for w in g["lam"])
    ax.annotate(f"$r$ = {pesi_g}: $q$ = {qv:.0f}", (g["cvar"].iloc[0], g["mean_cost"].iloc[0]),
                textcoords="offset points", xytext=(8, -3 if k in (0, len(gruppi) - 1) else 6), fontsize=8)
dx = front["cvar"].max() - front["cvar"].min()
ax.set_xlim(front["cvar"].min() - 0.06 * dx, front["cvar"].max() + 0.32 * dx)
ax.set_xlabel("CVaR$_{0.8}$ of the cost (€)"); ax.set_ylabel("mean cost (€)")
ax.set_title("Mean cost – tail risk frontier")
ax.legend(fontsize=8, loc="upper right")
salva_figura(fig, "cap08_frontiera")

print("\nDone: chapter 8.")
