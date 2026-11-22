# 1. Introduction to LP modelling

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-01-introduction.pdf)

!!! nota "Prerequisites"

    - From the *Linear Programming* module, [Chapter 4 «Linear Programming problems»](https://fabiofurini.github.io/linear-programming/lp-problems/04-lp-problems/): the form of a Linear Programming problem: objective function, linear constraints, domains of the variables.

!!! chiave "Objectives"

    At the end of this chapter you will be able to:

    - describe the path of every chapter: managerial problem, model, Python and solver, interpretation;

    - use the notation of the course for data, variables, duals, reduced costs and slacks;

    - explain why the course uses continuous variables only and what this buys;

    - find your way in the map of the models and in the structure of each chapter.

## What we shall do

The course teaches how to use linear programming as a tool for *decision making*, not
merely for computation. Every chapter starts from a concrete managerial problem — how much
to produce, how to charge a fleet, how efficient a branch is, how much risk to accept.

The problem becomes a linear programming model, implemented in Python, solved with a solver
and, above all, *interrogated*: how much is one extra hour of capacity worth? Does the
solution hold up if the data change by 5%? Which trade-off would we recommend to a decision
maker?

!!! tip "The right question"
    At the end of every laboratory session the question is not only *«what is the
    optimum?»*, but *«which decision do we recommend and how robust is it?»*. The value of
    a model lies in the quality of the recommendation it allows us to formulate.

## Linear models and acronyms used

All the models of the course are **LP** (*Linear Programming*): the objective and the
constraints are linear functions of the variables. An LP is always a convex problem: every
local optimum is also global, and [duality](theory-lp.md) holds without exceptions. The
other acronyms are defined at first use in the respective chapter.

The prerequisite is the module
[Linear Programming](https://fabiofurini.github.io/linear-programming/), in particular
duality and sensitivity analysis. Models with a quadratic or nonlinear objective are in the
module [NLP Modelling](https://fabiofurini.github.io/nlp-modelling/).

## Notation

Throughout the course the same convention applies:

- **scalars and indices**: lowercase italic letters ($x_{it}$, $b_t$, $\lambda$, $i$, $t$);
- **numbered objects**: products, channels, securities, vehicles, scenarios are numbered and the indices run over explicitly enumerated sets, $i \in \{1, 2, \dots, n\}$;
- **counts**: positive integers ($n \in \mathbb{Z}_{\ge 1}$); **numerical data**: rational values, $\mathbb{Q}_{> 0}$ or $\mathbb{Q}_{\ge 0}$;
- **vectors**: lowercase boldface ($\boldsymbol{x}$), all column vectors, with $\boldsymbol{a}'\boldsymbol{b}$ the scalar product; **matrices**: uppercase boldface ($\boldsymbol{A}$);
- **graphs**: $G = (N, A)$ with nodes $N$ and arcs $A$, the only sets that are not enumerated;
- **dual variables** $\pi_i$, one per constraint; **reduced costs** $\bar c_j$; **slacks** $\bar s_i$;
- **solutions**: the *bar* denotes the values of a feasible solution ($\bar x_j$, $\bar\pi_i$), the *tilde* those of an optimal one ($\tilde x_j$, $\tilde\pi_i$, $\tilde z$).

In every model the variables are introduced before the formulation, the non-negativity
constraints close the model and, after the model, a list describes the objective and the
constraints family by family, with the number of constraints in each.

## A deliberate choice: continuous variables only

All the models of the course use **exclusively continuous variables**: no binary or integer
variables. It is a deliberate choice, with three motivations.

1. **Teaching**: with continuous variables we can rely on duality, shadow prices and reduced costs, the tools that turn a numerical solution into an economic explanation.
2. **Coverage**: many real decisions are naturally continuous: quantities, flows, portfolio weights, power levels, weights.
3. **Progression**: the same tools — an LP, its dual, the shadow prices — serve production, finance and statistics, without changing solver.

## Map of the models

Chapters 1–4 form the **Modelling** part: introduction, background, solver and
[modelling techniques](techniques.md). The applied cases follow:

| Ch. | Application | Class | Central concept |
|---|---|---|---|
| 5 | [Multi-period production and inventory](production.md) | LP | duality, capacity |
| 6 | [Electric vehicle charging](ev-charging.md) | LP | energy, peaks |
| 7 | [Data Envelopment Analysis](dea.md) | LP | relative efficiency |
| 8 | [Newsvendor and variants](newsvendor.md) | stoch. LP | deciding before knowing |
| 9 | [VaR and CVaR](var-cvar.md) | LP | tail risk |
| 10 | [Arbitrage and pricing](arbitrage.md) | LP | the duality that prices |
| 11 | [Robust and quantile regression](regression.md) | LP | estimating with an LP |

## Structure of each chapter

Every application chapter follows the same eight-step outline:

1. **managerial motivation**: the problem told as a business decision;
2. **guided construction of the model**: sets, parameters, variables, constraints and objective, explained line by line;
3. **numerical example worked out by hand**: a minimal instance solved with all the steps;
4. **case study**: a realistic instance with reproducible data (CSV);
5. **Python/Gurobi implementation**: the complete code, with comments;
6. **results**: the solver output translated into managerial language;
7. **sensitivity analysis**: shadow prices, scenarios, trade-offs;
8. **exercises**: from verification to a small research extension.

!!! warning "The numbers come from the scripts"
    The numbers of each chapter are generated by the scripts in the `python/` folder:
    every script runs on its own (for example `python3 lab05_production.py`). If you
    modify the data, just run the chapter script again.

The essential path comprises four laboratory sessions, described in
[How to work with the course](organization.md).

## In summary

!!! chiave "In summary"

    - Every chapter goes from a managerial problem to a model, to Python and the solver; the model does not just return a number, it is interrogated.

    - The bar marks the values of a feasible solution, the tilde those of an optimal one; $\pi_i$ are duals, $\bar c_j$ reduced costs, $\bar s_i$ slacks.

    - Continuous variables only, by choice: duality, shadow prices and reduced costs then apply to every model.

    - Each chapter follows the same outline: motivation, model, example by hand, case study, code, results, sensitivity and exercises.
