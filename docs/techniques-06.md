# 4.6 Min-max and max-min

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** linearization with one auxiliary variable · [All the techniques](techniques.md)

## The non-linear form

Some requirements are not linear as they are written, but they can be rewritten as linear
constraints, possibly with the help of additional variables. The first case is an objective
function of the form

$$
\min ~ \max_{i \in \{1,2,\dots,m\}} \left\{ \sum_{j=1}^n a_{ij} \, x_j \right\} .
$$

## The linear constraints

!!! chiave "Linearization of the min-max"

    One introduces one additional free variable $w$ and writes

    $$
    \begin{aligned}
    &\min ~ w \\
    &\text{subject to} \quad w \ge \sum_{j=1}^n a_{ij} \, x_j , \qquad \forall i \in \{1,2,\dots,m\} .
    \end{aligned}
    $$

## Why it works

- The $m$ constraints impose that $w$ is not smaller than each of the $m$ linear functions, that is, than their maximum.
- Since $w$ is minimized, at an optimal solution it is exactly equal to that maximum.
- Symmetrically, a **max-min** objective function is linearized by introducing one additional free variable $w$, maximizing it and imposing $w \le \sum_{j} a_{ij} \, x_j$ for every $i$.

!!! warning "Only in these two directions"

    A *maximization* of a maximum, or a *minimization* of a minimum, cannot be linearized in this way.
