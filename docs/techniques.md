# 4. Modelling techniques

[:material-file-pdf-box: Lecture notes (PDF)](pdf/lp-modelling-notes.pdf) · [:material-presentation: Chapter slides (PDF)](pdf/slides-04-techniques.pdf)

**Class:** LP · modelling techniques · **Examples:** three solved instances and nine worked models in the notes

!!! nota "Prerequisites"

    - From the *Linear Programming* module, [Chapter 4 «Linear Programming problems»](https://fabiofurini.github.io/linear-programming/lp-problems/04-lp-problems/): the graphical method, used to check small models.

    - From the *Linear Programming* module, [Chapter 5 «Possible outcomes and equivalent formulations»](https://fabiofurini.github.io/linear-programming/lp-problems/05-outcomes-equivalences/): generic LP problems and their equivalent reformulations, with free variables.

!!! chiave "Objectives"

    At the end of this chapter you will be able to:

    - write an LP model from a description: decision variables with their units, objective function, constraints;

    - model production planning, blending, transportation and multi-period planning problems;

    - linearize min-max objectives, absolute values and ratio constraints;

    - recognize the requirements that need integer variables.

How to go from the description of a problem to a Linear Programming model: the three-step
method, four standard patterns, three linearizations and the requirements that Linear
Programming cannot express. The cases of the following chapters use these techniques on
real data.

!!! note "How to read each technique"
    The standard patterns (4.2–4.5) have the problem in words with the symbolic input
    data, the variables with their count, the model with the reading of its constraints and
    a numerical example. The linearizations (4.6–4.8) have the non-linear form, the linear
    constraints that replace it, the reason why, and the conditions under which they hold.

<div class="grid cards" markdown>

-   **4.1 From the description to the model**

    ---

    Variables, objective, constraints: three steps in this order, the symbolic input data
    and the three most frequent mistakes.

    [:octicons-arrow-right-24: the method](techniques-01.md)

-   **4.2 Production planning**

    ---

    Maximum profit with limited resources: an LP in canonical maximization form.

    [:octicons-arrow-right-24: production](techniques-02.md)

-   **4.3 Blending**

    ---

    A minimum cost blend with minimum quantities of the components and fractions of the
    blend written as linear constraints.

    [:octicons-arrow-right-24: blending](techniques-03.md)

-   **4.4 Transportation**

    ---

    The minimum cost plan from the warehouses to the clients, feasible if and only if
    $\sum_i a_i \ge \sum_j d_j$.

    [:octicons-arrow-right-24: transportation](techniques-04.md)

-   **4.5 Multi-period planning**

    ---

    Production and storage linked by the inventory balance $y_{t-1} + x_t - y_t = d_t$.

    [:octicons-arrow-right-24: multi-period](techniques-05.md)

-   **4.6 Min-max and max-min**

    ---

    $\min w$ with $w \ge \sum_j a_{ij} x_j$: one more free variable, and only in the right
    direction.

    [:octicons-arrow-right-24: min-max](techniques-06.md)

-   **4.7 Absolute values**

    ---

    $w_i \ge \pm \sum_j a_{ij} x_j$, or $w_i^{+} - w_i^{-}$, under the right sign
    condition.

    [:octicons-arrow-right-24: absolute values](techniques-07.md)

-   **4.8 Ratios and percentages**

    ---

    Multiply by the denominator, if it is known to be positive.

    [:octicons-arrow-right-24: ratios](techniques-08.md)

-   **4.9 What cannot be modelled**

    ---

    Indivisible quantities, yes/no decisions, fixed costs, either-or constraints, minimum
    positive quantities: they need integer variables.

    [:octicons-arrow-right-24: the limits](techniques-09.md)

</div>

## The map of the techniques

Read it from the first column («what I want to write») to the second one («the constraints
that say it»).

| Technique | Formulation |
|---|---|
| [4.2 production](techniques-02.md) | $\max \sum_j c_j x_j$ with $\sum_j a_{ij} x_j \le b_i$ |
| [4.3 blending](techniques-03.md) | $\sum_j x_j = d$ and $\sum_j p_{kj} x_j \ge q_k$ |
| [4.4 transportation](techniques-04.md) | $\sum_j x_{ij} \le a_i$ and $\sum_i x_{ij} \ge d_j$ |
| [4.5 multi-period](techniques-05.md) | $y_{t-1} + x_t - y_t = d_t$ |
| [4.6 min-max](techniques-06.md) | $\min w$ with $w \ge \sum_j a_{ij} x_j$ |
| [4.7 absolute value](techniques-07.md) | $w_i \ge \pm \sum_j a_{ij} x_j$, or $w_i^{+} - w_i^{-}$ |
| [4.8 ratio](techniques-08.md) | $\sum_j (a_j - \gamma\, e_j)\, x_j \le 0$ |

## Worked models in the notes

The [lecture notes](pdf/lp-modelling-notes.pdf) close the chapter with nine worked models,
each one with its statement and its complete solution:

- **symbolic models**: production with regular time and overtime; transportation from
  warehouses to clients; diet planning, also for several classes; multi-period production
  with purchases and storage;
- **numerical models**: choice of desserts; production and storage of fruit cakes; blending
  of crude oil in a refinery; production of three drugs.

## In summary

!!! chiave "In summary"

    - An LP model is built in three steps: decision variables (with units and domains), objective function, constraints.

    - The most frequent mistakes are missing non-negativity constraints, dimensionally inconsistent constraints, and variables used in the objective function without being defined.

    - Production, blending, transportation and multi-period planning follow standard patterns, with balance constraints linking the periods.

    - Min-max objectives, absolute values and ratios become linear with an auxiliary variable or by multiplying by a positive denominator; indivisible quantities and logical conditions need integer variables.

## Exercises

1. **Production planning (1)**

    A company produces $r \in \mathbb{Z}_{\ge 1}$ different products using $s \in \mathbb{Z}_{\ge 1}$ resources (for example machine hours and labour hours). For each product $j \in \{1, 2, \dots, r\}$, the value $c_j \in \mathbb{Q}_{>0}$ is the profit in euros of one unit of product and the value $u_j \in \mathbb{Q}_{>0}$ is the maximum number of units that the market can absorb per week. For each resource $i \in \{1, 2, \dots, s\}$ and each product $j \in \{1, 2, \dots, r\}$, the value $a_{ij} \in \mathbb{Q}_{\ge 0}$ is the quantity of resource $i$ consumed by one unit of product $j$. For each resource $i \in \{1, 2, \dots, s\}$, the value $b_i \in \mathbb{Q}_{>0}$ is the quantity available per week; moreover, the company can buy at most $e_i \in \mathbb{Q}_{\ge 0}$ additional units of the resource per week, at a cost of $g_i \in \mathbb{Q}_{>0}$ euros per unit. The company aims to determine a maximum profit weekly production plan subject to the constraints described above.

    **Questions**

    1. Write a Linear Programming (LP) model for the problem. Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints. What algorithm can be used to find an optimal solution of the model?

    2. Consider now an instance of the problem in which there are $r=3$ products and $s=2$ resources. These are the other input data:

        |  | $j=1$ | $j=2$ | $j=3$ |
        |---|---|---|---|
        | $c_j$ | 12 | 18 | 10 |
        | $u_j$ | 20 | 15 | 20 |
        | $a_{1j}$ | 2 | 3 | 1 |
        | $a_{2j}$ | 1 | 2 | 2 |

        |  | $i=1$ | $i=2$ |
        |---|---|---|
        | $b_i$ | 50 | 50 |
        | $e_i$ | 20 | 10 |
        | $g_i$ | 3 | 2 |

        Write the LP model for this instance.

    3. Find a feasible solution of the LP model of the instance and accordingly a lower bound on the optimal solution value of the LP model for the instance.

    4. Write the dual model of the LP model and the dual model for the instance. Find a feasible solution of the dual model of the instance and accordingly an upper bound on the optimal solution value of the LP model for the instance.

    5. Consider the following solution of the LP model of the instance:

        $$
        \tilde x_1 = 20,~~\tilde x_2 = 5,~~\tilde x_3 = 15,~~\tilde y_1 = 20,~~\tilde y_2 = 10,
        $$

        where $y_i$ is the quantity of resource $i$ bought. Prove that it is an optimal solution by finding, with the complementary slackness conditions, a feasible dual solution with the same objective function value. What is the optimal solution value?

2. **Production planning (2)**

    A bicycle workshop assembles city bikes and mountain bikes, which are sold at 200 euros and 400 euros, respectively. Each bike needs one frame of its type. The workshop can weld the frames in house: a city bike frame requires 2 hours of welding and 20 euros of material, while a mountain bike frame requires 3 hours of welding and 40 euros of material; 150 welding hours are available per week. Alternatively, the frames can be bought from a supplier, at 60 euros (city bike frame) and 100 euros (mountain bike frame). The assembly of a city bike requires 1 hour of work and the assembly of a mountain bike requires 2 hours of work; 120 assembly hours are available per week. The market can absorb at most 30 mountain bikes per week. The goal of the workshop is to determine a weekly production plan that maximizes the total profit, that is, the revenue of the bikes minus the cost of the frames.

    **Questions**

    1. Write a Linear Programming (LP) model for the problem. Identify the decisions that must be made and define the corresponding decision variables. Describe the objective function of the model and its constraints. What algorithm can be used to find an optimal solution to the model?

    2. Find a feasible solution of the LP model and accordingly a lower bound on its optimal solution value.

    3. Write the dual model of the LP model. Find a feasible solution of the dual model and accordingly an upper bound on the optimal solution value of the LP model.

    4. Prove that the plan in which the workshop welds 30 city bike frames and 30 mountain bike frames, and buys 30 city bike frames, is optimal, by finding with the complementary slackness conditions a feasible dual solution with the same objective function value. What is the optimal solution value?

3. **Blending (1)**

    A foundry has to produce $d \in \mathbb{Q}_{>0}$ tonnes of an alloy by melting together $r \in \mathbb{Z}_{\ge 1}$ raw materials (ores and metal scraps). For each raw material $j \in \{1, 2, \dots, r\}$, the value $c_j \in \mathbb{Q}_{>0}$ is the cost in thousands of euros of one tonne and the value $a_j \in \mathbb{Q}_{>0}$ is the number of tonnes available. The quality of the alloy depends on $s \in \mathbb{Z}_{\ge 1}$ chemical elements. For each element $k \in \{1, 2, \dots, s\}$ and each raw material $j \in \{1, 2, \dots, r\}$, the value $p_{kj} \in \mathbb{Q}_{\ge 0}$ is the percentage of element $k$ contained in raw material $j$. The percentage of each element $k \in \{1, 2, \dots, s\}$ in the alloy has to be at least $\ell_k \in \mathbb{Q}_{\ge 0}$ and at most $u_k \in \mathbb{Q}_{>0}$, with $\ell_k \le u_k$. The foundry aims to determine a minimum cost blend subject to the constraints described above.

    **Questions**

    1. Write a Linear Programming (LP) model for the problem. Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints. What algorithm can be used to find an optimal solution of the model?

    2. Consider now an instance of the problem in which the foundry has to produce $d = 100$ tonnes of alloy from $r=3$ raw materials, and the quality depends on $s=2$ elements. These are the other input data:

        |  | $j=1$ | $j=2$ | $j=3$ |
        |---|---|---|---|
        | $c_j$ | 5 | 2 | 4 |
        | $a_j$ | 40 | 60 | 50 |
        | $p_{1j}$ | 4 | 1 | 2 |
        | $p_{2j}$ | 1 | 3 | 2 |

        |  | $k=1$ | $k=2$ |
        |---|---|---|
        | $\ell_k$ | 2 | 2 |
        | $u_k$ | 3 | 3 |

        Write the LP model for this instance.

    3. Find a feasible solution of the LP model of the instance and accordingly an upper bound on the optimal solution value of the LP model for the instance.

    4. Write the dual model of the LP model and the dual model for the instance. Find a feasible solution of the dual model of the instance and accordingly a lower bound on the optimal solution value of the LP model for the instance.

    5. Prove that the blend with $\tilde x_1 = 30$, $\tilde x_2 = 60$ and $\tilde x_3 = 10$ tonnes of the three raw materials is optimal, by finding with the complementary slackness conditions a feasible dual solution with the same objective function value. What is the optimal solution value?

4. **Transportation (1)**

    A company produces a liquid detergent in $s \in \mathbb{Z}_{\ge 1}$ plants and delivers it to $r \in \mathbb{Z}_{\ge 1}$ clients. The product cannot be shipped directly from a plant to a client: it has to pass through one of $q \in \mathbb{Z}_{\ge 1}$ depots. For each plant $i \in \{1, 2, \dots, s\}$, the value $a_i \in \mathbb{Q}_{>0}$ is the quantity in thousands of liters that the plant can produce per week. For each depot $k \in \{1, 2, \dots, q\}$, the value $h_k \in \mathbb{Q}_{>0}$ is the maximum quantity in thousands of liters that the depot can handle per week. For each client $j \in \{1, 2, \dots, r\}$, the value $d_j \in \mathbb{Q}_{>0}$ is the weekly demand in thousands of liters. For each plant $i \in \{1, 2, \dots, s\}$ and each depot $k \in \{1, 2, \dots, q\}$, the value $c_{ik} \in \mathbb{Q}_{\ge 0}$ is the cost in euros of transporting one thousand liters from plant $i$ to depot $k$; for each depot $k \in \{1, 2, \dots, q\}$ and each client $j \in \{1, 2, \dots, r\}$, the value $g_{kj} \in \mathbb{Q}_{\ge 0}$ is the cost in euros of transporting one thousand liters from depot $k$ to client $j$. The depots do not keep any stock. The company aims to determine a weekly minimum-cost transportation plan subject to the constraints described above.

    **Questions**

    1. Write a Linear Programming (LP) model for the problem. Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints. What algorithm can be used to find an optimal solution of the model?

    2. Consider now an instance of the problem with $s=2$ plants, $q=2$ depots and $r=2$ clients. These are the other input data:

        | $c_{ik}$ | $k=1$ | $k=2$ |
        |---|---|---|
        | $i=1$ | 2 | 4 |
        | $i=2$ | 3 | 1 |

        | $g_{kj}$ | $j=1$ | $j=2$ |
        |---|---|---|
        | $k=1$ | 3 | 5 |
        | $k=2$ | 4 | 2 |

        |  | $1$ | $2$ |
        |---|---|---|
        | $a_i$ | 50 | 40 |
        | $h_k$ | 50 | 40 |
        | $d_j$ | 30 | 50 |

        Write the LP model for this instance.

    3. Find a feasible solution of the LP model of the instance and accordingly an upper bound on the optimal solution value of the LP model for the instance.

    4. Write the dual model of the LP model and the dual model for the instance. Find a feasible solution of the dual model of the instance and accordingly a lower bound on the optimal solution value of the LP model for the instance.

    5. Consider the following transportation plan: plant 1 sends 40 thousand liters to depot 1 and plant 2 sends 40 thousand liters to depot 2; depot 1 sends 30 thousand liters to client 1 and 10 thousand liters to client 2, and depot 2 sends 40 thousand liters to client 2. Prove that it is optimal by finding, with the complementary slackness conditions, a feasible dual solution with the same objective function value. What is the optimal solution value?

5. **Multi-period planning (1)**

    A company plans the production of a fertilizer over a time horizon of $n \in \mathbb{Z}_{\ge 2}$ weeks. For each week $t \in \{1, 2, \dots, n\}$, the value $d_t \in \mathbb{Q}_{\ge 0}$ is the demand in tonnes, the value $p_t \in \mathbb{Q}_{>0}$ is the maximum quantity in tonnes that can be produced, and the value $c_t \in \mathbb{Q}_{>0}$ is the production cost in euros of one tonne. The product left at the end of a week can be stored and sold in the following weeks: for each week $t \in \{1, 2, \dots, n-1\}$, storing one tonne from week $t$ to week $t+1$ costs $h_t \in \mathbb{Q}_{>0}$ euros. Moreover, the demand of a week can be satisfied late (*backlogging*): for each week $t \in \{1, 2, \dots, n-1\}$, each tonne of demand not yet satisfied at the end of week $t$ costs a penalty of $g_t \in \mathbb{Q}_{>0}$ euros. There is no stock at the beginning of the horizon, and all the demand has to be satisfied by the end of week $n$. The company aims to determine a minimum-cost production plan subject to the constraints described above.

    **Questions**

    1. Write a Linear Programming (LP) model for the problem. Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints. What algorithm can be used to find an optimal solution of the model?

    2. Consider now an instance of the problem with $n = 3$ weeks and the following input data:

        |  | $t=1$ | $t=2$ | $t=3$ |
        |---|---|---|---|
        | $d_t$ | 30 | 50 | 20 |
        | $p_t$ | 40 | 30 | 40 |
        | $c_t$ | 10 | 12 | 11 |
        | $h_t$ | 2 | 2 | – |
        | $g_t$ | 3 | 3 | – |

        Write the LP model for this instance.

    3. Find a feasible solution of the LP model of the instance and accordingly an upper bound on the optimal solution value of the LP model for the instance.

    4. Write the dual model of the LP model and the dual model for the instance. Find a feasible solution of the dual model of the instance and accordingly a lower bound on the optimal solution value of the LP model for the instance.

    5. Consider the plan that produces $40$, $30$ and $30$ tonnes in the three weeks, stores $10$ tonnes at the end of week $1$ and satisfies $10$ tonnes of the demand of week $2$ in week $3$. Prove that it is optimal by finding, with the complementary slackness conditions, a feasible dual solution with the same objective function value. What is the optimal solution value?

6. **Min-max objective (1)**

    A printing company has to print $r \in \mathbb{Z}_{\ge 1}$ jobs (for example, the copies of a book or of a catalogue) on $s \in \mathbb{Z}_{\ge 1}$ printing machines, which start working at the same time. Each job can be split among several machines: each machine prints a fraction of the copies of the job. For each machine $i \in \{1, 2, \dots, s\}$ and each job $j \in \{1, 2, \dots, r\}$, the value $t_{ij} \in \mathbb{Q}_{>0}$ is the number of hours that machine $i$ would need to print the whole job $j$ alone; printing a fraction of the job takes the same fraction of this time. The company aims to split the jobs among the machines so as to minimize the time at which the last machine finishes its work (the *makespan*).

    **Questions**

    1. Write a Linear Programming (LP) model for the problem. Identify the decisions that must be taken and the corresponding decision variables. Identify and comment the objective function of the model and the constraints. What algorithm can be used to find an optimal solution of the model?

    2. Consider now an instance of the problem with $s=2$ machines and $r=3$ jobs, and the following processing times:

        | $t_{ij}$ | $j=1$ | $j=2$ | $j=3$ |
        |---|---|---|---|
        | $i=1$ | 2 | 4 | 4 |
        | $i=2$ | 4 | 12 | 12 |

        Write the LP model for this instance.

    3. Find a feasible solution of the LP model of the instance and accordingly an upper bound on the optimal solution value of the LP model for the instance.

    4. Write the dual model of the LP model and the dual model for the instance. Find a feasible solution of the dual model of the instance and accordingly a lower bound on the optimal solution value of the LP model for the instance.

    5. Consider the solution in which machine $1$ prints $\frac{3}{4}$ of job $2$ and the whole job $3$, while machine $2$ prints the whole job $1$ and $\frac{1}{4}$ of job $2$. Prove that it is optimal by finding, with the complementary slackness conditions, a feasible dual solution with the same objective function value. What is the optimal solution value?

7. **Absolute values (1)**

    A shop recorded the sales of a product in four consecutive weeks: 3, 4, 8 and 9 hundreds of units in weeks 1, 2, 3 and 4, respectively. To forecast the sales of the next weeks, the shop wants to describe the sales with a *trend line*, that is, with a linear function $a + b\,t$ of the week $t$, where the intercept $a$ and the slope $b$ can be any real numbers. In week $t$, the deviation of the line from the recorded sales $y_t$ is $|\,y_t - a - b\,t\,|$. The goal of the shop is to determine the values of $a$ and $b$ that minimize the sum of the deviations in the four weeks.

    **Questions**

    1. Write a Linear Programming (LP) model for the problem. Identify the decisions that must be made and define the corresponding decision variables. Describe the objective function of the model and its constraints. What algorithm can be used to find an optimal solution to the model?

    2. Find a feasible solution of the LP model and accordingly an upper bound on its optimal solution value.

    3. Write the dual model of the LP model. Find a feasible solution of the dual model and accordingly a lower bound on the optimal solution value of the LP model.

    4. Prove that the trend line $1 + 2\,t$ is optimal, by finding with the complementary slackness conditions a feasible dual solution with the same objective function value. What is the optimal solution value?

8. **Covering (1)**

    The emergency department of a hospital divides the day into six periods of four hours: period 1 from 0 to 4, period 2 from 4 to 8, period 3 from 8 to 12, period 4 from 12 to 16, period 5 from 16 to 20 and period 6 from 20 to 24. The minimum number of nurses needed in the six periods is 4, 8, 10, 7, 12 and 4, respectively. Each nurse works a shift of eight consecutive hours, which starts at the beginning of one of the six periods: the shift that starts at the beginning of period 6 continues in period 1 of the following day. The cost of a nurse is 400 euros per shift, except for the night shifts that start at the beginning of periods 1 and 6, which cost 500 euros. The goal of the hospital is to determine how many nurses start their shift at the beginning of each period, so as to cover the requirements of all the periods at minimum cost.

    **Questions**

    1. Write a Linear Programming (LP) model for the problem, measuring the costs in hundreds of euros. Identify the decisions that must be made and define the corresponding decision variables. Describe the objective function of the model and its constraints. What algorithm can be used to find an optimal solution to the model?

    2. Find a feasible solution of the LP model and accordingly an upper bound on its optimal solution value.

    3. Write the dual model of the LP model. Find a feasible solution of the dual model and accordingly a lower bound on the optimal solution value of the LP model.

    4. Prove that the plan in which $4$, $10$, $0$, $8$, $4$ and $0$ nurses start their shift at the beginning of periods $1, 2, \dots, 6$, respectively, is optimal, by finding with the complementary slackness conditions a feasible dual solution with the same objective function value. What is the optimal solution value?
