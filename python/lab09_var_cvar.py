"""Chapter 9 — VaR and CVaR: linear models and applications (scenario LP).

Contents:
  1. Example with 6 scenarios: VaR = 12, CVaR = 18.67,
     checked with the linear formulation of Rockafellar-Uryasev
  2. Minimum-CVaR portfolio: 3 assets (TEC, UTL, GLD), 10 equally likely annual scenarios,
     alpha = 0.8 (the tail is the 2 worst scenarios), expected return at least b = 3%
  3. Return-CVaR frontier as b varies, shadow price of the return constraint
     and effect of the level alpha
  4. Two-stage supplier choice (2 suppliers, 10 scenarios): the cost of resilience
"""
import gurobipy as gp
import numpy as np
import pandas as pd
from gurobipy import GRB

from stile import (ARANCIO, GRIGIO, ROSSO, TEAL, VERDE, intestazione, plt, salva_dat,
                   salva_dati, salva_figura)

# ----------------------------------------------------------------------
# 1. EXAMPLE WITH 6 SCENARIOS
# ----------------------------------------------------------------------
intestazione("Example with 6 scenarios: VaR and CVaR with the linear formulation")
perdite = np.array([2.0, 4.0, 5.0, 7.0, 12.0, 20.0])
pi6 = np.full(6, 1 / 6)
alpha = 0.80

# direct computation
cum = np.cumsum(pi6)
var_diretto = perdite[np.searchsorted(cum, alpha)]
print(f"Losses: {perdite.tolist()}, probability 1/6 each, alpha = {alpha}")
print(f"VaR (quantile): {var_diretto:.2f}")

# linear formulation of Rockafellar-Uryasev: min eta + 1/(1-alpha) sum pi_s xi_s
m = gp.Model("cvar6")
m.Params.OutputFlag = 0
eta = m.addVar(lb=-GRB.INFINITY, name="eta")
xi = m.addVars(6, name="xi")
m.addConstrs((xi[s] >= perdite[s] - eta for s in range(6)), name="tail")
m.setObjective(eta + gp.quicksum(pi6[s] * xi[s] for s in range(6)) / (1 - alpha),
               GRB.MINIMIZE)
m.optimize()
print(f"Rockafellar-Uryasev LP: eta* = {eta.X:.2f} (a VaR), CVaR = {m.ObjVal:.4f}")
print(f"By hand: 12 + (1/0.20)·(1/6)·(20-12) = 12 + 6.67 = 18.67  OK")
print(f"Expected value of the loss: {perdite.mean():.2f} "
      f"-> the CVaR tells the story of the tail, the mean does not.")


def var_cvar(perd, alpha):
    """VaR_alpha and exact CVaR_alpha of k equiprobable scenarios.

    VaR = alpha-quantile (the (ceil(alpha*k))-th loss in increasing order);
    CVaR = VaR + 1/((1-alpha) k) * sum_s max(l_s - VaR, 0), the value of the
    Rockafellar-Uryasev formula: with losses tied at the VaR it counts exactly (1-alpha) k scenarios.
    """
    ordered = np.sort(perd)
    k = len(ordered)
    var_ = ordered[int(np.ceil(alpha * k - 1e-9)) - 1]
    cvar_ = var_ + np.maximum(ordered - var_, 0).sum() / ((1 - alpha) * k)
    return var_, cvar_


# ----------------------------------------------------------------------
# 2. MINIMUM-CVaR PORTFOLIO
# ----------------------------------------------------------------------
intestazione("Minimum-CVaR portfolio (LP): 3 assets, 10 scenarios")
titoli = ["TEC", "UTL", "GLD"]
# annual return r_is (%) of asset i in scenario s, 10 equally likely scenarios:
# in scenario 1 the markets crash and gold rises; in scenarios 2 and 9 gold falls
R = np.array([[-25, -8, 15],
              [5, 2, -10],
              [30, 6, -5],
              [5, 4, 4],
              [0, 5, -3],
              [-5, -6, 8],
              [20, 8, 0],
              [10, 3, 2],
              [25, 7, -6],
              [5, 9, 5]], dtype=float)
