# 4.9 What cannot be modelled

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** the limits of Linear Programming · [All the techniques](techniques.md)

## Requirements that need integer variables

!!! chiave "Outside Linear Programming"

    The following requirements *cannot* be written as linear constraints on continuous variables, and they need **integer** variables:

    1. **indivisible quantities**, for example the number of machines to buy or of vehicles to use;
    2. **yes/no decisions**, for example whether to open a warehouse or not;
    3. **fixed costs**, that is, a cost which is paid only if the associated activity is performed;
    4. **either-or constraints**, that is, requirements of which at least one out of two has to hold;
    5. **minimum positive quantities**, for example “*either produce nothing, or produce at least $q$ units*”.

    These requirements are the subject of **Integer Linear Programming**.

## Two frequent mistakes

- Writing a fixed cost as a non-linear term of the objective function.
- Imposing a minimum positive quantity with the constraint $x_j \ge q$: it forbids the solution $x_j = 0$, which instead has to remain feasible.

## The LP model is still useful

The LP model obtained by ignoring these requirements is a **relaxation** of the correct model.
Its optimal value is then an upper bound on the optimal value of the correct model, for a
maximization problem, and a lower bound for a minimization problem.

The models with integer variables are in the
[MIP Modelling](https://fabiofurini.github.io/mip-modelling/) module: fixed cost, minimum lot
and either-or constraints are among the [links between variables](https://fabiofurini.github.io/mip-modelling/links/).
