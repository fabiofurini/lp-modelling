# 4.8 Ratios and percentages

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** linearization by multiplying by the denominator · [All the techniques](techniques.md)

## The non-linear form

A constraint of the form

$$
\frac{\sum_{j=1}^n a_{j} \, x_j}{\sum_{j=1}^n e_{j} \, x_j} \le \gamma ,
\qquad
\sum_{j=1}^n e_{j} \, x_j > 0 ,
$$

is not linear.

## The linear constraint

!!! chiave "Linearization of a ratio"

    One multiplies both sides by the denominator, which is positive:

    $$
    \sum_{j=1}^n \big( a_{j} - \gamma \; e_{j} \big) \, x_j \le 0 .
    $$

## When it holds

- The same technique applies to the percentage requirements of the [blending](techniques-03.md) models.
- It is correct only when the denominator is *known to be positive* for every feasible solution.
- Otherwise multiplying by it would change the direction of the inequality.