k, n = R.shape
dati = pd.DataFrame(R, columns=titoli)
dati.insert(0, "scenario", range(1, k + 1))
salva_dati(dati, "cvar_scenari_rendimenti")
mu = R.mean(axis=0)                       # expected return m_i (%): 7, 3, 1
alpha_c = 0.80                            # the tail: (1 - 0.8) * 10 = 2 scenarios
b_obb = 3.0                               # minimum required expected return (%)

print(" s  " + "".join(f"{t:>6}" for t in titoli))
for s in range(k):
    print(f"{s + 1:2d}  " + "".join(f"{R[s, i]:6.0f}" for i in range(n)))
print("m_i " + "".join(f"{mu[i]:6.0f}" for i in range(n)) + "   (expected return, %)")


def porta_cvar(b, alpha=alpha_c):
    """min CVaR_alpha of the loss -R x  subject to  expected return >= b, weights summing to 1.

    Returns the weights, the CVaR (optimal value) and the shadow price of the return constraint,
    or None if no portfolio returns at least b."""
    m = gp.Model("min_cvar")
    m.Params.OutputFlag = 0
    x = m.addVars(n, name="x")
    eta = m.addVar(lb=-GRB.INFINITY, name="eta")
    xi = m.addVars(k, name="xi")
    m.addConstr(x.sum() == 1, name="budget")
    ret = m.addConstr(gp.quicksum(mu[i] * x[i] for i in range(n)) >= b, name="return")
    m.addConstrs((xi[s] >= -gp.quicksum(R[s, i] * x[i] for i in range(n)) - eta
                  for s in range(k)), name="tail")
    m.setObjective(eta + gp.quicksum(xi[s] for s in range(k)) / (k * (1 - alpha)),
                   GRB.MINIMIZE)
    m.optimize()
    if m.Status != GRB.OPTIMAL:
        return None
    return np.array([x[i].X for i in range(n)]), m.ObjVal, ret.Pi


x_ott, cvar_ott, ombra = porta_cvar(b_obb)
perd = -R @ x_ott
var_ott, _ = var_cvar(perd, alpha_c)
print(f"\nalpha = {alpha_c}, b = {b_obb:.0f}%: {n + 1 + k} variables, {k + 2} constraints")
print("Optimal weights: " + ", ".join(f"{titoli[i]} {x_ott[i]:.1%}" for i in range(n)))
print(f"{'s':>3} {'loss %':>10} {'xi_s':>6}")
for s in range(k):
    print(f"{s + 1:3d} {perd[s]:10.2f} {max(perd[s] - var_ott, 0):6.2f}")
print(f"mean loss {perd.mean():.2f}% (expected return {-perd.mean():.2f}%), "
      f"VaR80 {var_ott:.2f}%, CVaR80 {cvar_ott:.2f}%")
print(f"Shadow price of the return constraint: {ombra:.4f} "
      f"(one more point of return costs {ombra:.2f} points of CVaR)")
# the losses in increasing order; tail = 1 for the 2 worst scenarios (on a tie, the last in the order)
ordine = np.argsort(perd, kind="stable")
salva_dat(pd.DataFrame({"rank": range(1, k + 1), "scenario": ordine + 1, "loss": perd[ordine],
                        "tail": [0] * (k - 2) + [1, 1]}), "cap09_perdite")
salva_dat(pd.DataFrame({"stat": ["mean", "VaR", "CVaR"],
                        "value": [perd.mean(), var_ott, cvar_ott]}), "cap09_soglie")

