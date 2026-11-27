# 4.4 Transportation

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** standard pattern, availabilities and demands · [All the techniques](techniques.md)

## The problem

A company has $s \in \mathbb{Z}_{\ge 1}$ warehouses and has to serve $r \in \mathbb{Z}_{\ge 1}$
clients. For each warehouse $i \in \{1,2,\dots,s\}$, the value $a_i \in \mathbb{Q}_{> 0}$ is the
available quantity of product.

For each client $j \in \{1,2,\dots,r\}$, the value $d_j \in \mathbb{Q}_{> 0}$ is the demand, and
$c_{ij} \in \mathbb{Q}_{\ge 0}$ is the cost of transporting one unit of product from warehouse
$i$ to client $j$. The company aims to determine a minimum cost transportation plan.

## The model

We introduce the following $s \cdot r$ non-negative variables:

$$
\begin{gathered}
x_{ij} = \text{units transported from warehouse } i \text{ to client } j, \\
\forall i \in \{1,2,\dots,s\},~\forall j \in \{1,2,\dots,r\} .
\end{gathered}
$$

Using these variables, an LP model for the problem reads as follows:

$$
\begin{aligned}
\min ~~ \sum_{i=1}^{s} \sum_{j=1}^{r} c_{ij}\, x_{ij} & & \\
\text{subject to} \quad \sum_{j=1}^{r} x_{ij} &\le a_i, & \forall i \in \{1,2,\dots,s\}, \\
\sum_{i=1}^{s} x_{ij} &\ge d_j, & \forall j \in \{1,2,\dots,r\}, \\
x_{ij} &\ge 0, & \forall i \in \{1,2,\dots,s\},~\forall j \in \{1,2,\dots,r\} .
\end{aligned}
$$

- The availability constraints impose that no warehouse ships more than its availability.
- The demand constraints impose that every client receives at least its demand.
- The model is feasible if and only if $\sum_{i} a_i \ge \sum_{j} d_j$.

## Example

!!! example "Example 4.3: transportation"

    Consider an instance with $s=2$ warehouses, of availabilities $a_1 = 50$ and $a_2 = 60$, and $r=2$ clients, of demands $d_1 = 30$ and $d_2 = 80$. The transportation costs are:

    | $c_{ij}$ | $j=1$ | $j=2$ |
    |---|---|---|
    | $i=1$ | 4 | 6 |
    | $i=2$ | 5 | 3 |

    An optimal solution is

    $$
    \tilde x_{11} = 30, \qquad \tilde x_{12} = 20, \qquad \tilde x_{21} = 0, \qquad \tilde x_{22} = 60 ,
    $$

    with optimal value

    $$
    z(\text{LP}) = 4 \cdot 30 + 6 \cdot 20 + 5 \cdot 0 + 3 \cdot 60 = 420 .
    $$

<!-- modelli:inizio -->
**Worked models that use this technique:** [Example 4.5 — Transportation from warehouses to clients](techniques-models-02.md)
<!-- modelli:fine -->
