# 4.3 Blending

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Technique:** standard pattern, composition requirements · [All the techniques](techniques.md)

## The problem

A quantity $d \in \mathbb{Q}_{> 0}$ of a final product has to be obtained by mixing
$r \in \mathbb{Z}_{\ge 1}$ raw materials. For each raw material $j \in \{1,2,\dots,r\}$, the
value $c_j \in \mathbb{Q}_{> 0}$ is the cost of one unit.

The final product has to contain at least a quantity $q_k \in \mathbb{Q}_{\ge 0}$ of each of
$s \in \mathbb{Z}_{\ge 1}$ components, and $p_{kj} \in \mathbb{Q}_{\ge 0}$ is the quantity of
component $k$ contained in one unit of raw material $j$. The company aims to determine a
minimum cost blend.

## The model

We introduce the following $r$ non-negative variables:

$$
x_j = \text{units of raw material } j \text{ used in the blend}, \qquad \forall j \in \{1,2,\dots,r\} .
$$

Using these variables, an LP model for the problem reads as follows:

$$
\begin{aligned}
\min ~~ \sum_{j=1}^{r} c_j\, x_j & & \\
\text{subject to} \quad \sum_{j=1}^{r} x_j &= d, & \\
\sum_{j=1}^{r} p_{kj}\, x_j &\ge q_k, & \forall k \in \{1,2,\dots,s\}, \\
x_j &\ge 0, & \forall j \in \{1,2,\dots,r\} .
\end{aligned}
$$

- The equality constraint imposes that the total quantity produced is $d$.
- The $\ge$ constraints impose the minimum quantity of each component.

## Fractions of the blend

A requirement of the form “*the raw material $j$ has to be at least a fraction $f$ of
the blend*” is *not* written as $\frac{x_j}{\sum_{\ell} x_{\ell}} \ge f$, which is not a
linear constraint. It is written instead by multiplying both sides by the denominator, which
is positive:

$$
\begin{aligned}
& x_j \ge f \; \sum_{\ell = 1}^{r} x_{\ell} \\
\Longleftrightarrow \quad & (1 - f) \; x_j - f \sum_{\ell \ne j} x_{\ell} \ge 0 .
\end{aligned}
$$

The general rule is in the technique [4.8 Ratios and percentages](techniques-08.md).

## Example

!!! example "Example 4.2: blending"

    A company has to produce $d=100$ kilograms of animal feed by mixing $r=3$ raw materials, whose costs per kilogram are $c_1 = 0.80$, $c_2 = 0.50$ and $c_3 = 0.30$ euros.

    The feed has to contain at least $q_1 = 8$ kilograms of proteins, and one kilogram of each raw material contains, respectively, $p_{11} = 0.12$, $p_{12} = 0.08$ and $p_{13} = 0.03$ kilograms of them. Moreover, the first raw material has to be at least the $20\%$ of the blend.

    The LP model for this instance reads as follows:

    $$
    \begin{array}{rrcrcrcr}
    {\min} & {0.80\,x_{1}} & {+} & {0.50\,x_{2}} & {+} & {0.30\,x_{3}} \\[1ex]
    \text{subject to} & {x_{1}} & {+} & {x_{2}} & {+} & {x_{3}} & {=} & {100} \\[1ex]
    & {0.12\,x_{1}} & {+} & {0.08\,x_{2}} & {+} & {0.03\,x_{3}} & {\ge} & {8} \\[1ex]
    & {0.80\,x_{1}} & {-} & {0.20\,x_{2}} & {-} & {0.20\,x_{3}} & {\ge} & {0} \\[1ex]
    & {x_{1},} &  & {x_{2},} &  & {x_{3}} & {\ge} & {0}
    \end{array}
    $$

    The third constraint is the proportion requirement $x_1 \ge 0.20 \, (x_1 + x_2 + x_3)$, rewritten as a linear constraint.

    An optimal solution is $\tilde x_1 = 20$, $\tilde x_2 = 64$ and $\tilde x_3 = 16$, with optimal value

    $$
    z(\text{LP}) = 0.80 \cdot 20 + 0.50 \cdot 64 + 0.30 \cdot 16 = 52.80 \text{ euros} .
    $$

<!-- modelli:inizio -->
**Worked models that use this technique:** [Example 4.6 — Diet planning](techniques-models-03.md) · [Example 4.7 — Diet planning for several classes](techniques-models-04.md) · [Example 4.11 — Blending of crude oil in a refinery](techniques-models-08.md)
<!-- modelli:fine -->
