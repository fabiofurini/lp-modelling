"""Chapter 5 — Multi-period production and inventory planning (LP).

Case study: a company producing 3 components (products 1, 2, 3) over a 3-month
horizon with one shared resource (machine hours).

Contents:
  1. Minimum-cost LP with mandatory service
  2. Shadow prices of capacity and analysis of the duals
  3. Sensitivity: optimal cost as capacity varies
"""
import gurobipy as gp
import numpy as np
import pandas as pd
from gurobipy import GRB

from stile import (ARANCIO, GRIGIO, ROSSO, TEAL, VERDE, intestazione, plt, salva_dat, salva_dati,
                   salva_figura)

# ----------------------------------------------------------------------
# 1. DATA
# ----------------------------------------------------------------------
prodotti = ["1", "2", "3"]
mesi = list(range(1, 4))

# demand (units/month): increasing, peaking in month 3
domanda = {
    ("1", 1): 110, ("1", 2): 140, ("1", 3): 200,
    ("2", 1): 60,  ("2", 2): 80,  ("2", 3): 120,
    ("3", 1): 40,  ("3", 2): 40,  ("3", 3): 70,
}
costo_prod = {"1": 10.0, "2": 15.0, "3": 20.0}   # €/unit
costo_giac = {"1": 1.0, "2": 1.2, "3": 1.2}      # €/unit/month
ore_unit = {"1": 1.0, "2": 1.5, "3": 2.0}        # machine hours per unit
capacita = {1: 400, 2: 400, 3: 400}  # hours/month
scorta_iniziale = {"1": 0, "2": 0, "3": 0}      # r_i0: stock at the start of the horizon (units)
scorta_finale = {"1": 0, "2": 0, "3": 0}        # r_im: stock required at the end of the horizon (units)
ultimo = mesi[-1]                               # month m
mesi_s = mesi[:-1]                              # months 1..m-1: only here the stock s_it is a variable

df = pd.DataFrame(
    [(i, t, domanda[i, t], costo_prod[i], costo_giac[i], ore_unit[i], scorta_iniziale[i], scorta_finale[i])
     for i in prodotti for t in mesi],
    columns=["product", "month", "demand", "production_cost", "holding_cost", "hours_unit",
             "initial_stock", "final_stock"])
salva_dati(df, "produzione_domanda")
salva_dati(pd.DataFrame({"month": mesi, "capacity_hours": [capacita[t] for t in mesi]}),
           "produzione_capacita")


def costruisci_lp():
    """Basic LP: minimum production + holding cost, mandatory service."""
    m = gp.Model("production_inventory")
    m.Params.OutputFlag = 0
    x = m.addVars(prodotti, mesi, name="x")           # quantity produced
    s = m.addVars(prodotti, mesi_s, name="s")         # stock at the end of the month, months 1..m-1
    # inventory balance (variables on the left, data on the right): first month, middle months, last month
    m.addConstrs((x[i, 1] - s[i, 1] == domanda[i, 1] - scorta_iniziale[i]
                  for i in prodotti), name="balance_first")
    m.addConstrs((x[i, t] + s[i, t - 1] - s[i, t] == domanda[i, t]
                  for i in prodotti for t in mesi[1:-1]), name="balance")
    m.addConstrs((x[i, ultimo] + s[i, ultimo - 1] == domanda[i, ultimo] + scorta_finale[i]
                  for i in prodotti), name="balance_last")
    # capacity of the shared resource
    v_cap = m.addConstrs(
        (gp.quicksum(ore_unit[i] * x[i, t] for i in prodotti) <= capacita[t]
         for t in mesi), name="capacity")
    m.setObjective(
        gp.quicksum(costo_prod[i] * x[i, t] for i in prodotti for t in mesi)
        + gp.quicksum(costo_giac[i] * s[i, t] for i in prodotti for t in mesi_s), GRB.MINIMIZE)
    return m, x, s, v_cap


