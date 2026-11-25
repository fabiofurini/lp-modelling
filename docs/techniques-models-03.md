# Example 4.6 — Diet planning

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf) · [:material-gesture-tap: App: Diet planning](lab/diet.md)

**Model:** symbolic · **Techniques:** [4.3 Blending](techniques-03.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Diet planning"

    A school canteen needs to determine the monthly diet for its students. It is considering $s \in \mathbb{Z}_{\ge 1}$ possible types of food (e.g., milk, rice,  bread, potatoes, etc.), each containing $r \in \mathbb{Z}_{\ge 1}$ nutrients (e.g., iron, sodium, calcium, etc.). For each food $i \in \{1, 2, \dots, s\}$, the value $w_i \in \mathbb{Q}_{> 0}$ represents the cost in euros per kilogram of that food. For each food $i \in \{1, 2, \dots, s\}$ and each nutrient $j \in \{1, 2, \dots, r\}$, the value $g_{ij} \in \mathbb{Q}_{\ge 0}$ denotes the grams of nutrient $j$ provided by one kilogram of food $i$. For each nutrient $j \in \{1, 2, \dots, r\}$, the diet must contain at least $a_j \in \mathbb{Q}_{\ge 0}$ grams and at most $b_j \in \mathbb{Q}_{> 0}$ grams of that nutrient per month. Additionally, for each food $i \in \{1, 2, \dots, s\}$, the diet must include at least $c_i \in \mathbb{Q}_{\ge 0}$ kilograms and at most $d_i \in \mathbb{Q}_{> 0}$ kilograms of that food per month. The school canteen aims to determine a minimum-cost  monthly diet subject to the constraints described above.

**Questions**

1. Write a  *Linear Programming* (LP) model for the problem.  Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints.   What algorithm can be used to find an optimal solution of the model?

2. Consider now an instance of the problem with $s = 4$ types of food and $r=3$ nutrients. These are the other input data:

    |  | $j=1$ | $j=2$ | $j=3$ |  | $i=1$ | $i=2$ | $i=3$ | $i=4$ |
    |---|---|---|---|---|---|---|---|---|
    | $a_j$ | 10 | 20 | 10 | $w_i$ | 5 | 8 | 2 | 2 |
    | $b_j$ | 40 | 60 | 50 | $c_i$ | 1 | 1 | 0 | 1 |
    |  |  |  |  | $d_i$ | 10 | 15 | 20 | 10 |

    | $g_{ij}$ | $j=1$ | $j=2$ | $j=3$ |
    |---|---|---|---|
    | $i=1$ | $2$ | $4$ | $2$ |
    | $i=2$ | $1$ | $1$ | $1$ |
    | $i=3$ | $4$ | $6$ | $4$ |
    | $i=4$ | $4$ | $6$ | $2$ |

    Write the LP model for this instance.

3. Find a feasible solution of the  LP model of the  instance and accordingly an upper bound on the optimal solution value of the LP model for the  instance.

4. Write the dual model of the LP model and the dual model for the  instance. Find a feasible solution of the dual model of the  instance and accordingly a lower bound on the optimal solution value of the LP model for the  instance.

## Worked solution

1. We introduce the following $s$ non-negative variables:

    \begin{align*}
    x_i &= \text{kilograms of food } i \text{ in the diet per month}, \quad \forall i \in \{1,2,\dots,s\}.
    \end{align*}

    Using these variables, an LP model for the problem reads as follows:

    !!! chiave ""

        <a id="eq-sm3-LP"></a>

        \begin{align*}
        \min  ~~ \sum_{i=1}^s w_i \, x_i & & \label{sm3-obj}  \tag{1a}\\[1ex]
        \text{subject to} \quad  \sum_{i=1}^s g_{ij} \; x_i& \ge a_j,       &  \forall   j \in \{1,2,\dots,r\}, \label{sm3-cons1}  \tag{1b}\\[1ex]
        \sum_{i=1}^s g_{ij} \; x_i& \le b_j,       &  \forall   j \in \{1,2,\dots,r\}, \label{sm3-cons2}  \tag{1c}\\[1ex]
        x_i& \ge c_i,       &  \forall   i \in \{1,2,\dots,s\}, \label{sm3-cons3}  \tag{1d}\\[1ex]
        x_i& \le d_i,       &  \forall   i \in \{1,2,\dots,s\}, \label{sm3-cons4}  \tag{1e}\\[1ex]
        x_i                    &\ge  0, & \forall i \in \{1,2,\dots,s\}. \label{sm3-cons5} \tag{1f}
        \end{align*}

    Description of the objective function and constraints of the LP model:

    - the linear objective function $\eqref{sm3-obj}$ minimizes the total cost of the diet;

    - the linear constraints $\eqref{sm3-cons1}$ ensure that the total amount of each nutrient provided by the selected foods is at least equal to its minimum requirement ($r$ linear constraints);

    - the linear constraints $\eqref{sm3-cons2}$ ensure that the total amount of each nutrient provided by the selected foods does not exceed its maximum requirement ($r$ linear constraints);

    - the linear constraints $\eqref{sm3-cons3}$ ensure that each type of food included in the diet meets its minimum quantity requirement ($s$ linear constraints);

    - the linear constraints $\eqref{sm3-cons4}$ ensure that each type of food included in the diet does not exceed its maximum quantity requirement ($s$ linear constraints);

    - the linear constraints $\eqref{sm3-cons5}$ define the variables of the LP model.

    The LP model can be solved to optimality, for example, by  the simplex algorithm.

2. The LP model [(1)](#eq-sm3-LP)  for the specific instance reads as follows:

    $$
    \begin{array}{rrcrcrcrcr}
    {\min} & {5\,x_{1}} & {+} & {8\,x_{2}} & {+} & {2\,x_{3}} & {+} & {2\,x_{4}} \\[1ex]
    \text{subject to} & {2\,x_{1}} & {+} & {x_{2}} & {+} & {4\,x_{3}} & {+} & {4\,x_{4}} & {\ge} & {10} \\[1ex]
    & {4\,x_{1}} & {+} & {x_{2}} & {+} & {6\,x_{3}} & {+} & {6\,x_{4}} & {\ge} & {20} \\[1ex]
    & {2\,x_{1}} & {+} & {x_{2}} & {+} & {4\,x_{3}} & {+} & {2\,x_{4}} & {\ge} & {10} \\[1ex]
    & {2\,x_{1}} & {+} & {x_{2}} & {+} & {4\,x_{3}} & {+} & {4\,x_{4}} & {\le} & {40} \\[1ex]
    & {4\,x_{1}} & {+} & {x_{2}} & {+} & {6\,x_{3}} & {+} & {6\,x_{4}} & {\le} & {60} \\[1ex]
    & {2\,x_{1}} & {+} & {x_{2}} & {+} & {4\,x_{3}} & {+} & {2\,x_{4}} & {\le} & {50} \\[1ex]
    & {x_{1}} &  &  &  &  &  &  & {\ge} & {1} \\[1ex]
    &  &  & {x_{2}} &  &  &  &  & {\ge} & {1} \\[1ex]
    &  &  &  &  & {x_{3}} &  &  & {\ge} & {0} \\[1ex]
    &  &  &  &  &  &  & {x_{4}} & {\ge} & {1} \\[1ex]
    & {x_{1}} &  &  &  &  &  &  & {\le} & {10} \\[1ex]
    &  &  & {x_{2}} &  &  &  &  & {\le} & {15} \\[1ex]
    &  &  &  &  & {x_{3}} &  &  & {\le} & {20} \\[1ex]
    &  &  &  &  &  &  & {x_{4}} & {\le} & {10} \\[1ex]
    & {x_{1},} &  & {x_{2},} &  & {x_{3},} &  & {x_{4}} & {\ge} & {0}
    \end{array}
    $$

3. For example, by setting:

    $$
    \bar{x}_{1}=5,~~\bar{x}_{2}=1,~~\bar{x}_{3}=0,~~\bar{x}_{4}=1
    $$

    we have a feasible solution.   The objective function value of this feasible  solution is:

    $$
    \sum_{i=1}^s w_i \,  \bar x_i  = 5 \cdot 5 + 8 \cdot 1 + 2 \cdot 0 + 2 \cdot 1  =  35
    $$

    accordingly 35 is an upper bound on the optimal solution value of the LP model [(1)](#eq-sm3-LP). So, for this instance, we have:

    $$
    z(~ LP~) ~\le~  35
    $$

4. By using

    - a non-negative variable $\alpha_j$ for each constraint $\eqref{sm3-cons1}$ ($j \in \{1,2,\dots,r\}$)

    - a  non-positive variable $\beta_j$ for each constraint $\eqref{sm3-cons2}$ ($j \in \{1,2,\dots,r\}$)

    - a non-negative variable $\gamma_i$ for each constraint $\eqref{sm3-cons3}$ ($i \in \{1,2,\dots,s\}$)

    - a  non-positive variable $\delta_i$ for each constraint $\eqref{sm3-cons4}$ ($i \in \{1,2,\dots,s\}$)

    the dual of the LP model [(1)](#eq-sm3-LP) reads as follows:

    !!! chiave ""

        <a id="eq-sm3-DUAL"></a>

        \begin{align*}
        \max ~~ \sum_{j=1}^r a_j \: \alpha_j + \sum_{j=1}^r b_j \: \beta_j & &  \\[1ex]
        + \sum_{i=1}^s c_i \: \gamma_i + \sum_{i=1}^s d_i \: \delta_i & &  \tag{2a}\\[1ex]
        \text{subject to}  \quad \sum_{j=1}^{r} g_{ij} \; \alpha_j + \sum_{j=1}^{r} g_{ij} \; \beta_j + \gamma_i + \delta_i   &\le w_i,       & \forall i \in \{1,2,\dots,s\},  \tag{2b}\\[1ex]
        \alpha_{j}       &\ge 0, & \forall j \in \{1,2,\dots,r\},  \tag{2c}\\[1ex]
        \beta_{j}       &\le 0, & \forall j \in \{1,2,\dots,r\},  \tag{2d}\\[1ex]
        \gamma_{i}       &\ge 0, & \forall i \in \{1,2,\dots,s\},  \tag{2e}\\[1ex]
        \delta_{i}       &\le 0, & \forall i \in \{1,2,\dots,s\}. \tag{2f}
        \end{align*}

    The dual model [(2)](#eq-sm3-DUAL) for the  instance reads as follows:

$$
\begin{array}{rcrcrcrcrcrcrcrcrcr}
{\max} &  & {10\,\alpha_{1}} & {+} & {20\,\alpha_{2}} & {+} & {10\,\alpha_{3}} & {+} & {40\,\beta_{1}} & {+} & {60\,\beta_{2}} & {+} & {50\,\beta_{3}} &  &  &  &  &  &  \\
& {+} & {\gamma_{1}} & {+} & {\gamma_{2}} &  &  & {+} & {\gamma_{4}} & {+} & {10\,\delta_{1}} & {+} & {15\,\delta_{2}} & {+} & {20\,\delta_{3}} & {+} & {10\,\delta_{4}} &  &  \\[1.5ex]
\text{subject to} &  & {2\,\alpha_{1}} & {+} & {4\,\alpha_{2}} & {+} & {2\,\alpha_{3}} & {+} & {2\,\beta_{1}} & {+} & {4\,\beta_{2}} & {+} & {2\,\beta_{3}} &  &  &  &  &  &  \\
& {+} & {\gamma_{1}} &  &  &  &  &  &  & {+} & {\delta_{1}} &  &  &  &  &  &  & {\le} & {5} \\[1.5ex]
&  & {\alpha_{1}} & {+} & {\alpha_{2}} & {+} & {\alpha_{3}} & {+} & {\beta_{1}} & {+} & {\beta_{2}} & {+} & {\beta_{3}} &  &  &  &  &  &  \\
&  &  & {+} & {\gamma_{2}} &  &  &  &  &  &  & {+} & {\delta_{2}} &  &  &  &  & {\le} & {8} \\[1.5ex]
&  & {4\,\alpha_{1}} & {+} & {6\,\alpha_{2}} & {+} & {4\,\alpha_{3}} & {+} & {4\,\beta_{1}} & {+} & {6\,\beta_{2}} & {+} & {4\,\beta_{3}} &  &  &  &  &  &  \\
&  &  &  &  & {+} & {\gamma_{3}} &  &  &  &  &  &  & {+} & {\delta_{3}} &  &  & {\le} & {2} \\[1.5ex]
&  & {4\,\alpha_{1}} & {+} & {6\,\alpha_{2}} & {+} & {2\,\alpha_{3}} & {+} & {4\,\beta_{1}} & {+} & {6\,\beta_{2}} & {+} & {2\,\beta_{3}} &  &  &  &  &  &  \\
&  &  &  &  &  &  & {+} & {\gamma_{4}} &  &  &  &  &  &  & {+} & {\delta_{4}} & {\le} & {2} \\[1.5ex]
&  & {\alpha_{1},} &  & {\alpha_{2},} &  & {\alpha_{3},} &  &  &  &  &  &  &  &  &  &  &  &  \\
&  & {\gamma_{1},} &  & {\gamma_{2},} &  & {\gamma_{3},} &  & {\gamma_{4}} &  &  &  &  &  &  &  &  & {\ge} & {0} \\[1.5ex]
&  &  &  &  &  &  &  & {\beta_{1},} &  & {\beta_{2},} &  & {\beta_{3},} &  &  &  &  &  &  \\
&  &  &  &  &  &  &  &  &  & {\delta_{1},} &  & {\delta_{2},} &  & {\delta_{3},} &  & {\delta_{4}} & {\le} & {0}
\end{array}
$$

- For example, by setting:

    $$
    \bar\alpha_1=\bar\alpha_2=\bar\alpha_3=\bar\beta_1=\bar\beta_2=\bar\beta_3=\bar\delta_1=\bar\delta_2=\bar\delta_3=\bar\delta_4=0
    $$

    and by setting:

    $$
    \bar \gamma_1=5,~~\bar \gamma_2=8,~~\bar \gamma_3=2,~~\bar \gamma_4=2
    $$

    we have a feasible dual solution.

    The objective function value of this feasible dual solution is:

    $$
    \sum_{j=1}^r a_j \: \bar \alpha_j + \sum_{j=1}^r b_j \: \bar \beta_j + \sum_{i=1}^s c_i \: \bar \gamma_i  + \sum_{i=1}^s d_i \: \bar \delta_i =
    $$

    $$
    =10 \cdot 0 + 20 \cdot 0 +10 \cdot 0 +
    40 \cdot 0 +60 \cdot 0 +50 \cdot 0 +
    1 \cdot 5 + 1 \cdot 8 +0 \cdot 2 + 1 \cdot 2 +
    10 \cdot 0 + 15 \cdot 0 +20 \cdot 0 +10 \cdot 0
    =  15
    $$

    Accordingly  $15$ is a lower bound on the optimal solution value of the model. So, for this instance, we have:

    $$
    15 ~\le~ z(~ LP~) ~\le~  35
    $$

<!-- laboratorio-interattivo: sezione aggiunta per l'app dei nove modelli -->

## Interactive lab { #interactive-lab }

The app solves this model in the browser, with the data of the example: the sliders change the data and the simplex method recomputes the optimal solution and the shadow prices. It also opens full page in the interactive lab: [Diet planning](lab/diet.md).

<div class="gi gi-capitolo" data-grafico="pl-dieta"></div>
