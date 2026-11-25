# Example 4.7 — Diet planning for several classes

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Model:** symbolic · **Techniques:** [4.3 Blending](techniques-03.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Diet planning for several classes"

    A school canteen needs to determine  $n \in \mathbb{Z}_{\ge 1}$ monthly diets for its classes of students. It is considering $s \in \mathbb{Z}_{\ge 1}$ possible types of food (e.g., milk, rice,  bread, etc.), each containing $r \in \mathbb{Z}_{\ge 1}$ nutrients (e.g., iron, sodium, etc.). For each food $i \in \{1, 2, \dots, s\}$, the value $w_i \in \mathbb{Q}_{> 0}$ represents the cost in euros per kilogram of that food. For each food $i \in \{1, 2, \dots, s\}$ and each nutrient $j \in \{1, 2, \dots, r\}$, the value $g_{ij} \in \mathbb{Q}_{\ge 0}$ denotes the grams of nutrient $j$ provided by one kilogram of food $i$. For each diet $k \in \{1,2,\dots,n\}$ and each nutrient $j \in \{1, 2, \dots, r\}$, the diet must contain at least $a_{kj} \in \mathbb{Q}_{\ge 0}$ grams and at most $b_{kj} \in \mathbb{Q}_{>0}$ grams of that nutrient per month. Additionally, for each food $i \in \{1, 2, \dots, s\}$,  the diets must include at least $c_i \in \mathbb{Q}_{\ge 0}$ kilograms and at most $d_i \in \mathbb{Q}_{> 0}$ kilograms of that food per month. The school canteen aims to determine a minimum-cost monthly diets for all classes of students subject to the constraints described above.

**Questions**

1. Write a  *Linear Programming* (LP) model for the problem.  Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints.   What algorithm can be used to find an optimal solution of the model?

2. Consider now an instance of the problem with $n=2$ diets, $s=3$ types of food and $r=2$ nutrients. These are the other input data:

    | $a_{kj}$ | $j=1$ | $j=2$ |  |
    |---|---|---|---|
    | $k=1$ | $20$ | $10$ |
    | $k=2$ | $10$ | $20$ |

    | $b_{kj}$ | $j=1$ | $j=2$ |
    |---|---|---|
    | $k=1$ | $40$ | $20$ |
    | $k=2$ | $20$ | $40$ |

    |  | $i=1$ | $i=2$ | $i=3$ |
    |---|---|---|---|
    | $w_i$ | 5 | 8 | 6 |
    | $c_i$ | 1 | 1 | 0 |
    | $d_i$ | 5 | 4 | 10 |

    | $g_{ij}$ | $j=1$ | $j=2$ |
    |---|---|---|
    | $i=1$ | $6$ | $2$ |
    | $i=2$ | $2$ | $1$ |
    | $i=3$ | $2$ | $6$ |

    Write the LP model for this instance.

3. Find a feasible solution of the  LP model of the  instance and accordingly an upper bound on the optimal solution value of the LP model for the  instance.

4. Write the dual model of the LP model and the dual model for the  instance. Find a feasible solution of the dual model of the  instance and accordingly a lower bound on the optimal solution value of the LP model for the  instance.

## Worked solution

1. We introduce the following $s \; n$ non-negative variables:

    $$
    \begin{gathered}
    x_{ik} = \text{kilograms of food } i \text{ in the diet } k \text{ per month}, \\[0.5ex]
    \forall i \in \{1,2,\dots,s\}, ~ \forall k \in \{1,2,\dots,n\}.
    \end{gathered}
    $$

    Using these variables, an LP model for the problem reads as follows:

    !!! chiave ""

        <a id="eq-sm4-LP"></a>

        \begin{align*}
        \min  ~~ \sum_{i=1}^s  \sum_{k=1}^n  w_i \, x_{ik} & & \label{sm4-obj}  \tag{1a}\\[1ex]
        \text{subject to} \quad  \sum_{i=1}^s g_{ij} \; x_{ik}& \ge a_{kj},       &  \forall   k \in \{1,2,\dots,n\},~\forall   j \in \{1,2,\dots,r\}, \label{sm4-cons1}  \tag{1b}\\[1ex]
        \sum_{i=1}^s g_{ij} \; x_{ik}& \le b_{kj},       &  \forall   k \in \{1,2,\dots,n\},~\forall   j \in \{1,2,\dots,r\}, \label{sm4-cons2}  \tag{1c}\\[1ex]
        \sum_{k=1}^n x_{ik}& \ge c_i,       &  \forall   i \in \{1,2,\dots,s\}, \label{sm4-cons3}  \tag{1d}\\[1ex]
        \sum_{k=1}^n x_{ik}& \le d_i,       &  \forall   i \in \{1,2,\dots,s\}, \label{sm4-cons4}  \tag{1e}\\[1ex]
        x_{ik}                    &\ge  0, & \forall i \in \{1,2,\dots,s\},~\forall k \in \{1,2,\dots,n\}. \label{sm4-cons5} \tag{1f}
        \end{align*}

    Description of the objective function and constraints of the LP model:

    - the linear objective function $\eqref{sm4-obj}$ minimizes the total cost of the diets for all classes of students.

    - the linear constraints $\eqref{sm4-cons1}$ ensure that, for every diet and every nutrient, the total amount of the nutrient provided by the foods included in that diet satisfies the minimum requirement ($n \; r$ linear constraints);

    - the linear constraints $\eqref{sm4-cons2}$ ensure that, for every diet and every nutrient, the total amount of the nutrient provided by the foods included in that diet does not exceed the maximum requirement ($n \; r$ linear constraints);

    - the linear constraints $\eqref{sm4-cons3}$ ensure that, for each food, the total quantity distributed across all diets satisfies the minimum requirement ($s$ linear constraints);

    - the linear constraints $\eqref{sm4-cons4}$ ensure that, for each food, the total quantity distributed across all diets does not exceed the maximum requirement ($s$ linear constraints);

    - the linear constraints $\eqref{sm4-cons5}$ define the variables of the LP model.

    The LP model can be solved to optimality, for example, by  the simplex algorithm.

2. The LP model [(1)](#eq-sm4-LP)  for the specific instance reads as follows:

    $$
    \begin{array}{rrcrcrcrcrcrcr}
    {\min} & {5\,x_{11}} & {+} & {5\,x_{12}} & {+} & {8\,x_{21}} & {+} & {8\,x_{22}} & {+} & {6\,x_{31}} & {+} & {6\,x_{32}} \\[1ex]
    \text{subject to} & {6\,x_{11}} &  &  & {+} & {2\,x_{21}} &  &  & {+} & {2\,x_{31}} &  &  & {\ge} & {20} \\[1ex]
    & {2\,x_{11}} &  &  & {+} & {x_{21}} &  &  & {+} & {6\,x_{31}} &  &  & {\ge} & {10} \\[1ex]
    &  &  & {6\,x_{12}} &  &  & {+} & {2\,x_{22}} &  &  & {+} & {2\,x_{32}} & {\ge} & {10} \\[1ex]
    &  &  & {2\,x_{12}} &  &  & {+} & {x_{22}} &  &  & {+} & {6\,x_{32}} & {\ge} & {20} \\[1ex]
    & {6\,x_{11}} &  &  & {+} & {2\,x_{21}} &  &  & {+} & {2\,x_{31}} &  &  & {\le} & {40} \\[1ex]
    & {2\,x_{11}} &  &  & {+} & {x_{21}} &  &  & {+} & {6\,x_{31}} &  &  & {\le} & {20} \\[1ex]
    &  &  & {6\,x_{12}} &  &  & {+} & {2\,x_{22}} &  &  & {+} & {2\,x_{32}} & {\le} & {20} \\[1ex]
    &  &  & {2\,x_{12}} &  &  & {+} & {x_{22}} &  &  & {+} & {6\,x_{32}} & {\le} & {40} \\[1ex]
    & {x_{11}} & {+} & {x_{12}} &  &  &  &  &  &  &  &  & {\ge} & {1} \\[1ex]
    &  &  &  &  & {x_{21}} & {+} & {x_{22}} &  &  &  &  & {\ge} & {1} \\[1ex]
    &  &  &  &  &  &  &  &  & {x_{31}} & {+} & {x_{32}} & {\ge} & {0} \\[1ex]
    & {x_{11}} & {+} & {x_{12}} &  &  &  &  &  &  &  &  & {\le} & {5} \\[1ex]
    &  &  &  &  & {x_{21}} & {+} & {x_{22}} &  &  &  &  & {\le} & {4} \\[1ex]
    &  &  &  &  &  &  &  &  & {x_{31}} & {+} & {x_{32}} & {\le} & {10} \\[1ex]
    & {x_{11},} &  & {x_{12},} &  & {x_{21},} &  & {x_{22},} &  & {x_{31},} &  & {x_{32}} & {\ge} & {0}
    \end{array}
    $$

3. For example, by setting:

    $$
    \bar{x}_{11}=4,~~\bar{x}_{12}=1,~~\bar{x}_{21}=2,~~\bar{x}_{22}=1,~~\bar{x}_{31}=0,~~\bar{x}_{32}=3
    $$

    we have a feasible solution.   The objective function value of this feasible  solution is:

    $$
    \sum_{i=1}^s w_i \sum_{k=1}^n  \, \bar x_{ik}  = 5 \cdot 4 +  5 \cdot 1 + 8 \cdot 2 + 8 \cdot 1 + 6 \cdot 0 + 6 \cdot 3  =  67
    $$

    accordingly 67 is an upper bound on the optimal solution value of the LP model [(1)](#eq-sm4-LP). So, for this instance, we have:

    $$
    z(~ LP~) ~\le~  67
    $$

4. By using

    - a non-negative variable $\alpha_{kj}$ for each constraint $\eqref{sm4-cons1}$ ($k \in \{1,2,\dots,n\},j \in \{1,2,\dots,r\}$)

    - a  non-positive variable $\beta_{kj}$ for each constraint $\eqref{sm4-cons2}$ ($k \in \{1,2,\dots,n\},j \in \{1,2,\dots,r\}$)

    - a non-negative variable $\gamma_i$ for each constraint $\eqref{sm4-cons3}$ ($i \in \{1,2,\dots,s\}$)

    - a non-positive variable $\delta_i$ for each constraint $\eqref{sm4-cons4}$ ($i \in \{1,2,\dots,s\}$)

    the dual of the LP model [(1)](#eq-sm4-LP) reads as follows:

!!! chiave ""

    <a id="eq-sm4-DUAL"></a>

    \begin{align*}
    \max ~~ \sum_{k=1}^n \sum_{j=1}^r a_{kj} \, \alpha_{kj} & &  \\[1ex]
    + \sum_{k=1}^n \sum_{j=1}^r b_{kj} \, \beta_{kj} & &  \\[1ex]
    + \sum_{i=1}^s c_i \, \gamma_i + \sum_{i=1}^s d_i \, \delta_i & &  \tag{2a}\\[1ex]
    \text{subject to} \quad \sum_{j=1}^{r} g_{ij} \, \alpha_{kj} & &  \\[1ex]
    + \sum_{j=1}^{r} g_{ij} \, \beta_{kj} + \gamma_i + \delta_i &\le w_i, & \forall i \in \{1,2,\dots,s\},~\forall k \in \{1,2,\dots,n\},  \tag{2b}\\[1ex]
    \alpha_{kj}       &\ge 0, & \forall k \in \{1,2,\dots,n\},~\forall j \in \{1,2,\dots,r\},  \tag{2c}\\[1ex]
    \beta_{kj}       &\le 0, & \forall k \in \{1,2,\dots,n\},~\forall j \in \{1,2,\dots,r\},  \tag{2d}\\[1ex]
    \gamma_{i}       &\ge 0, & \forall i \in \{1,2,\dots,s\},  \tag{2e}\\[1ex]
    \delta_{i}       &\le 0, & \forall i \in \{1,2,\dots,s\}. \tag{2f}
    \end{align*}

- The dual model [(2)](#eq-sm4-DUAL) for the  instance reads as follows:

$$
\begin{array}{rcrcrcrcrcrcrcrcrcr}
{\max} &  & {20\,\alpha_{11}} & {+} & {10\,\alpha_{12}} & {+} & {10\,\alpha_{21}} & {+} & {20\,\alpha_{22}} & {+} & {40\,\beta_{11}} & {+} & {20\,\beta_{12}} & {+} & {20\,\beta_{21}} & {+} & {40\,\beta_{22}} &  &  \\
& {+} & {\gamma_{1}} & {+} & {\gamma_{2}} &  &  & {+} & {5\,\delta_{1}} & {+} & {4\,\delta_{2}} & {+} & {10\,\delta_{3}} &  &  &  &  &  &  \\[1.5ex]
\text{subject to} &  & {6\,\alpha_{11}} & {+} & {2\,\alpha_{12}} &  &  &  &  & {+} & {6\,\beta_{11}} & {+} & {2\,\beta_{12}} &  &  &  &  &  &  \\
& {+} & {\gamma_{1}} &  &  &  &  & {+} & {\delta_{1}} &  &  &  &  &  &  &  &  & {\le} & {5} \\[1.5ex]
&  &  &  &  &  & {6\,\alpha_{21}} & {+} & {2\,\alpha_{22}} &  &  &  &  & {+} & {6\,\beta_{21}} & {+} & {2\,\beta_{22}} &  &  \\
& {+} & {\gamma_{1}} &  &  &  &  & {+} & {\delta_{1}} &  &  &  &  &  &  &  &  & {\le} & {5} \\[1.5ex]
&  & {2\,\alpha_{11}} & {+} & {\alpha_{12}} &  &  &  &  & {+} & {2\,\beta_{11}} & {+} & {\beta_{12}} &  &  &  &  &  &  \\
&  &  & {+} & {\gamma_{2}} &  &  &  &  & {+} & {\delta_{2}} &  &  &  &  &  &  & {\le} & {8} \\[1.5ex]
&  &  &  &  &  & {2\,\alpha_{21}} & {+} & {\alpha_{22}} &  &  &  &  & {+} & {2\,\beta_{21}} & {+} & {\beta_{22}} &  &  \\
&  &  & {+} & {\gamma_{2}} &  &  &  &  & {+} & {\delta_{2}} &  &  &  &  &  &  & {\le} & {8} \\[1.5ex]
&  & {2\,\alpha_{11}} & {+} & {6\,\alpha_{12}} &  &  &  &  & {+} & {2\,\beta_{11}} & {+} & {6\,\beta_{12}} &  &  &  &  &  &  \\
&  &  &  &  & {+} & {\gamma_{3}} &  &  &  &  & {+} & {\delta_{3}} &  &  &  &  & {\le} & {6} \\[1.5ex]
&  &  &  &  &  & {2\,\alpha_{21}} & {+} & {6\,\alpha_{22}} &  &  &  &  & {+} & {2\,\beta_{21}} & {+} & {6\,\beta_{22}} &  &  \\
&  &  &  &  & {+} & {\gamma_{3}} &  &  &  &  & {+} & {\delta_{3}} &  &  &  &  & {\le} & {6} \\[1.5ex]
&  & {\alpha_{11},} &  & {\alpha_{12},} &  & {\alpha_{21},} &  & {\alpha_{22},} &  &  &  &  &  &  &  &  &  &  \\
&  & {\gamma_{1},} &  & {\gamma_{2},} &  & {\gamma_{3}} &  &  &  &  &  &  &  &  &  &  & {\ge} & {0} \\[1.5ex]
&  &  &  &  &  &  &  &  &  & {\beta_{11},} &  & {\beta_{12},} &  & {\beta_{21},} &  & {\beta_{22},} &  &  \\
&  &  &  &  &  &  &  & {\delta_{1},} &  & {\delta_{2},} &  & {\delta_{3}} &  &  &  &  & {\le} & {0}
\end{array}
$$

- For example, by setting:

    $$
    \bar\alpha_{11}=\bar\alpha_{12}=\bar\alpha_{21}=\bar\alpha_{22}=
    \bar\beta_{11}=\bar\beta_{12}=\bar\beta_{21}=\bar\beta_{22}=\bar\delta_{1}=\bar\delta_{2}=\bar\delta_{3}=0
    $$

    and by setting:

    $$
    \bar \gamma_1=\min\{5,5\}=5,~~\bar \gamma_2=\min\{8,8\}=8,~~\bar \gamma_3=\min\{6,6\}=6
    $$

    we have a feasible dual solution.

    The objective function value of this feasible dual solution is:

    $$
    \sum_{k=1}^n \sum_{j=1}^r a_{kj} \; \bar \alpha_{kj} + \sum_{k=1}^n \sum_{j=1}^r b_{kj} \;\bar \beta_{kj} +\sum_{i=1}^s c_i \: \bar \gamma_i +\sum_{i=1}^s d_ i\: \bar \delta_i =
    $$

    $$
    =
    20 \cdot 0 + 10 \cdot 0 + 10 \cdot 0 + 20 \cdot 0
    + 40 \cdot 0 + 20 \cdot 0 + 20 \cdot 0 + 40 \cdot 0
    + 1 \cdot 5 + 1 \cdot 8 + 0 \cdot 6 + 5 \cdot 0
    + 4 \cdot 0 + 10 \cdot 0=  13
    $$

    Accordingly  $13$ is a lower bound on the optimal solution value of the model. So, for this instance, we have:

    $$
    13 ~\le~ z(~ LP~) ~\le~  67
    $$

<!-- laboratorio-interattivo: sezione aggiunta per l'app dei nove modelli -->

## Interactive lab { #interactive-lab }

The app solves this model in the browser, with the data of the example: the sliders change the main data and the simplex method recomputes the optimal solution, the optimal value and the shadow prices. It also opens full page in the [interactive lab](lab/techniques.md), with the other eight worked models.

<div class="gi gi-capitolo" data-grafico="pl-tecniche" data-funzione="dieta-classi"></div>