# ----------------------------------------------------------------------
# 2. BASIC LP: solution and duals
# ----------------------------------------------------------------------
intestazione("Basic LP: minimum cost with mandatory service")
m, x, s, v_cap = costruisci_lp()
m.optimize()
assert m.Status == GRB.OPTIMAL
print(f"Optimal total cost: {m.ObjVal:,.2f} €")

def scorta(i, t):
    """stock at the end of month t: the variable s_it for t < m, the datum r_im for t = m"""
    return s[i, t].X if t < ultimo else scorta_finale[i]


piano = pd.DataFrame(
    [(i, t, x[i, t].X, scorta(i, t)) for i in prodotti for t in mesi],
    columns=["product", "month", "production", "stock"])
salva_dati(piano, "produzione_piano_ottimo")
print("\nProduction plan (units/month):")
print(piano.pivot(index="product", columns="month", values="production").round(1))
print(f"\nEnd-of-month stock (month {ultimo}: the required final stock r_i{ultimo}, a datum):")
print(piano.pivot(index="product", columns="month", values="stock").round(1))

print("\nCapacity constraints: utilisation, shadow price and validity range")
righe_duali = []
for t in mesi:
    uso = sum(ore_unit[i] * x[i, t].X for i in prodotti)
    c = v_cap[t]
    righe_duali.append((t, uso, capacita[t], c.Pi, c.SARHSLow, c.SARHSUp))
    print(f"  month {t}: usage {uso:6.1f}/{capacita[t]} hours | "
          f"shadow price {c.Pi:6.3f} €/hour | valid for b_t in [{c.SARHSLow:6.1f}, {c.SARHSUp:6.1f}]")
duali = pd.DataFrame(righe_duali, columns=["month", "hours_used", "capacity", "shadow_price",
                                           "rhs_min", "rhs_max"])
salva_dati(duali, "produzione_duali_capacita")

# check of the shadow price by perturbation (month with the most negative dual:
# in the Gurobi convention, for a <= constraint in a minimisation problem Pi <= 0)
t_star = duali.loc[duali["shadow_price"].idxmin(), "month"]
pi_star = duali["shadow_price"].min()
m2, x2, s2, v2 = costruisci_lp()
v2[t_star].RHS = capacita[t_star] + 1
m2.optimize()
print(f"\nCheck: +1 hour in month {t_star} -> cost goes from {m.ObjVal:.2f} to {m2.ObjVal:.2f} "
      f"(change {m2.ObjVal - m.ObjVal:+.3f} = shadow price {pi_star:.3f})")

# ----------------------------------------------------------------------
# 3. FIGURES (data for pgfplots + matplotlib preview)
# ----------------------------------------------------------------------
salva_dat(pd.DataFrame({
    "month": mesi,
    **{f"x{i}": [x[i, t].X for t in mesi] for i in prodotti},
    **{f"s{i}": [scorta(i, t) for t in mesi] for i in prodotti},       # month m: the datum r_im
    **{f"d{i}": [domanda[i, t] for t in mesi] for i in prodotti},
    "domtot": [sum(domanda[i, t] for i in prodotti) for t in mesi],
}), "cap05_piano")

fig = plt.figure(figsize=(10.5, 8.4))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], hspace=0.42, wspace=0.28)
ax1 = fig.add_subplot(gs[0, :])           # 1. ore macchina a_i x_it impilate e capacità b_t
ax2 = fig.add_subplot(gs[1, 0])           # 2. produzione x_it e domanda d_it per prodotto
ax3 = fig.add_subplot(gs[1, 1])           # 3. scorte s_it
colori = {i: c for i, c in zip(prodotti, [TEAL, ROSSO, VERDE])}
sotto = np.zeros(len(mesi))
for i in prodotti:
    ore_i = np.array([ore_unit[i] * x[i, t].X for t in mesi])
    ax1.bar(mesi, ore_i, bottom=sotto, width=0.6, color=colori[i], label=f"product {i}: machine hours $a_{i} x_{{{i}t}}$")
    sotto += ore_i
