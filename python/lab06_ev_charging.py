"""Chapter 6 — Smart charging of electric vehicles (LP).

Case study: a company depot with 3 electric vans to be charged in the 6 hours
from midnight to 6 am; hourly energy prices; base load of the building.

Contents:
  1. Minimum-cost LP: charging chases the cheap hours
  2. Peak shaving: minimise the peak withdrawal (minimax)
  3. Multi-objective cost-peak comparison
  4. Shadow prices: grid capacity and energy requirement
"""
import gurobipy as gp
import pandas as pd
from gurobipy import GRB

from stile import (ARANCIO, GRIGIO, ROSSO, TEAL, intestazione, plt, salva_dat, salva_dati,
                   salva_figura)

# ----------------------------------------------------------------------
# 1. DATA
# ----------------------------------------------------------------------
ore = list(range(1, 7))                    # hour t = from t-1 to t (t = 1: from 0:00 to 1:00)
# price €/kWh: high in the first hours (tail of the evening peak), lowest from 3 to 4 am
prezzo = pd.Series([0.20, 0.15, 0.11, 0.07, 0.09, 0.13], index=ore)
# base load of the building (kW)
base = pd.Series([14.0, 12.0, 10.0, 8.0, 8.0, 10.0], index=ore)

veicoli = ["V1", "V2", "V3"]
# (arrival hour, departure hour, required energy kWh, max power kW)
flotta = {
    "V1": (0, 6, 36, 11),     # plugged in all night
    "V2": (0, 3, 18, 11),     # leaves at 3 am for the first shift
    "V3": (3, 6, 18, 16),     # back at 3 am from the last shift
}
eta = 0.9             # charging efficiency
C_rete = 30.0         # maximum power that can be drawn from the meter (kW)

# plugged in during hour t (from t-1 to t) if it arrived by t-1 and leaves at t or later
disp = {(v, t): 1 if flotta[v][0] < t <= flotta[v][1] else 0
        for v in veicoli for t in ore}

salva_dati(pd.DataFrame({"hour": ore, "price": prezzo, "base_load": base}), "ev_prezzi_base")
salva_dati(pd.DataFrame([(v, *flotta[v]) for v in veicoli],
                        columns=["vehicle", "arrival", "departure", "energy_kWh", "pmax_kW"]),
           "ev_flotta")


def costruisci():
    m = gp.Model("ev_charging")
    m.Params.OutputFlag = 0
    x = m.addVars(veicoli, ore, name="x")       # charging power (kW)
    for v in veicoli:
        for t in ore:
            x[v, t].UB = flotta[v][3] * disp[v, t]     # 0 if not plugged in
    v_ene = m.addConstrs((eta * gp.quicksum(x[v, t] for t in ore) >= flotta[v][2]
                          for v in veicoli), name="energy")
    v_rete = m.addConstrs((gp.quicksum(x[v, t] for v in veicoli) + base[t] <= C_rete
                           for t in ore), name="grid")
    return m, x, v_ene, v_rete


def profilo(x):
    return pd.Series([sum(x[v, t].X for v in veicoli) for t in ore], index=ore)


# ----------------------------------------------------------------------
# 2. MINIMUM-COST LP
# ----------------------------------------------------------------------
intestazione("LP: minimum energy cost")
m, x, v_ene, v_rete = costruisci()
m.setObjective(gp.quicksum(prezzo[t] * x[v, t] for v in veicoli for t in ore), GRB.MINIMIZE)
m.optimize()
assert m.Status == GRB.OPTIMAL
prof_costo = profilo(x)
costo_min = m.ObjVal
picco_costo = (prof_costo + base).max()
print(f"Charging cost: {costo_min:.2f} €   peak withdrawal: {picco_costo:.1f} kW "
      f"(limit {C_rete:.0f})")
print("\nPower x[v, t] (kW), hours t = 1..6:")
for v in veicoli:
    print(f"  {v}: " + "  ".join(f"{x[v, t].X:5.1f}" if disp[v, t] else "    ." for t in ore))
print("\nShadow prices of the energy requirement (marginal cost of 1 more kWh per vehicle):")
for v in veicoli:
    print(f"  {v}: {v_ene[v].Pi:.4f} €/kWh")
print("Shadow prices of the grid (saving for 1 more kW in hour t):")
print("  " + "  ".join(f"t={t}: {abs(v_rete[t].Pi):.3f}" for t in ore))

# ----------------------------------------------------------------------
# 3. PEAK SHAVING (minimax) and COST-PEAK TRADE-OFF
# ----------------------------------------------------------------------
intestazione("Peak shaving: minimise the peak withdrawal")
mp, xp, _, _ = costruisci()
z = mp.addVar(name="peak")
mp.addConstrs((gp.quicksum(xp[v, t] for v in veicoli) + base[t] <= z for t in ore),
              name="peak_def")
mp.setObjective(z, GRB.MINIMIZE)
mp.optimize()
prof_picco = profilo(xp)
costo_picco = sum(prezzo[t] * prof_picco[t] for t in ore)
print(f"Lowest achievable peak: {mp.ObjVal:.1f} kW   cost: {costo_picco:.2f} € "
      f"(+{costo_picco - costo_min:.2f} € with respect to the minimum cost)")

