# Example 4.8 — Multi-period production with purchases and storage

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Model:** symbolic · **Techniques:** [4.5 Multi-period planning](techniques-05.md) · [All the worked models](techniques.md#worked-models)

## The problem

!!! abstract "Multi-period production with purchases and storage"

    A company needs to satisfy the forecast demand for a chemical product over a time horizon of $n \in \mathbb{Z}_{\ge 1}$ days. Each day $t \in \{1, 2, \dots, n\}$, the quantity $d_t \in \mathbb{Q}_{\ge  0}$ is the forecast demand in liters of the product. On each day $t \in \{1,2,\dots,n\}$, the company can produce up to $m_t \in \mathbb{Q}_{\ge 0}$ liters at a cost of $p_t \in \mathbb{Q}_{>0}$ euros per liter, buy from the market at a cost of $u_t \in \mathbb{Q}_{>0}$ euros per liter, and store product at the end of the day  in a warehouse at a holding cost of $h_t \in \mathbb{Q}_{>0}$ euros per liter. The initial stock in the warehouse is $\ell_0 \in \mathbb{Q}_{\ge 0}$ liters while a safety stock of $\ell_n \in \mathbb{Q}_{\ge 0}$ liters is required at the end of the time horizon. Storage and buying capacities are assumed to be unlimited. The company wants to determine a minimum-cost plan  to satisfy the demand subject to the constraints described above.

**Questions**

1. Write a  linear programming (LP) model for the problem.  Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints.   What algorithm can be used to find an optimal solution of the model?

2. Consider now an instance of the problem with $4$ days ($n=4$) and the following input data:

    |  | $t=1$ | $t=2$ | $t=3$ | $t=4$ |
    |---|---|---|---|---|
    | $d_t$ | 45 | 60 | 75 | 75 |
    | $p_t$ | 10 | 10 | 10 | 10 |
    | $u_t$ | 15 | 15 | 15 | 15 |
    | $h_t$ | 2 | 2 | 2 | 2 |
    | $m_t$ | 40 | 50 | 150 | 40 |

    Moreover $\ell_0 = 10$ and $\ell_n=5$. Write the LP model for this instance.

3. Find a feasible solution of the  LP model of the  instance and accordingly an upper bound on the optimal solution value of the LP model for the  instance.

4. Write the dual model of the LP model and the dual model for the  instance. Find a feasible solution of the dual model of the  instance and accordingly a lower bound on the optimal solution value of the LP model for the  instance.

## Worked solution

1. We introduce the following $2 \; n+ n-1$ non-negative variables:

    $$
    \begin{cases}
    x_t = \text{  liters produced on day } t \\[1ex]
    b_t = \text{  liters bought from the market on day } t
    \end{cases}
    \qquad \forall t \in \{1,2,\dots,n\}
    $$

    \begin{align*}
    s_t &= \text{  liters stored in the warehouse at the end of day } t, \qquad \forall t \in \{1,2,\dots,n-1\}.
    \end{align*}

    Using these variables, an LP model for the problem reads as follows:

    !!! chiave ""

        <a id="eq-sm5-LP"></a>

        \begin{align*}
        \underbrace{h_n \; \ell_n}_{\text{constant term}} + \min \quad \sum_{t=1}^n p_t \, x_t & &  \\[1ex]
        + \sum_{t=1}^n u_t \, b_t & &  \\[1ex]
        + \sum_{t=1}^{n-1} h_t \, s_t & & \label{sm5-obj}  \tag{1a}\\[1ex]
        \text{subject to} \quad x_1 + b_1 - s_1 &= d_1 - \ell_0, \label{sm5-cons1}  \tag{1b}\\[1ex]
        x_t + b_t + s_{t-1} - s_t &= d_t, & \forall t \in \{2,3,\dots,n-1\}, \label{sm5-cons2}  \tag{1c}\\[1ex]
        x_n + b_n + s_{n-1} &= d_n + \ell_n, \label{sm5-cons3}  \tag{1d}\\[1ex]
        x_t &\le m_t, & \forall t \in \{1,2,\dots,n\}, \label{sm5-cons4}  \tag{1e}\\[1ex]
        x_t &\ge 0, & \forall t \in \{1,2,\dots,n\}, \label{sm5-cons5}  \tag{1f}\\[1ex]
        b_t &\ge 0, & \forall t \in \{1,2,\dots,n\}, \label{sm5-cons6}  \tag{1g}\\[1ex]
        s_t &\ge 0, & \forall t \in \{1,2,\dots,n-1\}. \label{sm5-cons7} \tag{1h}
        \end{align*}

    Description of the objective function and constraints of the LP model:

    - the linear objective function $\eqref{sm5-obj}$ minimizes the total cost of the production, market purchases, and inventory holding over the planning horizon. The constant term $h_n \, \ell_n$ accounts for the holding cost of the final safety stock, and it is written outside the minimization since it does not depend on the decision variables.

    - the linear constraint $\eqref{sm5-cons1}$ ensures that the demand on the first day is satisfied using production, purchases, and the initial stock level, while accounting for the stock stored at the end of the first day (one linear constraint);

    - the linear constraints $\eqref{sm5-cons2}$ ensure that, on intermediate days, the demand is satisfied using daily production, purchases, and inventory carried over from the previous day ($n-2$ linear constraints);

    - the linear constraint $\eqref{sm5-cons3}$ ensures that the final day's demand is satisfied, and the required safety stock is left in storage at the end of the planning horizon (one linear constraint);

    - the linear constraint $\eqref{sm5-cons4}$ ensures that daily production does not exceed the available production capacity ($n$ linear constraints);

    - the linear constraints $\eqref{sm5-cons5}$, $\eqref{sm5-cons6}$, and $\eqref{sm5-cons7}$ define the variables of the LP model.

    The LP model can be solved to optimality, for example, by  the simplex algorithm.

2. The LP model [(1)](#eq-sm5-LP)  for the specific instance (without the constant term) reads as follows:

    $$
    \begin{array}{rcrcrcrcrcrcrcrcrcr}
    {\min} &  & {10\,x_{1}} & {+} & {10\,x_{2}} & {+} & {10\,x_{3}} & {+} & {10\,x_{4}} & {+} & {15\,b_{1}} & {+} & {15\,b_{2}} & {+} & {15\,b_{3}} & {+} & {15\,b_{4}} &  &  \\
    & {+} & {2\,s_{1}} & {+} & {2\,s_{2}} & {+} & {2\,s_{3}} &  &  &  &  &  &  &  &  &  &  &  &  \\[1.5ex]
    \text{subject to} &  & {x_{1}} &  &  &  &  &  &  & {+} & {b_{1}} &  &  &  &  &  &  &  &  \\
    & {-} & {s_{1}} &  &  &  &  &  &  &  &  &  &  &  &  &  &  & {=} & {35} \\[1.5ex]
    &  &  &  & {x_{2}} &  &  &  &  &  &  & {+} & {b_{2}} &  &  &  &  &  &  \\
    & {+} & {s_{1}} & {-} & {s_{2}} &  &  &  &  &  &  &  &  &  &  &  &  & {=} & {60} \\[1.5ex]
    &  &  &  &  &  & {x_{3}} &  &  &  &  &  &  & {+} & {b_{3}} &  &  &  &  \\
    &  &  & {+} & {s_{2}} & {-} & {s_{3}} &  &  &  &  &  &  &  &  &  &  & {=} & {75} \\[1.5ex]
    &  &  &  &  &  &  &  & {x_{4}} &  &  &  &  &  &  & {+} & {b_{4}} &  &  \\
    &  &  &  &  & {+} & {s_{3}} &  &  &  &  &  &  &  &  &  &  & {=} & {80} \\[1.5ex]
    &  & {x_{1}} &  &  &  &  &  &  &  &  &  &  &  &  &  &  & {\le} & {40} \\[1.5ex]
    &  &  &  & {x_{2}} &  &  &  &  &  &  &  &  &  &  &  &  & {\le} & {50} \\[1.5ex]
    &  &  &  &  &  & {x_{3}} &  &  &  &  &  &  &  &  &  &  & {\le} & {150} \\[1.5ex]
    &  &  &  &  &  &  &  & {x_{4}} &  &  &  &  &  &  &  &  & {\le} & {40} \\[1.5ex]
    &  & {x_{1},} &  & {x_{2},} &  & {x_{3},} &  & {x_{4},} &  & {b_{1},} &  & {b_{2},} &  & {b_{3},} &  & {b_{4},} &  &  \\
    &  & {s_{1},} &  & {s_{2},} &  & {s_{3}} &  &  &  &  &  &  &  &  &  &  & {\ge} & {0}
    \end{array}
    $$

3. For example, by setting:

    $$
    \bar{x}_{1}=35,~~\bar{x}_{2}=50,~~\bar{x}_{3}=75,~~\bar{x}_{4}=40,
    $$

    $$
    ~~\bar{b}_{1}=0,~~\bar{b}_{2}=10,~~\bar{b}_{3}=0,~~\bar{b}_{4}=40,
    $$

    $$
    ~~ \bar{s}_{1}=0,~~\bar{s}_{2}=0,~~\bar{s}_{3}=0
    $$

    we have a feasible solution.   The objective function value of this feasible  solution is:

    \begin{align*}
    \underbrace{h_n \; \ell_n}_{\text{constant term}}
    + \sum_{t=1}^n p_t \,  \bar x_t
    + \sum_{t=1}^n u_t \, \bar b_t
    + \sum_{t=1}^{n-1} h_t \, \bar s_t &=  2 \cdot 5 +\\
    &+ 10 \cdot 35 + 10 \cdot 50 + 10 \cdot 75 + 10 \cdot 40 +\\
    &+ 15 \cdot 0 + 15 \cdot 10 + 15 \cdot 0 + 15 \cdot 40 +\\
    & + 2 \cdot 0 + 2 \cdot 0 + 2 \cdot 0 \\
    & = 2760
    \end{align*}

    accordingly $2760$ is an upper bound on the optimal solution value of the LP model [(1)](#eq-sm5-LP). So, for this instance, we have:

    $$
    z(~ LP~) \le 2760
    $$

4. By using

    - a free dual variable $\mu_1$ for the constraint $\eqref{sm5-cons1}$

    - a free dual variable $\mu_t$ for each  constraint $\eqref{sm5-cons2}$  ($t \in \{2,3,\dots,n-1\}$)

    - a free dual variable $\mu_n$ for the constraint $\eqref{sm5-cons3}$

    - a non-positive dual variable $\pi_t$ for each constraint $\eqref{sm5-cons4}$ ($t \in \{1,2,\dots,n\}$)

    the dual of the LP model [(1)](#eq-sm5-LP) (without the constant term) reads as follows:

    !!! chiave ""

        <a id="eq-sm5-DUAL"></a>

        \begin{align*}
        \max \quad (d_1 - \ell_0) \, \mu_1 + \sum_{t=2}^{n-1} d_t \, \mu_t & &  \\[1ex]
        + (d_n + \ell_n) \, \mu_n + \sum_{t=1}^n m_t \, \pi_t & &  \tag{2a}\\[1ex]
        \text{subject to} \quad \mu_t + \pi_t &\le p_t, & \forall t \in \{1,2,\dots,n\},  \tag{2b}\\[1ex]
        \mu_t &\le u_t, & \forall t \in \{1,2,\dots,n\},  \tag{2c}\\[1ex]
        -\mu_t + \mu_{t+1} &\le h_t, & \forall t \in \{1,2,\dots,n-1\},  \tag{2d}\\[1ex]
        \mu_t &\gtreqless 0, & \forall t \in \{1,2,\dots,n\},  \tag{2e}\\[1ex]
        \pi_t &\le 0, & \forall t \in \{1,2,\dots,n\}. \tag{2f}
        \end{align*}

    The dual model [(2)](#eq-sm5-DUAL) for the  instance (without the constant term) reads as follows:

    $$
    \begin{array}{rrcrcrcrcrcrcrcrcr}
    {\max} & {35\,\mu_{1}} & {+} & {60\,\mu_{2}} & {+} & {75\,\mu_{3}} & {+} & {80\,\mu_{4}} & {+} & {40\,\pi_{1}} & {+} & {50\,\pi_{2}} & {+} & {150\,\pi_{3}} & {+} & {40\,\pi_{4}} \\[1ex]
    \text{subject to} & {\mu_{1}} &  &  &  &  &  &  & {+} & {\pi_{1}} &  &  &  &  &  &  & {\le} & {10} \\[1ex]
    &  &  & {\mu_{2}} &  &  &  &  &  &  & {+} & {\pi_{2}} &  &  &  &  & {\le} & {10} \\[1ex]
    &  &  &  &  & {\mu_{3}} &  &  &  &  &  &  & {+} & {\pi_{3}} &  &  & {\le} & {10} \\[1ex]
    &  &  &  &  &  &  & {\mu_{4}} &  &  &  &  &  &  & {+} & {\pi_{4}} & {\le} & {10} \\[1ex]
    & {\mu_{1}} &  &  &  &  &  &  &  &  &  &  &  &  &  &  & {\le} & {15} \\[1ex]
    &  &  & {\mu_{2}} &  &  &  &  &  &  &  &  &  &  &  &  & {\le} & {15} \\[1ex]
    &  &  &  &  & {\mu_{3}} &  &  &  &  &  &  &  &  &  &  & {\le} & {15} \\[1ex]
    &  &  &  &  &  &  & {\mu_{4}} &  &  &  &  &  &  &  &  & {\le} & {15} \\[1ex]
    & {-\mu_{1}} & {+} & {\mu_{2}} &  &  &  &  &  &  &  &  &  &  &  &  & {\le} & {2} \\[1ex]
    &  & {-} & {\mu_{2}} & {+} & {\mu_{3}} &  &  &  &  &  &  &  &  &  &  & {\le} & {2} \\[1ex]
    &  &  &  & {-} & {\mu_{3}} & {+} & {\mu_{4}} &  &  &  &  &  &  &  &  & {\le} & {2} \\[1ex]
    & {\mu_{1},} &  & {\mu_{2},} &  & {\mu_{3},} &  & {\mu_{4}} &  &  &  &  &  &  &  &  & {\gtreqless} & {0} \\[1ex]
    &  &  &  &  &  &  &  &  & {\pi_{1},} &  & {\pi_{2},} &  & {\pi_{3},} &  & {\pi_{4}} & {\le} & {0}
    \end{array}
    $$

    For example, by setting:

    $$
    \bar\pi_1=0,~~\bar\pi_2=0,~~\bar\pi_3=0,~~\bar\pi_4=0
    $$

    and by setting:

    $$
    \begin{gathered}
    \bar \mu_1=\min\{10,15\}=10,~~\bar \mu_2=\min\{10,15\}=10, \\[0.5ex]
    \bar \mu_3=\min\{10,15\}=10,~~\bar \mu_4=\min\{10,15\}=10
    \end{gathered}
    $$

    we have a feasible dual solution.

    The objective function value of this feasible dual solution is:

    \begin{align*}
    & \underbrace{h_n \; \ell_n}_{\text{constant term}} + (d_1 - \ell_0) \; \bar \mu_1 + \sum_{t=2}^{n-1} d_t \; \bar \mu_t + (d_n + \ell_n) \; \bar \mu_n + {} \\
    & + \sum_{t=1}^n m_t \; \bar \pi_t = 2 \cdot 5 + {} \\
    &+ 35 \cdot 10 + 60 \cdot 10 + 75 \cdot 10 + 80 \cdot 10 +\\
    & + 40 \cdot 0 + 50 \cdot 0 + 150 \cdot 0 + 40 \cdot 0  \\
    &=  2510
    \end{align*}

    Accordingly, $2510$ is a lower bound on the optimal solution value of the primal LP model. So, for this instance, we have:

    $$
    2510 \le z(~ LP~) \le 2760
    $$
