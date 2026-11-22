# 2. Background: linear programming and sensitivity analysis

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-02-background.pdf)

!!! nota "Prerequisites"

    - From the module *Linear Programming*, [Chapter 9 «Duality theory»](https://fabiofurini.github.io/linear-programming/duality/09-duality/): the dual of a Linear Programming problem, weak and strong duality, complementary slackness.

    - From the module *Linear Programming*, [Chapter 14 «Sensitivity analysis»](https://fabiofurini.github.io/linear-programming/advanced-methods/14-sensitivity/): shadow prices, reduced costs and their validity ranges.

!!! chiave "Objectives"

    At the end of this chapter you will be able to:

    - write the dual of an LP in general form with the conversion rules;

    - check optimality with complementary slackness;

    - deduce the sign of a shadow price from the direction of the constraint and the sense of the objective;

    - read a shadow price and a reduced cost together with their validity ranges;

    - apply the six steps of the sensitivity protocol.

The linear programming background used throughout the course: duality, optimality
conditions, sensitivity analysis and the sensitivity protocol of every chapter. The
complete theory, with proofs, is in the module *Linear Programming*:
[“Duality theory”](https://fabiofurini.github.io/linear-programming/duality/09-duality/)
and [“Sensitivity analysis”](https://fabiofurini.github.io/linear-programming/advanced-methods/14-sensitivity/).

## Linear programming and duality

The *data* are the costs $c_j$, the coefficients $a_{ij}$ and the right-hand sides $b_i$,
with $i \in M = \{1, 2, \dots, m\}$ and $j \in N = \{1, 2, \dots, n\}$. The sets
$M_{\le}, M_{=}, M_{\ge}$ partition $M$ according to the direction of the constraint;
the sets $N_{\ge 0}, N_{\gtreqless 0}, N_{\le 0}$ partition $N$ according to the
sign of the variable (non-negative, free, non-positive).

The *variables* are the $x_j$ of the primal (P), a maximization problem in general form, and,
in the minimization dual (D), one $\pi_i$ per constraint of the primal. The two complete models
are in the chapter [“Duality theory”](https://fabiofurini.github.io/linear-programming/duality/09-duality/)
of *Linear Programming*.

**The rules of duality** — every constraint of the primal generates a dual
variable, every variable a dual constraint:

| Primal (max) | Dual (min) |
|---|---|
| constraint $\le b_i$ ($i \in M_{\le}$) | variable $\pi_i \ge 0$ |
| constraint $= b_i$ ($i \in M_{=}$) | variable $\pi_i \gtreqless 0$ |
| constraint $\ge b_i$ ($i \in M_{\ge}$) | variable $\pi_i \le 0$ |
| variable $x_j \ge 0$ ($j \in N_{\ge 0}$) | constraint $\ge c_j$ |
| variable $x_j \gtreqless 0$ ($j \in N_{\gtreqless 0}$) | constraint $= c_j$ |
| variable $x_j \le 0$ ($j \in N_{\le 0}$) | constraint $\le c_j$ |

The *equalities* of the primal give *free* dual variables (and vice versa); for a
**minimization** primal the table is read from right to left.

**Theorem (weak duality).** For every feasible solution $(\bar x_1, \dots, \bar x_n)$
of (P) and every feasible solution $(\bar\pi_1, \dots, \bar\pi_m)$ of (D):

$$
\sum_{j \in N} c_j \bar x_j \;\le\; \sum_{i \in M} b_i \bar\pi_i .
$$

**Theorem (strong duality).** (P) has an optimal solution $(\tilde x_1, \dots, \tilde x_n)$
**if and only if** (D) has an optimal solution $(\tilde\pi_1, \dots, \tilde\pi_m)$,
and in that case the optimal values coincide:

$$
\sum_{j \in N} c_j \tilde x_j \;=\; \sum_{i \in M} b_i \tilde\pi_i .
$$

If two feasible solutions, of the primal and of the dual, have the same value, they are both
optimal. The proofs and the examples of construction of the dual are in the chapter
[“Duality theory”](https://fabiofurini.github.io/linear-programming/duality/09-duality/)
of *Linear Programming*.

## The optimality conditions of LP: complementary slackness

To every constraint we associate its *slack* $\bar s_i$, and to every variable
its *reduced cost* $\bar c_j$, that is the slack of the corresponding *dual*
constraint:

$$
\bar s_i = \sum_{j \in N} a_{ij} \bar x_j - b_i, \quad \forall i \in M,
\qquad
\bar c_j = c_j - \sum_{i \in M} a_{ij} \bar\pi_i, \quad \forall j \in N.
$$

The slack measures how far the constraint is from being binding; the reduced
cost measures $c_j$ net of the value of the resources consumed, at the shadow
prices.

A pair of feasible solutions is optimal for both problems **if and only if** the
**complementary slackness** conditions hold:

$$
\bar\pi_i \cdot \bar s_i = 0, \quad \forall i \in M,
\qquad
\bar x_j \cdot \bar c_j = 0, \quad \forall j \in N.
$$

In words: **slack constraint ⇒ dual at zero**, and variable different from zero ⇒
reduced cost null. At the optimum these are *implications*, not equivalences
(degeneracy: there may exist a variable at zero with null reduced cost).

**Two readings to remember:**

- **shadow price** $\tilde\pi_i = \partial \tilde z / \partial b_i$: the marginal
  value of the right-hand side; it holds within the **validity range of the
  right-hand side** $[b_i^{\min}, b_i^{\max}]$, the largest interval in which,
  varying only $b_i$, the shadow price remains exactly $\tilde\pi_i$. Inactive
  constraint ⇒ $\tilde\pi_i = 0$;
- **reduced cost** $\bar c_j$: for a variable at zero, by how much $c_j$ must
  improve for it to become worth activating; it holds within the **validity range
  of the coefficient** $[c_j^{\min}, c_j^{\max}]$, the largest interval in which,
  varying only $c_j$, the optimal solution does not change (for a variable at zero
  the profitability threshold is one of the two endpoints). Variable different
  from zero ⇒ $\bar c_j = 0$.

**The signs of shadow prices.** The sign of
$\tilde\pi_i = \partial \tilde z / \partial b_i$ is deduced by answering two
questions: *does increasing $b_i$ enlarge or shrink the feasible region?* (it
enlarges it with $\le$, it shrinks it with $\ge$); *how does a wider region change
the optimum?* (it can never worsen it).

| Direction of the constraint | minimization | maximization |
|---|---|---|
| $\le$ ($b_i$ ↑ ⇒ wider region) | $\tilde\pi_i \le 0$ | $\tilde\pi_i \ge 0$ |
| $\ge$ ($b_i$ ↑ ⇒ narrower region) | $\tilde\pi_i \ge 0$ | $\tilde\pi_i \le 0$ |
| $=$ | any sign | any sign |

An **inactive** constraint always has $\tilde\pi_i = 0$ (complementarity).

!!! example "Duality on the 2×2 LP, worked out in full"
    The 2×2 LP used throughout the course is $\max 30x_1 + 50x_2$ with $x_1 + 3x_2 \le 90$,
    $2x_1 + x_2 \le 80$ and $x_1, x_2 \ge 0$; its dual is $\min 90\pi_1 + 80\pi_2$ with
    $\pi_1 + 2\pi_2 \ge 30$, $3\pi_1 + \pi_2 \ge 50$ and $\pi_1, \pi_2 \ge 0$.

    **Solving we obtain**: $(\tilde x_1, \tilde x_2) = (30, 20)$,
    $\tilde z = 1900$, $(\tilde\pi_1, \tilde\pi_2) = (14, 8)$,
    $(\bar c_1, \bar c_2) = (0, 0)$, with validity ranges
    $[b_1^{\min}, b_1^{\max}] = [40, 240]$, $[b_2^{\min}, b_2^{\max}] = [30, 180]$,
    $[c_1^{\min}, c_1^{\max}] = [50/3, 100]$, $[c_2^{\min}, c_2^{\max}] = [15, 90]$;
    both constraints active.

    **Checks**: $x_1, x_2 \ne 0$ ⇒ dual constraints active
    ($\bar c_1 = \bar c_2 = 0$) and strong duality:

    $$
    14 + 16 = 30 = c_1, \qquad 42 + 8 = 50 = c_2,
    \qquad 90 \cdot 14 + 80 \cdot 8 = 1900 = \tilde z . \quad ✓
    $$

## Sensitivity analysis in LPs

Together with the solution, four numbers for each constraint and variable come free:

- the **shadow price** $\tilde\pi_i$: marginal value of the right-hand side;
- the **validity range of the right-hand side** $[b_i^{\min}, b_i^{\max}]$
  (in the 2×2 example: the shadow price 14 holds while $b_1$ stays in $[40, 240]$);
- the **reduced cost** $\bar c_j$: for a variable at zero, by how much its
  coefficient must improve for it to become worth activating;
- the **validity range of the coefficient** $[c_j^{\min}, c_j^{\max}]$
  (in the 2×2 example: $c_1$ can vary in $[50/3, 100]$ and $c_2$ in $[15, 90]$
  without moving the solution).

!!! example "Shadow prices in practice"
    On the 2×2 LP ($\tilde z = 1900$, $\tilde\pi_1 = 14$): one extra unit of
    $b_1$ is worth 14; if it cost 12, it would be worth it. By perturbation:

    $$
    b_1 = 91 \Rightarrow 1914 = 1900 + 14,
    \qquad
    b_1 = 100 \Rightarrow 2040 = 1900 + 10 \cdot 14,
    $$

    exact because $100 \in [40, 240]$. At $b_1 = 240$ the structure changes: beyond
    that, every unit is worth less than 14. With $b_1 = 300$ the constraint would be
    inactive and the shadow price $0$.

!!! example "Reduced costs in practice: is a third variable worth it?"
    Let us add to the 2×2 LP a variable $x_3 \ge 0$ with coefficient $c_3 = 20$
    and consumptions $a_{13} = a_{23} = 1$. At the shadow prices the resources
    absorbed are worth

    $$
    1 \cdot 14 + 1 \cdot 8 = 22 > 20 = c_3 ,
    \qquad
    \bar c_3 = 20 - 22 = -2 :
    $$

    the solution remains $(30, 20, 0)$ with $\tilde z = 1900$ and $c_3^{\max} = 22$ —
    the coefficient would have to rise to at least 22. Counter-check with
    $c_3 = 23$: the solution changes to $(0, 5, 75)$, value 1975.

## The sensitivity protocol (used in every chapter)

1. **Base scenario**: solve, verify, identify the active constraints.
2. **One-at-a-time**: vary one key parameter over a grid.
3. **Shadow prices and reduced costs**: compare the dual with a re-optimization
   after a perturbation; read the $\bar c_j$ of every variable at zero (its
   profitability threshold).
4. **Scenarios**: pessimistic, central, optimistic.
5. **Trade-off**: trace a frontier (cost-service, risk-return…).
6. **Stability**: data ±5% → does the recommendation hold?

## In summary

!!! chiave "In summary"

    - Every constraint generates a dual variable and every variable a dual constraint; weak duality gives a bound, strong duality equal values at the optimum.

    - Complementary slackness: a slack constraint has a null dual, a non-null variable has a null reduced cost.

    - The shadow price $\tilde\pi_i = \partial \tilde z / \partial b_i$ holds only inside its range; a number is always quoted with its range.

    - The reduced cost says by how much $c_j$ must improve for a variable at zero to be worth using.

    - The protocol: base case, one-at-a-time, shadow prices checked by perturbation, scenarios, trade-off, stability.
