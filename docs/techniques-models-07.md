# Example 4.10 — Production and storage of fruit cakes

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Model:** numerical · **Techniques:** [4.5 Multi-period planning](techniques-05.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Production and storage of fruit cakes"

    A bakery must plan fruit cake production over the next four days to meet daily demands of 10, 20, 30, and 20 kilograms. It starts with 5 kilograms in stock. Daily production is limited to 30 kilograms, and storage capacity at the end of each day is 10 kilograms. Production costs per kilogram are 10, 20, 30, and 40 euros, respectively. Holding one kilogram in inventory at the end of a day costs 10% of its production cost. The bakery aims to minimize total production and inventory holding costs while satisfying all demands and respecting capacity constraints.

**Questions**

1. Write a Linear Programming optimization model for the problem. Identify the decisions that must be made and define the corresponding decision variables. Describe the objective function of the model and its constraints. What algorithm can be used to find an optimal solution to the model?

## Worked solution

!!! nota ""

    We assume that the bakery can produce any fractional quantity of fruit cake.

1. We introduce the following seven non-negative decision variables:

    $$
    \begin{cases}
    x_t = \text{kilograms of fruit cake produced on day } t, & \forall t \in \{1,2,3,4\},\\[1ex]
    s_t = \text{kilograms of fruit cake stored at the end of day } t, & \forall t \in \{1,2,3\}.
    \end{cases}
    $$

    Using these variables, a Linear Programming (LP) model for the problem reads as follows:

    !!! chiave ""

        $$
        \begin{array}{rrcrcrcrcrcrcrcr}
        {\min} & {10\,x_{1}} & {+} & {20\,x_{2}} & {+} & {30\,x_{3}} & {+} & {40\,x_{4}} & {+} & {s_{1}} & {+} & {2\,s_{2}} & {+} & {3\,s_{3}} \\[0.4ex]
        \text{subject to} & {x_{1}} &  &  &  &  &  &  & {-} & {s_{1}} &  &  &  &  & {=} & {10-5} \\[0.4ex]
        &  &  & {x_{2}} &  &  &  &  & {+} & {s_{1}} & {-} & {s_{2}} &  &  & {=} & {20} \\[0.4ex]
        &  &  &  &  & {x_{3}} &  &  &  &  & {+} & {s_{2}} & {-} & {s_{3}} & {=} & {30} \\[0.4ex]
        &  &  &  &  &  &  & {x_{4}} &  &  &  &  & {+} & {s_{3}} & {=} & {20} \\[0.4ex]
        & {x_{1}} &  &  &  &  &  &  &  &  &  &  &  &  & {\le} & {30} \\[0.4ex]
        &  &  & {x_{2}} &  &  &  &  &  &  &  &  &  &  & {\le} & {30} \\[0.4ex]
        &  &  &  &  & {x_{3}} &  &  &  &  &  &  &  &  & {\le} & {30} \\[0.4ex]
        &  &  &  &  &  &  & {x_{4}} &  &  &  &  &  &  & {\le} & {30} \\[0.4ex]
        &  &  &  &  &  &  &  &  & {s_{1}} &  &  &  &  & {\le} & {10} \\[0.4ex]
        &  &  &  &  &  &  &  &  &  &  & {s_{2}} &  &  & {\le} & {10} \\[0.4ex]
        &  &  &  &  &  &  &  &  &  &  &  &  & {s_{3}} & {\le} & {10} \\[0.4ex]
        & {x_{1},} &  & {x_{2},} &  & {x_{3},} &  & {x_{4},} &  & {s_{1},} &  & {s_{2},} &  & {s_{3}} & {\ge} & {0}
        \end{array}
        $$

    Description of the objective function and constraints of the LP model:

    - the linear objective function minimizes the total production and inventory holding costs over the 4-day planning horizon;

    - the first four linear constraints ensure that, in each day, the quantity of fruit cake available—given by the initial stock and the amount produced during the day—matches the daily customer demand after accounting for what is stored at the end of the day;

    - the next eight linear constraints enforce the daily production and storage capacity limits;

    - the final constraints define the variables of the optimization model.

<!-- laboratorio-interattivo: sezione aggiunta per l'app dei nove modelli -->

## Interactive lab { #interactive-lab }

The app solves this model in the browser, with the data of the example: the sliders change the main data and the simplex method recomputes the optimal solution, the optimal value and the shadow prices. It also opens full page in the [interactive lab](lab/techniques.md), with the other eight worked models.

<div class="gi gi-capitolo" data-grafico="pl-tecniche" data-funzione="torte"></div>
