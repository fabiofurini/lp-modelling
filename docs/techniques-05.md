# 4.5 Multi-period planning

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** standard pattern, inventory balance · [All the techniques](techniques.md)

## The problem

A company has to satisfy the demand of a product over a time horizon of
$n \in \mathbb{Z}_{\ge 1}$ periods. For each period $t \in \{1,2,\dots,n\}$, the value
$d_t \in \mathbb{Q}_{\ge 0}$ is the demand and $p_t \in \mathbb{Q}_{> 0}$ is the maximum production.

Moreover, $c_t \in \mathbb{Q}_{> 0}$ is the unit production cost and $h_t \in \mathbb{Q}_{> 0}$
is the unit cost of storing one unit from period $t$ to period $t+1$.

## The model

We introduce the following $2\,n$ non-negative variables:

$$
\begin{cases}
x_t = \text{units produced in period } t\\[1ex]
y_t = \text{units stored at the end of period } t
\end{cases}
\qquad \forall t \in \{1,2,\dots,n\} .
$$

Using these variables, an LP model for the problem reads as follows (with $y_0 = 0$):

$$
\begin{aligned}
\min ~~ \sum_{t=1}^{n} c_t\, x_t + \sum_{t=1}^{n} h_t\, y_t & & \\
\text{subject to} \quad y_{t-1} + x_t - y_t &= d_t, & \forall t \in \{1,2,\dots,n\}, \\
x_t &\le p_t, & \forall t \in \{1,2,\dots,n\}, \\
x_t &\ge 0, & \forall t \in \{1,2,\dots,n\}, \\
y_t &\ge 0, & \forall t \in \{1,2,\dots,n\} .
\end{aligned}
$$

## The inventory balance

!!! chiave "Inventory balance constraints"

    In every period, what was in stock at the end of the previous period plus what is produced equals the demand plus what is left in stock:

    $$
    y_{t-1} + x_t - y_t = d_t, \qquad \forall t \in \{1,2,\dots,n\} .
    $$

    They are the key of every multi-period model, and they link consecutive periods.

## The complete case

The chapter [5. Multi-period production and inventory](production.md) uses this pattern with
several products and shared machine-hour capacities. There you find the data, the code, the
shadow prices of the capacity and the sensitivity analysis.

<!-- modelli:inizio -->
**Worked models that use this technique:** [Example 4.8 — Multi-period production with purchases and storage](techniques-models-05.md) · [Example 4.10 — Production and storage of fruit cakes](techniques-models-07.md)
<!-- modelli:fine -->
