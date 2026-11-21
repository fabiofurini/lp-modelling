# Tools

What you need before the models: the theory that lets you *interrogate* a
solution (duality, shadow prices, reduced costs) and the solver you build and solve the
models with.

<div class="grid cards" markdown>

-   :material-function-variant: **Theory: linear programming**

    ---

    Primal-dual pair in general form, duality rules, weak and strong duality,
    complementary slackness, shadow prices, sensitivity analysis and the
    sensitivity protocol used in every chapter.

    [:octicons-arrow-right-24: Go to the page](theory-lp.md)

-   :material-console: **Solver: linear models**

    ---

    The five steps to build a model with `gurobipy`, how to run it, how to read
    the solution, shadow prices, reduced costs and validity ranges.

    [:octicons-arrow-right-24: Go to the page](solver-lp.md)

</div>

## Linear models and prerequisites

All the models of the course are **LP** (*Linear Programming*): linear objective
and constraints. An LP is always convex: every local optimum is global and duality
holds without exceptions. The prerequisite is the module
[Linear Programming](https://fabiofurini.github.io/linear-programming/), in particular duality and sensitivity analysis.
Models with a quadratic or nonlinear objective are in the module
[NLP Modelling](https://fabiofurini.github.io/nlp-modelling/).

**Notation used throughout the course.** Scalars and indices in lowercase
($x_{it}$, $\lambda$); the objects of the models (products, channels, assets,
scenarios…) are **numbered** and the indices run over explicitly enumerated sets,
$i \in \{1, 2, \dots, n\}$; integer counts ($n \in \mathbb{Z}_{\ge 1}$),
rational data ($\mathbb{Q}$); vectors in lowercase bold ($\boldsymbol{x}$),
matrices in uppercase bold ($\boldsymbol{A}$). Dual variables $\pi_i$, reduced
costs $\bar c_j$, slacks $\bar s_i$: the **bar** denotes the values of a feasible
solution, the **tilde** those of an optimal one ($\tilde x_j$, $\tilde z$). In
the models the wording is always "subject to", the variables are introduced before
the formulation and the constraints defining them close the model.
