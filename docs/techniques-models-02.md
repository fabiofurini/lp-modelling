# Example 4.5 — Transportation from warehouses to clients

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf) · [:material-gesture-tap: App: Transportation from warehouses to customers](lab/transportation.md)

**Model:** symbolic · **Techniques:** [4.4 Transportation](techniques-04.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Transportation from warehouses to clients"

    A company has $s \in \mathbb{Z}_{\ge 1}$ warehouses and transports its product to $r \in \mathbb{Z}_{\ge 1}$ clients. For each warehouse $i \in \{1, 2, \dots, s\}$, the value $d_i \in \mathbb{Q}_{> 0}$ represents the maximum capacity in liters of product that can be transported from that warehouse to the clients per week. For each client $j \in \{1, 2, \dots, r\}$, the value $e_j \in \mathbb{Q}_{> 0}$ denotes the demand in liters of product of that client per week. For each warehouse $i \in \{1, 2, \dots, s\}$ and each client $j \in \{1, 2, \dots, r\}$, the value $f_{ij} \in \mathbb{Q}_{> 0}$ represents the cost in euros of transporting one liter of product from warehouse $i$ to client $j$. The company aims to determine a weekly minimum-cost transportation plan for the product from the warehouses to the clients subject to the constraints described above.

**Questions**

1. Write a *Linear Programming* (LP) model for the problem.  Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints. What algorithm can be used to find an optimal solution of the model?

2. Consider now an instance of the problem in which there are $s=2$ warehouses and $r=3$ clients. These are the other input data:

    | $f_{ij}$ | $j=1$ | $j=2$ | $j=3$ |
    |---|---|---|---|
    | $i=1$ | 3 | 2 | 1 |
    | $i=2$ | 2 | 4 | 1 |

    |  | $i=1$ | $i=2$ |
    |---|---|---|
    | $d_i$ | 120 | 110 |

    |  | $j=1$ | $j=2$ | $j=3$ |
    |---|---|---|---|
    | $e_j$ | 50 | 60 | 100 |

    Write the LP model for this instance.

3. Find a feasible solution of the  LP model of the  instance and accordingly an upper bound on the optimal solution value of the LP model for the  instance.

4. Write the dual model of the LP model and the dual model for the  instance. Find a feasible solution of the dual model of the  instance and accordingly a lower bound on the optimal solution value of the LP model for the  instance.

## Worked solution

1. We introduce the following $r \; s$ non-negative  variables:

    $$
    \begin{gathered}
    x_{ij} = \text{ liters of product transported from warehouse } i \text{ to client } j, \\[0.5ex]
    \forall i \in \{1,2,\dots,s\}, ~ \forall j \in \{1,2,\dots,r\}.
    \end{gathered}
    $$

    Using these variables, an LP model for the problem reads as follows:

    !!! chiave ""

        <a id="eq-sm2-LP"></a>

        \begin{align*}
        \min  ~~ \sum_{i=1}^s \sum_{j=1}^r  f_{ij} \; x_{ij} & & \label{sm2-obj}  \tag{1a}\\[1ex]
        \text{subject to} \quad  \sum_{j=1}^r   x_{ij}  &\le d_i,       & \forall  i \in \{1,2,\dots,s\},               \label{sm2-cons1}  \tag{1b}\\[1ex]
        \sum_{i=1}^s   x_{ij}  &= e_{j},       & \forall  j \in \{1,2,\dots,r\}               , \label{sm2-cons2}  \tag{1c}\\[1ex]
        x_{ij}                        &\ge  0, & \forall i \in \{1,2,\dots,s\},  \forall j \in \{1,2,\dots,r\}. \label{sm2-cons3} \tag{1d}
        \end{align*}

    Description of the objective function and constraints of the LP model:

    - the linear objective function $\eqref{sm2-obj}$ minimizes the total transportation cost;

    - the linear constraints $\eqref{sm2-cons1}$ ensure that the total quantity of product transported from each warehouse does not exceed its available capacity ($s$ linear constraints);

    - the linear constraints $\eqref{sm2-cons2}$ ensure that each client receives exactly the amount of product it has requested ($r$ linear constraints);

    - the linear constraints $\eqref{sm2-cons3}$ define the variables of the LP model.

    The LP model can be solved to optimality, for example, by  the simplex algorithm.

2. The LP model [(1)](#eq-sm2-LP) for the specific instance reads as follows:

    $$
    \begin{array}{rrcrcrcrcrcrcr}
    {\min} & {3\,x_{11}} & {+} & {2\,x_{12}} & {+} & {x_{13}} & {+} & {2\,x_{21}} & {+} & {4\,x_{22}} & {+} & {x_{23}} \\[1ex]
    \text{subject to} & {x_{11}} & {+} & {x_{12}} & {+} & {x_{13}} &  &  &  &  &  &  & {\le} & {120} \\[1ex]
    &  &  &  &  &  &  & {x_{21}} & {+} & {x_{22}} & {+} & {x_{23}} & {\le} & {110} \\[1ex]
    & {x_{11}} &  &  &  &  & {+} & {x_{21}} &  &  &  &  & {=} & {50} \\[1ex]
    &  &  & {x_{12}} &  &  &  &  & {+} & {x_{22}} &  &  & {=} & {60} \\[1ex]
    &  &  &  &  & {x_{13}} &  &  &  &  & {+} & {x_{23}} & {=} & {100} \\[1ex]
    & {x_{11},} &  & {x_{12},} &  & {x_{13},} &  & {x_{21},} &  & {x_{22},} &  & {x_{23}} & {\ge} & {0}
    \end{array}
    $$

3. For example, by setting:

    $$
    \bar{x}_{11}=50,~~\bar{x}_{12}=60,~~\bar{x}_{13}=10,~~\bar{x}_{21}=0,~~\bar{x}_{22}=0,~~\bar{x}_{23}=90
    $$

    we have a feasible solution.   The objective function value of this feasible  solution is:

    $$
    \sum_{i=1}^s \sum_{j=1}^r  f_{ij} \; \bar x_{ij} = 3\cdot 50 + 2 \cdot 60 + 1 \cdot 10 + 2 \cdot 0 + 4 \cdot 0 + 1 \cdot 90 =  370
    $$

    accordingly 370 is an upper bound on the optimal solution value of the LP model  [(1)](#eq-sm2-LP). So, for this instance,  we have:

    $$
    z(~ LP~) ~\le~  370
    $$

4. By using

    - a non-positive dual variable $\mu_{i}$ for each  constraint $\eqref{sm2-cons1}$ ($i \in \{1,2,\dots,s\}$)

    - a free dual variable $\pi_j$ for each constraint $\eqref{sm2-cons2}$ ($j \in \{1,2,\dots,r\}$)

    the dual model of the LP model [(1)](#eq-sm2-LP) reads as follows:

    !!! chiave ""

        <a id="eq-sm2-DUAL"></a>

        \begin{align*}
        \max ~~  \sum_{i=1}^{s}  d_i \; \mu_{i} + \sum_{j =1}^r e_{j} \: \pi_j & &  \tag{2a}\\[1ex]
        \text{subject to}  \quad    \; \mu_{i} +  \pi_j &\le f_{ij},       & \forall i \in \{1,2,\dots,s\}, \forall j \in \{1,2,\dots,r\},  \tag{2b}\\[1ex]
        \mu_{i}                        &\le  0, & \forall i \in \{1,2,\dots,s\},  \tag{2c}\\[1ex]
        \pi_{j}       &\gtreqless 0, & \forall j \in \{1,2,\dots,r\}. \tag{2d}
        \end{align*}

    The dual model [(2)](#eq-sm2-DUAL) for the specific instance reads as follows:

    $$
    \begin{array}{rrcrcrcrcrcr}
    {\max} & {120\,\mu_{1}} & {+} & {110\,\mu_{2}} & {+} & {50\,\pi_{1}} & {+} & {60\,\pi_{2}} & {+} & {100\,\pi_{3}} \\[1ex]
    \text{subject to} & {\mu_{1}} &  &  & {+} & {\pi_{1}} &  &  &  &  & {\le} & {3} \\[1ex]
    & {\mu_{1}} &  &  &  &  & {+} & {\pi_{2}} &  &  & {\le} & {2} \\[1ex]
    & {\mu_{1}} &  &  &  &  &  &  & {+} & {\pi_{3}} & {\le} & {1} \\[1ex]
    &  &  & {\mu_{2}} & {+} & {\pi_{1}} &  &  &  &  & {\le} & {2} \\[1ex]
    &  &  & {\mu_{2}} &  &  & {+} & {\pi_{2}} &  &  & {\le} & {4} \\[1ex]
    &  &  & {\mu_{2}} &  &  &  &  & {+} & {\pi_{3}} & {\le} & {1} \\[1ex]
    & {\mu_{1},} &  & {\mu_{2}} &  &  &  &  &  &  & {\le} & {0} \\[1ex]
    &  &  &  &  & {\pi_{1},} &  & {\pi_{2},} &  & {\pi_{3}} & {\gtreqless} & {0}
    \end{array}
    $$

    For example, by setting:

    $$
    \bar\mu_1=0,~~\bar\mu_2=0
    $$

    and by setting:

    $$
    \bar \pi_1=\min\{3,2\}=2,~~\bar \pi_2=\min\{2,4\}=2,~~\bar \pi_3=\min\{1,1\}= 1
    $$

    we have a feasible dual solution.

    The objective function value of this feasible dual solution is:

    $$
    \sum_{i=1}^{s}  d_i \; \bar \mu_{i} + \sum_{j =1}^r e_{j} \: \bar \pi_j = 120\cdot 0+ 110 \cdot 0 + 50 \cdot 2 + 60 \cdot 2 +100 \cdot 1   =  320
    $$

    Accordingly  $320$ is a lower bound on the optimal solution value of the model. So, for this instance,  we have:

    $$
    320 ~\le~ z(~ LP~) ~\le~  370
    $$

<!-- laboratorio-interattivo: sezione aggiunta per l'app dei nove modelli -->

## Interactive lab { #interactive-lab }

A transportation model is solved in the browser by the app [Transportation from warehouses to customers](lab/transportation.md) of the interactive lab, on an instance with two warehouses and three customers: the sliders change the data and the simplex method recomputes the optimal solution.