# ----------------------------------------------------------------------
# 3. RETURN-CVaR FRONTIER AND EFFECT OF ALPHA
# ----------------------------------------------------------------------
intestazione("Return-CVaR frontier (alpha = 0.8)")
righe = []
for b in np.arange(0, mu.max() + 1e-9, 0.25):
    x, cv, pi = porta_cvar(b)
    righe.append((b, cv, *x, pi))
front = pd.DataFrame(righe, columns=["ret", "cvar", *titoli, "shadow"])
salva_dat(front, "cap09_frontiera")
print(f"{'b':>5} {'CVaR':>7} " + "".join(f"{t:>7}" for t in titoli) + f" {'shadow':>7}")
for r in front.itertuples(index=False):
    if r.ret in (0, 2.5, 3, 3.5, 4.25, 5, 6, 7):
        print(f"{r.ret:5.2f} {r.cvar:7.2f} " + "".join(f"{q:7.1%}" for q in r[2:2 + n]) + f" {r.shadow:7.2f}")
x0, cv0, _ = porta_cvar(0)
print(f"Minimum CVaR {cv0:.2f}% with expected return {mu @ x0:.2f}%: for b below this value "
      f"the return constraint is not active (shadow price 0)")
print(f"b = {mu.max() + 0.25:.2f}%: {'infeasible' if porta_cvar(mu.max() + 0.25) is None else 'feasible'} "
      f"(no asset returns more than {mu.max():.0f}%)")

intestazione("Effect of the level alpha (b = 3%)")
for a in [0.5, 0.6, 0.7, 0.8, 0.9]:
    x, cv, pi = porta_cvar(b_obb, a)
    print(f"alpha = {a:.1f} (tail of {(1 - a) * k:.0f} scenarios): CVaR {cv:6.2f}% | "
          + ", ".join(f"{titoli[i]} {x[i]:.1%}" for i in range(n)))

# ----------------------------------------------------------------------
# 4. TWO-STAGE SUPPLIER CHOICE
# ----------------------------------------------------------------------
intestazione("Two-stage suppliers: reserved capacity + recourse")
# Two suppliers (F1 cheap but fragile, F2 expensive but reliable) -> one market.
# 1st stage: reserved capacity x_a.  2nd stage, in each scenario: purchases f_as and unmet demand u_s.
forn = ["F1", "F2"]
c_pren = {"F1": 2.0, "F2": 3.0}         # reservation cost €/unit
c_uso = {"F1": 4.0, "F2": 4.0}          # purchase cost €/unit, the same for both suppliers
pen = 10.0                              # penalty per unit of unmet demand
dom_s = np.array([80, 90, 100, 100, 110, 110, 120, 120, 130, 140], dtype=float)
Ss = len(dom_s)
# availability of the fragile supplier: in scenarios 4 and 9 it delivers only half of the capacity
disp_f1 = np.array([1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1])
disp = {"F1": disp_f1, "F2": np.ones(Ss)}
alpha_f = 0.80                          # here too the tail is the 2 most expensive scenarios
print(f"{Ss} equally likely scenarios: demand {dom_s.astype(int).tolist()}, F1 at 50% in scenarios 4 and 9")
print(f"{2 + 3 * Ss} variables and {3 * Ss} constraints; with the CVaR {3 + 4 * Ss} and {4 * Ss}")


