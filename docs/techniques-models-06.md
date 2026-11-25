# Example 4.9 — Choice of desserts

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Model:** numerical · **Techniques:** [4.2 Production planning](techniques-02.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Choice of desserts"

    A person wishes to determine which desserts to eat and in what quantities the next day. The available desserts are fruit cake and ice cream. According to nutritional labels, each portion of fruit cake weighs 50 grams, provides 120 calories, and contains 5 grams of fat. Each portion of ice cream weighs 75 grams, provides 160 calories, and contains 10 grams of fat. The person aims to consume at least 120 grams of dessert, without exceeding 450 calories and 25 grams of fat. Additionally, a personal taste score is assigned to each gram of dessert on a scale from 0 (least preferred) to 10 (most preferred): 8 for fruit cake and 9 for ice cream. The goal of the person is to determine the quantities of desserts to consume that satisfy all nutritional constraints while maximizing the total taste score.

**Questions**

1. Write a Linear Programming optimization model for the problem. Identify the decisions that must be made and define the corresponding decision variables. Describe the objective function of the model and its constraints. What algorithm can be used to find an optimal solution to the model?

## Worked solution

!!! nota ""

    We assume that the person can consume any fractional portions of each dessert.

1. We introduce the following two non-negative decision variables:

    $$
    \begin{cases}
    x_1 = \text{number of portions of fruit cake}\\[1ex]
    x_2 = \text{number of portions of ice cream}
    \end{cases}
    $$

    Using these variables, a Linear Programming (LP) model for the problem reads as follows:

    !!! chiave ""

        $$
        \begin{array}{rrcrcr}
        {\max} & {\overbrace{(8 \cdot 50)}^{=400}\,x_{1}} & {+} & {\overbrace{(9 \cdot 75)}^{=675}\,x_{2}} \\[1ex]
        \text{subject to} & {120\,x_{1}} & {+} & {160\,x_{2}} & {\le} & {450} \\[1ex]
        & {5\,x_{1}} & {+} & {10\,x_{2}} & {\le} & {25} \\[1ex]
        & {50\,x_{1}} & {+} & {75\,x_{2}} & {\ge} & {120} \\[1ex]
        & {x_{1},} &  & {x_{2}} & {\ge} & {0}
        \end{array}
        $$

    Description of the objective function and constraints of the LP model:

    - the linear objective function maximizes the total taste score;

    - the first linear constraint ensures that the total caloric intake from the selected portions does not exceed the specified limit;

    - the second linear constraint restricts the total fat intake to the specified maximum;

    - the third linear constraint guarantees that the person consumes at least the specified number of grams of dessert per day;

    - the final constraint defines the variables of the model.

<!-- laboratorio-interattivo: sezione aggiunta per l'app dei nove modelli -->

## Interactive lab { #interactive-lab }

The app solves this model in the browser, with the data of the example: the sliders change the main data and the simplex method recomputes the optimal solution, the optimal value and the shadow prices. It also opens full page in the [interactive lab](lab/techniques.md), with the other eight worked models.

<div class="gi gi-capitolo" data-grafico="pl-tecniche" data-funzione="dolci"></div>
