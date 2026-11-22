# 4.2 Production planning

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** standard pattern, canonical maximization form · [All the techniques](techniques.md)

## The problem

A company produces $r \in \mathbb{Z}_{\ge 1}$ different products using $s \in \mathbb{Z}_{\ge 1}$
limited resources. For each product $j \in \{1,2,\dots,r\}$, the value $c_j \in \mathbb{Q}_{> 0}$
is the profit of one unit of product.

For each resource $i \in \{1,2,\dots,s\}$, the value $b_i \in \mathbb{Q}_{> 0}$ is the available
quantity, and $a_{ij} \in \mathbb{Q}_{\ge 0}$ is the quantity of resource $i$ consumed by one
unit of product $j$. The company aims to determine a maximum profit production plan.

## The model

We introduce the following $r$ non-negative variables:

$$
x_j = \text{units of product } j \text{ produced}, \qquad \forall j \in \{1,2,\dots,r\} .
$$

Using these variables, an LP model for the problem reads as follows:

$$
\begin{aligned}
\max ~~ \sum_{j=1}^{r} c_j\, x_j & & \\
\text{subject to} \quad \sum_{j=1}^{r} a_{ij}\, x_j &\le b_i, & \forall i \in \{1,2,\dots,s\}, \\
x_j &\ge 0, & \forall j \in \{1,2,\dots,r\} .
\end{aligned}
$$

- The objective function is the total profit.
- The constraints impose that the consumption of every resource does not exceed its availability.
- This is an LP problem in **canonical maximization form**.

## Example

!!! example "Example 4.1: production planning"

    Consider an instance with $r=2$ products and $s=3$ resources:

    |  | $j=1$ | $j=2$ |
    |---|---|---|
    | $c_j$ | 3 | 5 |
    | $a_{1j}$ | 1 | 0 |
    | $a_{2j}$ | 0 | 2 |
    | $a_{3j}$ | 3 | 2 |

    | $b_1$ | $b_2$ | $b_3$ |
    |---|---|---|
    | 4 | 12 | 18 |

    The LP model for this instance reads as follows:

    $$
    \begin{array}{rrcrcr}
    {\max} & {3\,x_{1}} & {+} & {5\,x_{2}} \\[1ex]
    \text{subject to} & {x_{1}} &  &  & {\le} & {4} \\[1ex]
    &  &  & {2\,x_{2}} & {\le} & {12} \\[1ex]
    & {3\,x_{1}} & {+} & {2\,x_{2}} & {\le} & {18} \\[1ex]
    & {x_{1},} &  & {x_{2}} & {\ge} & {0}
    \end{array}
    $$

    An optimal solution is $\tilde x_1 = 2$ and $\tilde x_2 = 6$, with optimal value $z(\mathit{LP}) = 36$.

<!-- modelli:inizio -->
**Worked models that use this technique:** [Example 4.4 — Production with regular time and overtime](techniques-models-01.md) · [Example 4.9 — Choice of desserts](techniques-models-06.md) · [Example 4.12 — Production of three drugs](techniques-models-09.md)
<!-- modelli:fine -->