intestazione("Trade-off: cost + w · peak")
compromessi = []
for rho in [0, 0.05, 0.1, 0.15, 0.2, 0.5, 1.0]:
    mc, xc, _, _ = costruisci()
    zc = mc.addVar(name="peak")
    mc.addConstrs((gp.quicksum(xc[v, t] for v in veicoli) + base[t] <= zc for t in ore))
    mc.setObjective(gp.quicksum(prezzo[t] * xc[v, t] for v in veicoli for t in ore)
                    + rho * zc, GRB.MINIMIZE)
    mc.optimize()
    cc = sum(prezzo[t] * xc[v, t].X for v in veicoli for t in ore)
    compromessi.append((rho, cc, zc.X))
    print(f"  w = {rho:4.2f}: cost {cc:6.2f} €, peak {zc.X:6.1f} kW")
salva_dati(pd.DataFrame(compromessi, columns=["rho", "cost", "peak"]), "ev_compromessi")

# ----------------------------------------------------------------------
# 4. SENSITIVITY: capacity of the meter
# ----------------------------------------------------------------------
intestazione("Sensitivity: capacity of the grid connection")
# careful: in the constraint "sum x + base[t] <= C" Gurobi moves the constant base[t]
# into the right-hand side; the stored RHS is C - base[t], so it must be updated like this:
for CC in [23, 24, 26, 28, 30, 32, 35]:
    ms, xs_, _, vr = costruisci()
    for t in ore:
        vr[t].RHS = CC - base[t]
    ms.setObjective(gp.quicksum(prezzo[t] * xs_[v, t] for v in veicoli for t in ore),
                    GRB.MINIMIZE)
    ms.optimize()
    esito = f"cost {ms.ObjVal:6.2f} €" if ms.Status == GRB.OPTIMAL else "INFEASIBLE"
    print(f"  C_grid = {CC:3d} kW: {esito}")

# ----------------------------------------------------------------------
# 5. FIGURES (pgfplots data + matplotlib preview)
# ----------------------------------------------------------------------
salva_dat(pd.DataFrame({"hour": ore, "price_cent": prezzo * 100, "base": base,
                        "totcost": base + prof_costo, "totpeak": base + prof_picco}),
          "cap06_profili")
salva_dat(pd.DataFrame(compromessi, columns=["rho", "cost", "peak"]), "cap06_frontiera")
# one-hour-wide steps for pgfplots (const plot): edges 0.5, 1.5, ..., 6.5, the last value repeated
bordi = [t - 0.5 for t in ore] + [ore[-1] + 0.5]


def gradino(serie):
    return list(serie) + [serie.iloc[-1]]


salva_dat(pd.DataFrame({"x": bordi, "base": gradino(base), "totcost": gradino(base + prof_costo),
                        "totpeak": gradino(base + prof_picco)}), "cap06_gradini")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.2, 6.4), sharex=True)
ax1.bar(ore, prezzo * 100, color=GRIGIO, alpha=0.6)
ax1.set_ylabel("price $c_t$ (c€/kWh)")
ax1.set_title("Hourly energy price")
# same entries, colours and title as the lab app; legend above the meter limit
# one column per hour: steps one hour wide, from t-1 to t (edges as above)
ax2.stairs(base, bordi, baseline=None, color=GRIGIO, ls="--", label="base load $b_t$")
ax2.stairs(base + prof_costo, bordi, baseline=None, color=TEAL, lw=2, label="minimum cost")
ax2.stairs(base + prof_picco, bordi, baseline=None, color=ARANCIO, lw=2, label="peak shaving")
ax2.axhline(C_rete, color=ROSSO, ls=":", label=f"meter power $k$ = {C_rete:.0f} kW")
ax2.set_ylim(0, C_rete * 1.45)
ax2.set_xticks(ore); ax2.set_xlabel("hour $t$ (from $t-1$ to $t$)"); ax2.set_ylabel("total withdrawal (kW)")
ax2.set_title("Power withdrawn from the grid")
ax2.legend(fontsize=8, ncol=2, loc="upper right")
salva_figura(fig, "cap06_profili")

comp = pd.DataFrame(compromessi, columns=["rho", "cost", "peak"])
fig, ax = plt.subplots()
ax.plot(comp["peak"], comp["cost"], "-o", color=TEAL)
# weights with the same point (same peak and cost) in a single label
groups = comp.groupby([comp["peak"].round(3), comp["cost"].round(4)], sort=False)
for k, ((pk, cc), g) in enumerate(groups):
    weights = ", ".join(f"{w:.2f}" for w in g["rho"])
    ax.annotate(f"$w$ = {weights}", (pk, cc), textcoords="offset points", xytext=(8, -3 if k == 0 else 4),
                fontsize=8)
ax.set_xlim(comp["peak"].min() - 3, comp["peak"].max() + 6)
ax.set_xlabel("peak withdrawal (kW)")
ax.set_ylabel("charging cost (€)")
ax.set_title("Cost-peak frontier: cutting the peak is cheap at first")
salva_figura(fig, "cap06_frontiera")

print("\nDone: chapter 6.")
