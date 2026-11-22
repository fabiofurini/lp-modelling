# Example 4.11 — Blending of crude oil in a refinery

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Model:** numerical · **Techniques:** [4.3 Blending](techniques-03.md) · [4.8 Ratios and percentages](techniques-08.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Blending of crude oil in a refinery"

    A refinery has 5000 barrels of crude oil of type 1 and 10000 barrels of crude oil of type 2. The refinery produces and sells two products: gasoline and heating oil. These products are obtained by blending the two types of crude oil in appropriate proportions. Each barrel of type 1 crude oil has a quality level of 10, while each barrel of type 2 has a quality level of 5. To meet market standards, gasoline must have an average quality level of at least 8, and heating oil must have an average quality level of at least 6. Gasoline is sold at 25 dollars per barrel, and heating oil at 20 dollars per barrel. The goal of the refinery is to determine a production plan that maximizes total profit while satisfying all constraints.

**Questions**

1. Write a Linear Programming optimization model for the problem. Identify the decisions that must be made and define the corresponding decision variables. Describe the objective function of the model and its constraints. What algorithm can be used to find an optimal solution to the model?

## Worked solution

!!! nota ""

    We assume that the refinery can blend any fractional quantity of crude oil to produce gasoline and heating oil.

1. We introduce the following four non-negative decision variables:

    $$
    \left\{
    \begin{aligned}
    x_1 &= \text{barrels of crude oil type 1 used for gasoline}, \\
    x_2 &= \text{barrels of crude oil type 2 used for gasoline}, \\
    y_1 &= \text{barrels of crude oil type 1 used for heating oil}, \\
    y_2 &= \text{barrels of crude oil type 2 used for heating oil}.
    \end{aligned}
    \right.
    $$

    Using these variables, a Linear Programming (LP) model for the problem reads as follows:

    !!! chiave ""

        $$
        \begin{array}{rrcrcrcrcr}
        {\max} & {25\,x_{1}} & {+} & {25\,x_{2}} & {+} & {20\,y_{1}} & {+} & {20\,y_{2}} \\[1ex]
        \text{subject to} & {x_{1}} &  &  & {+} & {y_{1}} &  &  & {\le} & {5000} \\[1ex]
        &  &  & {x_{2}} &  &  & {+} & {y_{2}} & {\le} & {10000} \\[1ex]
        & {2\,x_{1}} & {-} & {3\,x_{2}} &  &  &  &  & {\ge} & {0} \\[1ex]
        &  &  &  &  & {4\,y_{1}} & {-} & {y_{2}} & {\ge} & {0} \\[1ex]
        & {x_{1},} &  & {x_{2},} &  & {y_{1},} &  & {y_{2}} & {\ge} & {0}
        \end{array}
        $$

    Description of the objective function and constraints of the LP model:

    - the linear objective function maximizes the total revenue from the sale of gasoline and heating oil;

    - the first two linear constraints impose the availability limits on the total usage of crude oil type 1 and type 2, respectively;

    - the third linear constraint enforces the quality requirement for gasoline. It ensures that the average quality of the crude oil blend used to produce gasoline is at least the desired amount.

        $$
        \frac{10x_1 + 5x_2}{x_1 + x_2} \ge 8 \quad \iff \quad 10x_1 + 5x_2 \ge 8(x_1 + x_2)
        \quad \iff \quad
        2x_1 - 3x_2 \ge 0
        $$

    - the fourth linear constraint enforces the quality requirement for heating oil. It ensures that the average quality of the crude oil blend used to produce heating oil is at least the desired amount.

        $$
        \frac{10y_1 + 5y_2}{y_1 + y_2} \ge 6 \quad \iff \quad 10y_1 + 5y_2 \ge 6(y_1 + y_2)
        \quad \iff \quad
        4y_1 - y_2 \ge 0
        $$

    - the final constraint defines the variables of the model.
