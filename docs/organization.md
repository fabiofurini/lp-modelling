# Organization of the lab

<!-- collana-dalla-home -->
## The lab at a glance

**4 modelling chapters · 7 application chapters · LP models only · one Colab
notebook per chapter · reproducible Python/Gurobi code.** The full list, chapter
by chapter, is in the [syllabus](syllabus.md).

<div class="grid cards" markdown>

-   :material-clipboard-check-outline: **Self-assessment**

    ---

    *Mock exam*

    A new mock exam at every start: 13 questions, 33 points, with the solutions and links to the notes.

    [:octicons-arrow-right-24: Test yourself](self-assessment.md)

</div>

## Download as PDF

- 📘 **[Full lecture notes](pdf/lp-modelling-notes.pdf)** — models, worked examples, case studies, sensitivity analysis
- 📊 **[Lecture slides](downloads.md)** — one deck per chapter of the notes, on the [downloads](downloads.md) page

## Getting started

Nothing to install: every chapter has its own
[notebook that opens in Colab](notebooks.md) and runs in the browser. Those who
prefer to work locally find the commands and the notes on the Gurobi licence on
the same page.
<!-- /collana-dalla-home -->

## Essential path in four lab sessions

| | Content | Learning objectives |
|---|---|---|
| **Lab 1** | Production and inventory | formulate a multi-period LP; read duals, slacks and ranges; verify a shadow price by perturbation |
| **Lab 2** | Data Envelopment Analysis | build one LP per unit; read the envelopment form (peers and targets); tell weak from strong efficiency |
| **Lab 3** | Newsvendor *or* CVaR | formulate a scenario LP; read the optimal quantile; measure the cost of protection |
| **Lab 4** | Project of your choice | EV charging, arbitrage or robust and quantile regression; managerial presentation |

## The most common mistakes

1. Reading `.X` or `.Pi` without checking `m.Status`.
2. Forgetting `lb=-GRB.INFINITY` on the free variables ($b$ of the regression, $\eta$ of the CVaR).
3. Using a shadow price outside its validity range.
4. Getting the sign of the duals wrong in minimization problems.
5. Updating the RHS of a constraint that contains constants on the left-hand side.
6. Optimizing a single objective when the problem has two (pure minimax).
7. Choosing the parameters ($\tau$, $r$, the budget) by looking at the data used to decide.
8. Reporting six decimal digits from estimates that wobble at the second.

## Reproducibility

```bash
python3 -m pip install gurobipy matplotlib pandas scipy   # scipy: statistical functions only
python3 python/lab05_production.py   # every script runs on its own
```

The slides are on the [downloads](downloads.md) page; the solutions to the exercises of the cases are distributed in class, those of the [modelling techniques](techniques.md#exercises) open below each exercise.