def duestadi(lam, alpha_c2=alpha_f):
    m = gp.Model("twostage")
    m.Params.OutputFlag = 0
    x = m.addVars(forn, name="x")
    f = m.addVars(forn, range(Ss), name="f")
    u = m.addVars(range(Ss), name="u")
    for s in range(Ss):
        for a in forn:
            m.addConstr(f[a, s] <= disp[a][s] * x[a])
        m.addConstr(gp.quicksum(f[a, s] for a in forn) + u[s] >= dom_s[s])
    costo1 = gp.quicksum(c_pren[a] * x[a] for a in forn)
    costo2 = {s: gp.quicksum(c_uso[a] * f[a, s] for a in forn) + pen * u[s]
              for s in range(Ss)}
    atteso = costo1 + gp.quicksum(costo2[s] for s in range(Ss)) / Ss
    if lam > 0:
        eta = m.addVar(lb=-GRB.INFINITY)
        xi = m.addVars(range(Ss))
        m.addConstrs((xi[s] >= costo1 + costo2[s] - eta for s in range(Ss)))
        cvar = eta + gp.quicksum(xi[s] for s in range(Ss)) / (Ss * (1 - alpha_c2))
        m.setObjective((1 - lam) * atteso + lam * cvar, GRB.MINIMIZE)
    else:
        m.setObjective(atteso, GRB.MINIMIZE)
    m.optimize()
    assert m.Status == GRB.OPTIMAL, m.Status
    tot = np.array([c_pren["F1"] * x["F1"].X + c_pren["F2"] * x["F2"].X
                    + sum(c_uso[a] * f[a, s].X for a in forn) + pen * u[s].X
                    for s in range(Ss)])
    serv = np.array([1 - u[s].X / dom_s[s] for s in range(Ss)])
    return {a: x[a].X for a in forn}, tot, serv


# with r = 1 only the tail would count: the purchases in the other scenarios would not be determined
righe = []
for lam in [0.0, 0.5, 0.75]:
    cap, tot, serv = duestadi(lam)
    _, cvar_t = var_cvar(tot, alpha_f)
    righe.append((lam, cap["F1"], cap["F2"], tot.mean(), cvar_t, serv.mean()))
    print(f"  r = {lam:4.2f}: reserve F1 = {cap['F1']:5.1f}, F2 = {cap['F2']:5.1f} | "
          f"mean cost {tot.mean():6.1f}, CVaR80 {cvar_t:6.1f} | mean service {serv.mean():.1%}")
    print("          cost per scenario: " + " ".join(f"{c:.0f}" for c in tot))
res2 = pd.DataFrame(righe, columns=["lam", "F1", "F2", "mean_cost", "cvar", "service"])
salva_dat(res2, "cap09_duestadi")
print("The risk-averse decision maker reserves more capacity from the reliable supplier:")
print("it pays more on average, but it cuts the tail of the scenarios with unmet demand.")

# ----------------------------------------------------------------------
# 5. FIGURES
# ----------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 4.0))
ax1.bar(range(1, k + 1), perd[ordine], color=[TEAL] * (k - 2) + [ROSSO] * 2, alpha=0.8)
ax1.set_xticks(range(1, k + 1), [str(s + 1) for s in ordine])
ax1.axhline(0, color=GRIGIO, lw=0.8)
ax1.axhline(perd.mean(), color=VERDE, ls="--", label=f"mean {perd.mean():.2f}%")
ax1.axhline(var_ott, color=ARANCIO, ls="-.", label=f"VaR$_{{0.8}}$ {var_ott:.2f}%")
ax1.axhline(cvar_ott, color=ROSSO, ls="-", label=f"CVaR$_{{0.8}}$ {cvar_ott:.2f}%")
ax1.set_xlabel("scenario, in increasing order of loss (in red the 2 of the tail)")
ax1.set_ylabel("annual loss of the portfolio (%)")
ax1.set_title(f"Losses of the optimal portfolio (b = {b_obb:.0f}%)")
ax1.legend(fontsize=8, loc="upper left")
ax2.plot(front["cvar"], front["ret"], "-o", color=TEAL, ms=4)
ax2.plot([cvar_ott], [b_obb], "o", ms=10, mfc="none", mec=ROSSO, mew=2,
         label=f"b = {b_obb:.0f}%: CVaR {cvar_ott:.2f}%")
ax2.set_xlabel("CVaR$_{0.8}$ of the annual loss (%)")
ax2.set_ylabel("required expected return b (%)")
ax2.set_title("Return-CVaR frontier")
ax2.legend(fontsize=8, loc="lower right")
salva_figura(fig, "cap09_perdite_frontiera")

print("\nDone: chapter 9.")
