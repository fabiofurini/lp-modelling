# 4.7 Absolute values

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** linearization with auxiliary variables · [All the techniques](techniques.md)

## The non-linear form

A term $\left| \sum_{j=1}^n a_{ij} \, x_j \right|$ in the objective function is not linear. It
can be linearized when it appears with a *positive* coefficient in a *minimized* objective
function.

## The linear constraints

!!! chiave "Linearization of the absolute value"

    One introduces one additional non-negative variable $w_i$ and writes

    $$
    w_i \ge \sum_{j=1}^n a_{ij} \, x_j ,
    \qquad
    w_i \ge - \sum_{j=1}^n a_{ij} \, x_j .
    $$

## Why it works

- The two constraints impose $w_i \ge \left| \sum_{j} a_{ij} \, x_j \right|$.
- The minimization makes the inequality tight at an optimal solution.

## The second form

Under the *same condition* (positive coefficient in a minimized objective function, or
negative coefficient in a maximized one), the same term is linearized by writing

$$
\sum_{j=1}^n a_{ij} \, x_j = w_i^{+} - w_i^{-}, \qquad w_i^{+}, w_i^{-} \ge 0,
$$

and by replacing the absolute value with $w_i^{+} + w_i^{-}$.

- The optimization makes at least one of $w_i^{+}$ and $w_i^{-}$ equal to $0$ at an optimal solution, and then $w_i^{+} + w_i^{-} = \left| \sum_{j} a_{ij} \, x_j \right|$.
- Without that condition, both variables could be positive and the model would be wrong.

The least absolute deviations regression of the chapter
[11. Robust and quantile regression](regression.md) uses this technique on real data.
