# Example 4.4 — Production with regular time and overtime

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf) · [:material-gesture-tap: App: Production with regular time and overtime](lab/overtime-production.md)

**Model:** symbolic · **Techniques:** [4.2 Production planning](techniques-02.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Production with regular time and overtime"

    A company produces $r \in \mathbb{Z}_{\ge 1}$ different  products. For each product $i \in \{1, 2, \dots, r\}$, the value $w_i \in \mathbb{Q}_{>0}$ is the maximum production quantity in liters of the product per day.  Each product can be further treated and sold at a higher price. The maximum quantity per day of all products that can be treated is $d \in \mathbb{Q}_{> 0}$ liters during regular time and $e \in \mathbb{Q}_{> 0}$ liters during overtime. For each product $i \in \{1, 2, \dots, r\}$, the value $a_i \in \mathbb{Q}_{> 0}$ is the profit in euros of one liter of product not treated; the values $b_i \in \mathbb{Q}_{> 0}$ and $c_i \in \mathbb{Q}_{> 0}$ are the profits in euros of one liter of product  treated during regular time and overtime, respectively. The company aims to determine a maximum profit daily production plan subject to the constraints described above.

**Questions**

1. Write a  *Linear Programming* (LP) model for the problem.  Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints.   What algorithm can be used to find an optimal solution of the model?

2. Consider now an instance of the problem in which there are $r=3$ products. These are the other input data:

    |  | $i=1$ | $i=2$ | $i=3$ |
    |---|---|---|---|
    | $w_i$ | 35 | 30 | 25 |
    | $a_i$ | 3 | 2 | 2 |
    | $b_i$ | 6 | 4 | 4 |
    | $c_i$ | 5 | 3 | 3 |

    | $d$ | $e$ |
    |---|---|
    | 30 | 20 |

    Write the LP model for this specific instance.

3. Find a feasible solution of the  LP model of the  instance and accordingly a lower bound on the optimal solution value of the LP model for the  instance.

4. Write the dual model of the LP model and the dual model for the  instance. Find a feasible solution of the dual model of the  instance and accordingly an upper bound on the optimal solution value of the LP model for the  instance.

## Worked solution

1. We introduce the following  $3 \; r$ non-negative variables:

    $$
    \begin{cases}
    x_i = \text{  liters of product } i \text{ not treated per day}\\[1ex]
    y_i = \text{  liters of product } i \text{ treated in regular time per day}\\[1ex]
    z_i = \text{  liters of product } i \text{ treated in overtime per day}
    \end{cases}
    \quad \forall i \in \{1,2,\dots,r\}.
    $$

    Using these variables, an LP model for the problem reads as follows:

    !!! chiave ""

        <a id="eq-sm1-LP"></a>

        \begin{align*}
        \max ~~ \sum_{i=1}^{r} a_i \;  x_i +  \sum_{i=1}^{r} b_i  \; y_i+  \sum_{i=1}^{r} c_i \;  z_i & & \label{sm1-obj}  \tag{1a}\\[1ex]
        \text{subject to} \quad     x_i + y_i + z_i  &\le w_i,       & \forall  i \in \{1,2,\dots,r\},               \label{sm1-cons1}  \tag{1b}\\[1ex]
        \sum_{i=1}^{r}   y_i  &\le d,       &  \label{sm1-cons2}  \tag{1c}\\[1ex]
        \sum_{i=1}^{r}   z_i  &\le e,       &  \label{sm1-cons3}  \tag{1d}\\[1ex]
        x_i                        &\ge  0, & \forall i \in \{1,2,\dots,r\}, \label{sm1-cons4}  \tag{1e}\\[1ex]
        y_i                        &\ge  0, & \forall i \in \{1,2,\dots,r\}, \label{sm1-cons5}  \tag{1f}\\[1ex]
        z_i                        &\ge  0, & \forall i \in \{1,2,\dots,r\}. \label{sm1-cons6} \tag{1g}
        \end{align*}

    Description of the objective function and constraints of the LP model:

    - the linear objective function $\eqref{sm1-obj}$ maximizes the total profit of the production plan;

    - the linear constraints $\eqref{sm1-cons1}$ ensure that, for each product, the total  production does not exceed the available capacity ($r$ linear constraints);

    - the linear constraint $\eqref{sm1-cons2}$ ensures that the total quantity of products treated during regular time does not exceed the available capacity (one linear constraint);

    - the linear constraint $\eqref{sm1-cons3}$ ensures that the total quantity of products treated during overtime does not exceed the available capacity (one linear constraint);

    - the linear constraints $\eqref{sm1-cons4}$, $\eqref{sm1-cons5}$, and $\eqref{sm1-cons6}$ define the variables of the LP model.

    The LP model can be solved to optimality, for example, by  the simplex algorithm.

2. The LP model [(1)](#eq-sm1-LP)  for the instance reads as follows:

    $$
    \begin{array}{rrcrcrcrcrcrcrcrcrcr}
    {\max} & {3\,x_{1}} & {+} & {2\,x_{2}} & {+} & {2\,x_{3}} & {+} & {6\,y_{1}} & {+} & {4\,y_{2}} & {+} & {4\,y_{3}} & {+} & {5\,z_{1}} & {+} & {3\,z_{2}} & {+} & {3\,z_{3}} \\[1ex]
    \text{subject to} & {x_{1}} &  &  &  &  & {+} & {y_{1}} &  &  &  &  & {+} & {z_{1}} &  &  &  &  & {\le} & {35} \\[1ex]
    &  &  & {x_{2}} &  &  &  &  & {+} & {y_{2}} &  &  &  &  & {+} & {z_{2}} &  &  & {\le} & {30} \\[1ex]
    &  &  &  &  & {x_{3}} &  &  &  &  & {+} & {y_{3}} &  &  &  &  & {+} & {z_{3}} & {\le} & {25} \\[1ex]
    &  &  &  &  &  &  & {y_{1}} & {+} & {y_{2}} & {+} & {y_{3}} &  &  &  &  &  &  & {\le} & {30} \\[1ex]
    &  &  &  &  &  &  &  &  &  &  &  &  & {z_{1}} & {+} & {z_{2}} & {+} & {z_{3}} & {\le} & {20} \\[1ex]
    & {x_{1},} &  & {x_{2},} &  & {x_{3},} &  & {y_{1},} &  & {y_{2},} &  & {y_{3},} &  & {z_{1},} &  & {z_{2},} &  & {z_{3}} & {\ge} & {0}
    \end{array}
    $$

3. For example, by setting:

    $$
    \bar{x}_{1}=5,~~\bar{x}_{2}=30,~~\bar{x}_{3}=25,~~\bar{y}_{1}=30,~~\bar{y}_{2}=0,~~\bar{y}_{3}=0,~~\bar{z}_{1}=0,~~\bar{z}_{2}=0,~~\bar{z}_{3}=0
    $$

    we have a feasible solution.   The objective function value of this feasible  solution is:

    $$
    \sum_{i=1}^{r} a_i \; \bar  x_i +  \sum_{i=1}^{r} b_i  \; \bar y_i+  \sum_{i=1}^{r} c_i \;  \bar z_i = 3 \cdot 5 + 2 \cdot 30 + 2 \cdot 25 + 6 \cdot 30 + 4 \cdot 0 + 4 \cdot 0 + 5 \cdot 0 + 3 \cdot 0 + 3 \cdot 0=  305
    $$

    accordingly $305$ is a lower bound for the optimal solution value of the LP model [(1)](#eq-sm1-LP). So, for this instance, we have:

    $$
    305 ~\le~ z(~LP~)
    $$

4. By using

    - a non-negative dual variable $\lambda_i$ for each  constraint $\eqref{sm1-cons1}$ ($i \in \{1,2,\dots,r\}$)

    - a non-negative dual variable $\pi$ for the constraint $\eqref{sm1-cons2}$

    - a non-negative dual variable $\varrho$ for the constraint $\eqref{sm1-cons3}$

    the dual of the LP model [(1)](#eq-sm1-LP) reads as follows:

    !!! chiave ""

        <a id="eq-sm1-DUAL"></a>

        \begin{align*}
        \min  ~~ \sum_{i=1}^{r}  w_i \; \lambda_i + d \; \pi + e \; \varrho & &  \tag{2a}\\[1ex]
        \text{subject to}  \quad   \lambda_i  &\ge a_i,       & \forall i \in \{1,2,\dots,r\},  \tag{2b}\\[1ex]
        \lambda_i + \pi  &\ge b_i,       &               \forall i \in \{1,2,\dots,r\},  \tag{2c}\\[1ex]
        \lambda_i + \varrho  &\ge c_i,       &  \forall i \in \{1,2,\dots,r\},  \tag{2d}\\[1ex]
        \lambda_i                        &\ge  0, & \forall i \in \{1,2,\dots,r\},  \tag{2e}\\[1ex]
        \pi &\ge  0, &  \tag{2f}\\[1ex]
        \varrho                        &\ge  0. & \tag{2g}
        \end{align*}

    The dual model [(2)](#eq-sm1-DUAL) for the specific instance reads as follows:

    $$
    \begin{array}{rrcrcrcrcrcr}
    {\min} & {35\,\lambda_{1}} & {+} & {30\,\lambda_{2}} & {+} & {25\,\lambda_{3}} & {+} & {30\,\pi} & {+} & {20\,\varrho} \\[1ex]
    \text{subject to} & {\lambda_{1}} &  &  &  &  &  &  &  &  & {\ge} & {3} \\[1ex]
    &  &  & {\lambda_{2}} &  &  &  &  &  &  & {\ge} & {2} \\[1ex]
    &  &  &  &  & {\lambda_{3}} &  &  &  &  & {\ge} & {2} \\[1ex]
    & {\lambda_{1}} &  &  &  &  & {+} & {\pi} &  &  & {\ge} & {6} \\[1ex]
    &  &  & {\lambda_{2}} &  &  & {+} & {\pi} &  &  & {\ge} & {4} \\[1ex]
    &  &  &  &  & {\lambda_{3}} & {+} & {\pi} &  &  & {\ge} & {4} \\[1ex]
    & {\lambda_{1}} &  &  &  &  &  &  & {+} & {\varrho} & {\ge} & {5} \\[1ex]
    &  &  & {\lambda_{2}} &  &  &  &  & {+} & {\varrho} & {\ge} & {3} \\[1ex]
    &  &  &  &  & {\lambda_{3}} &  &  & {+} & {\varrho} & {\ge} & {3} \\[1ex]
    & {\lambda_{1},} &  & {\lambda_{2},} &  & {\lambda_{3},} &  & {\pi,} &  & {\varrho} & {\ge} & {0}
    \end{array}
    $$

    For example, by setting:

    $$
    \bar\pi=0,~~\bar\varrho=0,~~
    $$

    and by setting:

    $$
    \bar \lambda_1=\max\{3,6,5\}=6,~~\bar \lambda_2=\max\{2,4,3\}=4,~~\bar \lambda_3=\max\{2,4,3\}= 4
    $$

    we have a feasible dual solution.

    The objective function value of this feasible dual solution is:

    $$
    \sum_{i=1}^{r}  w_i \; \bar \lambda_i + d \; \bar \pi + e \; \bar \varrho =  35 \cdot 6 + 30 \cdot 4 +25 \cdot 4 +30 \cdot 0 +20 \cdot 0  =  430
    $$

    Accordingly  $430$ is an upper bound on the optimal solution value of the model. So, for this instance, we have:

    $$
    305 ~\le~ z(~LP~) ~\le~  430
    $$

<!-- laboratorio-interattivo: sezione aggiunta per l'app dei nove modelli -->

## Interactive lab { #interactive-lab }

The app solves this model in the browser, with the data of the example: the sliders change the data and the simplex method recomputes the optimal solution and the shadow prices. It also opens full page in the interactive lab: [Production with regular time and overtime](lab/overtime-production.md).

<div class="gi gi-capitolo" data-grafico="pl-straordinario"></div>
