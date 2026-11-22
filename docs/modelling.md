# Modelling

Before the cases, the tools to build them: how to write a Linear Programming model from a
description, how to interrogate it with duality and how to bring it to Python/Gurobi. The
cases of the following parts all use these four chapters.

!!! success "At the end of this part you can"
    - Write an LP model from a text: variables with their units, objective, constraints.
    - Recognize the standard patterns: production, blending, transportation, multi-period.
    - Linearize min-max, absolute values and ratios, and tell when it cannot be done.
    - Read shadow prices and reduced costs with their validity ranges.
    - Build and solve the model in `gurobipy`, and read what it answers.

Four chapters, in this order: the introduction with the notation of the course; the
background on duality and sensitivity needed to interrogate a solution; the solver; the
modelling techniques, one per page.

<div class="grid cards" markdown>

-   :material-flag-outline: **1. Introduction to LP modelling**

    ---

    What we shall do, the notation, why continuous variables only, the map of the models
    and the structure of each chapter.

    [:octicons-arrow-right-24: The chapter](introduction.md)

-   :material-function-variant: **2. Background: linear programming and sensitivity analysis**

    ---

    The rules of duality, complementary slackness, shadow prices and reduced costs with
    their ranges, and the sensitivity protocol used in every chapter.

    [:octicons-arrow-right-24: The chapter](theory-lp.md)

-   :material-console: **3. The solver: building, solving, interpreting**

    ---

    The five steps to build a model with `gurobipy`, how to run it, how to read the
    solution, shadow prices, reduced costs and validity ranges.

    [:octicons-arrow-right-24: The chapter](solver-lp.md)

-   :material-link-variant: **4. Modelling techniques**

    ---

    From the description to the model, production, blending, transportation,
    multi-period, min-max, absolute values, ratios and what LP cannot express.

    [:octicons-arrow-right-24: The nine techniques](techniques.md)

</div>
