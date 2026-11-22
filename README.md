<h3 align="center">Teaching material by
<a href="https://fabiofurini.github.io/">Fabio Furini</a></h3>
<p align="center">
  Associate professor of Operations Research ·
  <a href="https://www.diag.uniroma1.it/">DIAG</a>, Sapienza University of Rome ·
  <a href="https://fabiofurini.github.io/">personal website</a>
</p>

# LP Modelling

> **The author.** Since September 2021 Fabio Furini has been an associate
> professor at DIAG, Sapienza University of Rome. Ph.D. in Control Engineering
> and Operations Research at the University of Bologna (2011), research fellow
> there until 2012; postdoc at Université Paris-13 (2012–2013); from 2013 to 2019
> *Maître de Conférences* at Université Paris-Dauphine. *Habilitation à Diriger
> des Recherches* in France in 2017 and Italian National Scientific
> Qualification for Full Professor in Operations Research in 2019. In 2020 CNR
> researcher at IASI-CNR in Rome.
> Personal website: <https://fabiofurini.github.io/>

Linear programming models — the course lecture
notes in online form, with Python/Gurobi code, data and case studies.

**📖 Online lecture notes: [fabiofurini.github.io/lp-modelling](https://fabiofurini.github.io/lp-modelling/)**

**▶️ Runnable notebooks in Colab: [the list of chapters](https://fabiofurini.github.io/lp-modelling/notebooks/)** — they run in the browser, with nothing to install.

## Download as PDF

- [Full lecture notes](https://fabiofurini.github.io/lp-modelling/pdf/lp-modelling-notes.pdf)
- [Lecture slides](https://fabiofurini.github.io/lp-modelling/downloads/), one deck per chapter, on the downloads page

## Contents

Prerequisite: [Linear Programming](https://fabiofurini.github.io/linear-programming/) (duality and sensitivity analysis).
Quadratic and nonlinear models are in [NLP Modelling](https://fabiofurini.github.io/nlp-modelling/).

**Modelling**

- [Introduction to LP modelling](https://fabiofurini.github.io/lp-modelling/introduction/) — what we shall do, notation, structure of the chapters
- [Background: linear programming](https://fabiofurini.github.io/lp-modelling/theory-lp/) — duality, shadow prices, sensitivity protocol
- [The solver: linear models](https://fabiofurini.github.io/lp-modelling/solver-lp/) — building the model, running it, reading and interpreting the solution
- [Modelling techniques](https://fabiofurini.github.io/lp-modelling/techniques/) — production, blending, transportation, multi-period planning, linearizations

**Deterministic models**

- [Multi-period production and inventory](https://fabiofurini.github.io/lp-modelling/production/) — LP
- [Electric vehicle charging](https://fabiofurini.github.io/lp-modelling/ev-charging/) — LP
- [Data Envelopment Analysis](https://fabiofurini.github.io/lp-modelling/dea/) — LP, relative efficiency and the dual

**Decisions under uncertainty**

- [The Newsvendor and its variants](https://fabiofurini.github.io/lp-modelling/newsvendor/) — stochastic LP
- [VaR and CVaR](https://fabiofurini.github.io/lp-modelling/var-cvar/) — scenario-based LP
- [Arbitrage and pricing](https://fabiofurini.github.io/lp-modelling/arbitrage/) — LP, the duality that prices

**Optimization and machine learning**

- [Robust and quantile regression](https://fabiofurini.github.io/lp-modelling/regression/) — LP, estimating the parameters

**The course**

- [Organization of the lab](https://fabiofurini.github.io/lp-modelling/organization/) — lab sessions and mistakes to avoid

## Running the models

Every chapter has its own script in [`python/`](python/) (`lab05`–`lab11`), with the
data in [`data/`](data/):

```bash
python3 -m pip install gurobipy matplotlib pandas scipy
python3 python/run_all.py     # all models: data, results and figures
```

With nothing to install, every chapter has its own notebook in
[`notebooks/`](notebooks/): it opens in Colab from the badge at the top of the
chapter page (the full list is [on the website](https://fabiofurini.github.io/lp-modelling/notebooks/))
and runs in the browser. The notebooks are generated from the scripts —
`python3 python/make_notebooks.py` — so the course code stays in one place.

The `gurobipy` licence bundled with the pip package is enough for every model in
the course; the free academic licence can be activated at
[portal.gurobi.com](https://portal.gurobi.com).

## Licence

- **Text, figures and data** (`docs/`, `data/`): [CC BY 4.0](LICENSE) — anyone may
  reuse, adapt and redistribute them, in other courses too, with attribution.
- **Python code** (`python/`): [MIT](LICENSE-CODE), the usual licence for software,
  so that reusing the scripts raises no ambiguity.

To cite the material see [`CITATION.cff`](CITATION.cff): GitHub turns it into the
*Cite this repository* entry. Exercise solutions are not
published: they are distributed in class.

## Versione italiana

The whole course is also available in Italian:
**[fabiofurini.github.io/modellazione-pl](https://fabiofurini.github.io/modellazione-pl/)**
([repository](https://github.com/fabiofurini/modellazione-pl)).

## Same series

- [MIP Modelling](https://fabiofurini.github.io/mip-modelling/)
- [Mathematical Analysis 1](https://fabiofurini.github.io/mathematical-analysis-1/)
- [Linear Algebra](https://fabiofurini.github.io/linear-algebra/)
- [Linear Programming](https://fabiofurini.github.io/linear-programming/)
- [Convex Optimization](https://fabiofurini.github.io/convex-optimization/)
- [Algorithms](https://fabiofurini.github.io/algorithms/)

---

Teaching material by **[Fabio Furini](https://fabiofurini.github.io/)** — [DIAG](https://www.diag.uniroma1.it/), Sapienza University of Rome.
Exercise solutions are distributed in class.