for k, t in enumerate(mesi):
    ax1.hlines(capacita[t], t - 0.4, t + 0.4, colors=ROSSO, linestyles="--", lw=1.8,
               label="capacity $b_t$ (hours available)" if k == 0 else None)
    if sotto[k] >= capacita[t] - 1e-6:
        ax1.text(t, capacita[t] + 8, "binding", ha="center", fontsize=8, color=ROSSO)
ax1.plot([], [], " ", label="binding: capacity constraint active (all hours used)")      # voce di sola legenda
ax1.set_ylim(0, max(capacita.values()) * 1.12)
ax1.set_xticks(mesi); ax1.set_xlabel("month"); ax1.set_ylabel("hours")
ax1.set_title("Machine hours used by product and capacity (the bar height is the month's total)")
ax1.legend(fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1.0))   # fuori a destra: non copre le barre
larg = 0.26
for k, i in enumerate(prodotti):
    ax2.bar([t + (k - 1) * larg for t in mesi], [x[i, t].X for t in mesi], width=larg, color=colori[i],
            label=f"product {i}: production $x_{{{i}t}}$")
for k, i in enumerate(prodotti):
    ax2.plot([t + (k - 1) * larg for t in mesi], [domanda[i, t] for t in mesi], "--", marker="D", ms=4,
             color=colori[i], mfc="white", lw=1.2, label=f"product {i}: demand $d_{{{i}t}}$")
ax2.set_ylim(0, max(domanda.values()) * 1.6)
ax2.set_xticks(mesi); ax2.set_xlabel("month"); ax2.set_ylabel("units")
ax2.set_title("Production and demand by product")
ax2.legend(fontsize=7, ncol=2, loc="upper left")
for i in prodotti:                        # stock s_it (months 1..m-1) and, hollow, the datum r_im of month m
    ax3.plot(mesi_s, [s[i, t].X for t in mesi_s], marker="o", color=colori[i], label=f"product {i}")
    ax3.plot([mesi_s[-1], ultimo], [s[i, mesi_s[-1]].X, scorta_finale[i]], "--", color=colori[i], lw=1)
    ax3.plot([ultimo], [scorta_finale[i]], "o", color=colori[i], mfc="white")
ax3.plot([], [], "o", color=GRIGIO, mfc="white", label=f"month {ultimo}: final stock $r_{{i{ultimo}}}$ (datum)")
ax3.set_xticks(mesi); ax3.set_xlabel("month"); ax3.set_ylabel("units in stock")
ax3.set_title("End-of-month inventory")
ax3.set_ylim(-3, max([s[i, t].X for i in prodotti for t in mesi_s] + [10]) * 1.6)
ax3.legend(fontsize=8, loc="upper left")
salva_figura(fig, "cap05_piano_scorte")

# sensitivity: optimal cost as the uniform capacity varies
intestazione("Sensitivity: optimal cost as capacity varies")
fattori = np.linspace(0.90, 1.35, 19)
costi = []
for f in fattori:
    ms, xs_, ss_, vs = costruisci_lp()
    for t in mesi:
        vs[t].RHS = capacita[t] * f
    ms.optimize()
    costi.append(ms.ObjVal if ms.Status == GRB.OPTIMAL else np.nan)
    print(f"  capacity x{f:4.2f}: cost {costi[-1]:10.2f} €")

tab_cap = pd.DataFrame({"percent": fattori * 100, "cost": costi}).dropna()
salva_dat(tab_cap, "cap05_capacita")

fig, ax = plt.subplots()
ax.plot(fattori * 100, costi, "-o", color=TEAL)
ax.axvline(100, color=ARANCIO, linestyle="--", label="current capacity")
ax.set_xlabel("available capacity (% of the current one)")
ax.set_ylabel("optimal total cost (€)")
ax.set_title("Value curve of capacity: convex and decreasing")
ax.legend()
salva_figura(fig, "cap05_valore_capacita")

print("\nDone: chapter 5.")
