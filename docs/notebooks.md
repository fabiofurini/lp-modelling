# The notebooks of the lab

Every chapter with a model has its own **notebook**: one click on the badge opens
it in Google Colab, it installs the solver by itself and runs in the browser —
nothing to install on your machine. It is the very same code as the scripts in
`python/`, cell by cell, with the figures appearing below the cells instead of
being written to a file.

!!! tip "The pip licence is enough"
    The licence bundled with `gurobipy` is limited to 2000 variables and 2000
    constraints, and every model of the lab fits: the largest one — the scenario
    newsvendor — uses 1803 and 1801. Raising the number of scenarios can exceed it:
    in that case activate the free academic licence at
    [portal.gurobi.com](https://portal.gurobi.com).

| Chapter | Class | Notebook |
|---|---|---|
| [Multi-period production and inventory](production.md) | LP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabiofurini/lp-modelling/blob/main/notebooks/lab04_production.ipynb) |
| [Smart charging of electric vehicles](ev-charging.md) | LP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabiofurini/lp-modelling/blob/main/notebooks/lab05_ev_charging.ipynb) |
| [Data Envelopment Analysis](dea.md) | LP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabiofurini/lp-modelling/blob/main/notebooks/lab06_dea.ipynb) |
| [The Newsvendor and its variants](newsvendor.md) | 1D convex / scenario-based stochastic LP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabiofurini/lp-modelling/blob/main/notebooks/lab07_newsvendor.ipynb) |
| [VaR and CVaR: measuring and optimizing risk](var-cvar.md) | scenario-based LP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabiofurini/lp-modelling/blob/main/notebooks/lab08_var_cvar.ipynb) |
| [Arbitrage and arbitrage-free pricing](arbitrage.md) | LP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabiofurini/lp-modelling/blob/main/notebooks/lab09_arbitrage.ipynb) |
| [Robust and quantile regression](regression.md) | LP | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabiofurini/lp-modelling/blob/main/notebooks/lab10_regression.ipynb) |

## How they are made

The notebooks are not written by hand: they are generated from the scripts with

```bash
python3 python/make_notebooks.py
```

The chapter script remains the single source of the code — the notebook takes its
docstring, sections and comments from it — and whoever prefers the command line
keeps running, from the `python/` folder:

```bash
python3 lab06_markowitz.py
```

## Installation and licence

Working locally needs only `gurobipy`:

```bash
python3 -m pip install gurobipy
```

The pip package ships with a **demo licence** (up to 2000 variables and 2000 constraints):
enough for every model in this lab. At start-up the line
`Restricted license - for non-production use only` appears: this is normal.

**Full academic licence (free of charge):**

1. register at <https://portal.gurobi.com> with your institutional email (`@uniroma1.it`);
2. request a *Named-User Academic License*;
3. run the command `grbgetkey XXXXXXXX-...` shown by the portal (you need the university network or a VPN);
4. the licence is saved in `~/gurobi.lic` and from that moment there are no size limits.

Quick check:

```python
import gurobipy as gp
print(gp.gurobi.version())        # e.g. (13, 0, 3)
```

## Regenerating everything

```bash
python3 -m pip install gurobipy matplotlib pandas scipy   # scipy: statistical functions only
python3 python/run_all.py             # regenerates data, results and figures
```

The [repository](https://github.com/fabiofurini/lp-modelling)
holds all the **Python scripts** and the case study **data** in CSV format.
