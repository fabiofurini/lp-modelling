# Syllabus

<!-- collana-dalla-fascia -->
Every chapter starts from a concrete managerial problem — how much to produce, how
to charge a fleet, how efficient a branch is, how much risk to accept — turns it
into a linear programming model, solves it with Gurobi called from Python and, above all,
*interrogates* it: how much is one extra hour of capacity worth? Does the solution hold if the data
change by 5%?

Every model can be run **right away in the browser**: each chapter has its own
[notebook that opens in Colab](notebooks.md), with nothing to install.

!!! tip "The right question"
    At the end of every lab session the question is not only *“what is the optimum?”*,
    but *“which decision do we recommend and how robust is it?”*. All the decision
    variables are **continuous** and every model is linear: we read the solution
    through duality, shadow prices and reduced costs.
<!-- /collana-dalla-fascia -->

The complete list of the chapters, in the order in which they are covered. Every
chapter has its own page, its own Python script and its own
[notebook that opens in Colab](notebooks.md).

**[Modelling](modelling.md)**

1. [Introduction to LP modelling](introduction.md) — what we shall do, notation,
   structure of the chapters
2. [Background: linear programming and sensitivity analysis](theory-lp.md) — duality,
   shadow prices, sensitivity protocol
3. [The solver: building, solving, interpreting](solver-lp.md) — building the model,
   running it, retrieving the solution, interpreting the output
4. [Modelling techniques](techniques.md) — from the description to the model,
   production, blending, transportation, multi-period, linearizations

**[Deterministic models](deterministic-models.md)**

5. [Multi-period production and inventory](production.md) — LP
6. [Electric vehicle charging](ev-charging.md) — LP
7. [Data Envelopment Analysis](dea.md) — LP and duality

**[Decisions under uncertainty](decisions-uncertainty.md)**

8. [The Newsvendor and its variants](newsvendor.md) — stochastic LP
9. [VaR and CVaR](var-cvar.md) — scenario-based LP
10. [Arbitrage and pricing](arbitrage.md) — LP and duality that prices

**[Optimization and machine learning](optimization-ml.md)**

11. [Robust and quantile regression](regression.md) — LP

**The course**

12. [Organization of the lab](organization.md) — lab sessions and mistakes
    to avoid

Prerequisite: the module [Linear Programming](https://fabiofurini.github.io/linear-programming/), in particular
duality and sensitivity analysis. Quadratic and nonlinear models are in the module
[NLP Modelling](https://fabiofurini.github.io/nlp-modelling/).

---

The four parts and what each one is for are described on the
[home page](index.md).
