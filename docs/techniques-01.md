# 4.1 From the description to the model

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** the three-step method · [All the techniques](techniques.md)

## What a model is

A **model** of an optimization problem is a mathematical description of its feasible
solutions and of the quantity to be optimized. Writing a model requires three steps,
always in this order.

!!! chiave "The three steps"

    1. **Decision variables.** Identify the decisions to be taken and associate one variable with each of them. For every variable, state its *unit of measure* and its domain.

    2. **Objective function.** Write, as a linear function of the decision variables, the quantity to be maximized or minimized.

    3. **Constraints.** Write, as linear equalities or inequalities, every requirement that a feasible solution has to satisfy.

## Symbolic input data

The model is written with **symbolic input data**, so that it describes the problem for
every instance, and not only for one of them. We use the following conventions:

1. the *sizes* of the instance are integer numbers, for example $r \in \mathbb{Z}_{\ge 1}$ and $s \in \mathbb{Z}_{\ge 1}$;
2. the *numerical data* are rational numbers, for example $a_i \in \mathbb{Q}_{> 0}$ and $w_{ij} \in \mathbb{Q}_{\ge 0}$;
3. the *index sets* are written explicitly, for example $\forall i \in \{1,2,\dots,r\}$.

## Linear Programming models

A model is a **Linear Programming** model if its objective function and all its constraints
are linear, and if all its variables are continuous. In this case the model can be solved
with the simplex algorithm.

!!! warning "The three most frequent mistakes"

    1. Forgetting the **non-negativity constraints** of the variables.

    2. Writing constraints which are not *dimensionally consistent*, that is, which sum quantities with different units of measure.

    3. Using a variable in the objective function without defining it among the decision variables.
