---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# LP Modelling

<!-- collana-riga -->
<p class="collana-riga" markdown>A course of the <b>Operations Research and Mathematics</b> series · [all the courses](#the-series)</p>
<!-- /collana-riga -->

Teaching material designed and developed by **[Fabio Furini](https://fabiofurini.github.io/)**, associate
professor at [DIAG](https://www.diag.uniroma1.it/), Sapienza University of Rome.

The course presents modelling with linear programming: how to build a model, the solver and the
interpretation of the solution, modelling techniques, and models of production and inventory,
electric vehicle charging, Data Envelopment Analysis, the newsvendor, VaR and CVaR, arbitrage and
robust regression, with Python/Gurobi code.

Prerequisites: [Linear Programming](https://fabiofurini.github.io/linear-programming/) (duality and sensitivity analysis).

[Start :material-arrow-right:](modelling.md){ .md-button .md-button--primary }
[:material-pencil: Exercises](exercises/index.md){ .md-button }
[:material-gesture-tap: Lab](lab/index.md){ .md-button }
[:material-clipboard-check-outline: Quiz](self-assessment.md){ .md-button }
[:material-download: Downloads](downloads.md){ .md-button }

</div>

<!-- collana-app -->
## Try it now

The transportation problem from two warehouses to three customers, solved to optimality in the browser: change one cost and the capacity of a warehouse with the sliders and the simplex method recomputes the optimal shipments and their cost.

<div class="gi" data-grafico="pl-trasporto"></div>

[:material-gesture-tap: More apps in the lab](lab/index.md){ .md-button }
<!-- /collana-app -->

## The parts of the course

<div class="grid cards" markdown>

-   :material-vector-polygon: **Modelling**

    ---

    From the description to the model: the techniques (production, blending,
    transportation, multi-period, linearizations), duality to interrogate the solution, the solver.

    [:octicons-arrow-right-24: The four chapters](modelling.md)

-   :material-factory: **Deterministic models**

    ---

    Production and inventory, electric vehicle charging, branch efficiency:
    every datum is known.

    [:octicons-arrow-right-24: The three problems](deterministic-models.md)

-   :material-dice-multiple: **Decisions under uncertainty**

    ---

    You decide before you know: the quantile rule, tail risk and the duality that
    prices financial instruments.

    [:octicons-arrow-right-24: The three problems](decisions-uncertainty.md)

-   :material-robot: **Optimization and machine learning**

    ---

    Robust and quantile regression as an LP: absolute deviations, support
    points from the duals and the quantile the newsvendor needs.

    [:octicons-arrow-right-24: The problem](optimization-ml.md)

</div>

<!-- collana-da-non-perdere -->
## Don't miss

<div class="grid cards" markdown>

-   :material-pencil-box-multiple: **Exercises**

    ---

    Modelling exercises for every chapter, at exam level, on the case studies of the course.

    [:octicons-arrow-right-24: The exercises](exercises/index.md)

-   :material-clipboard-check-outline: **Self-assessment quiz**

    ---

    A new mock exam at every start: 13 questions, 33 points, with the solution and the link to the notes. Downloads also has the full question bank.

    [:octicons-arrow-right-24: Test yourself](self-assessment.md)

-   :material-gesture-tap: **Interactive lab**

    ---

    Apps running in the browser: move the parameters and watch the ideas of the course at work, one step at a time.

    [:octicons-arrow-right-24: The lab](lab/index.md)

-   :material-download: **Lecture notes in PDF**

    ---

    Lecture notes, exercise books and slides in PDF, with the same numbering as the website.

    [:octicons-arrow-right-24: Downloads](downloads.md)

-   :material-language-python: **Notebooks in Colab**

    ---

    The code of the course running in the browser, with nothing to install.

    [:octicons-arrow-right-24: The notebooks](notebooks.md)

-   :material-format-list-numbered: **Full index**

    ---

    All the chapters with their sections on one page, and how each chapter is organized.

    [:octicons-arrow-right-24: The index](syllabus.md)

</div>
<!-- /collana-da-non-perdere -->

---

<!-- collana -->
## The series

All the courses of the series are built the same way: lecture notes online and in PDF, exercises with solutions, an interactive lab and self-assessment quizzes.

<div class="grid cards" markdown>

-   :material-function-variant: **[Mathematical Analysis 1](https://fabiofurini.github.io/mathematical-analysis-1/)**

    real numbers, functions, limits, derivatives and series, with interactive graphs

-   :material-matrix: **[Linear Algebra](https://fabiofurini.github.io/linear-algebra/)**

    vectors, matrices, determinants, linear systems and eigenvalues, with the computation lab

-   :material-code-braces: **[Algorithms](https://fabiofurini.github.io/algorithms/)**

    number representation, pseudo-code, sorting and searching, analysis and recursive algorithms

-   :material-vector-triangle: **[Linear Programming](https://fabiofurini.github.io/linear-programming/)**

    polyhedra, the simplex algorithm, duality and the dual simplex, with the interactive lab

-   :material-dots-grid: **[Integer Linear Programming](https://fabiofurini.github.io/integer-linear-programming/)**

    LP relaxation, valid inequalities, cutting planes, branch-and-bound and branch-and-cut

-   :material-vector-curve: **[Convex Optimization](https://fabiofurini.github.io/convex-optimization/)**

    convex sets and functions, convex optimization problems, with interactive graphs

-   :material-graph-outline: **[Network Optimization](https://fabiofurini.github.io/network-optimization/)**

    graphs, spanning trees, shortest paths, network flows, the network simplex and project management

-   :material-hexagon-multiple-outline: **[Combinatorial Optimization Problems](https://fabiofurini.github.io/combinatorial-optimization/)**

    knapsack, bin packing, coloring, TSP, scheduling and lot sizing: the problems, their formulations and ad hoc algorithms

-   :material-table-large: **[Dynamic Programming](https://fabiofurini.github.io/dynamic-programming/)**

    principles and DP algorithms for knapsack, lot sizing, coin change and rod cutting

-   :material-map-marker-path: **[Heuristic Algorithms](https://fabiofurini.github.io/heuristic-algorithms/)**

    constructive heuristics, local search, metaheuristics and MIP heuristics for combinatorial optimization problems

-   :material-approximately-equal: **[Approximation Algorithms](https://fabiofurini.github.io/approximation-algorithms/)**

    performance guarantees, approximation schemes and limits of approximation for combinatorial problems

-   :material-chart-line: **LP Modelling** · *this course*

    linear programming models of managerial problems, solved with Python and Gurobi

-   :material-chart-bell-curve-cumulative: **[NLP Modelling](https://fabiofurini.github.io/nlp-modelling/)**

    nonlinear programming models, from portfolios to machine learning, with Python and Gurobi

-   :material-vector-polygon: **[MIP Modelling](https://fabiofurini.github.io/mip-modelling/)**

    integer linear programming models, from the formulation to the solution with solvers

</div>
<!-- /collana -->

---

Teaching material by **[Fabio Furini](https://fabiofurini.github.io/)** —
[DIAG](https://www.diag.uniroma1.it/), Sapienza University of Rome.
