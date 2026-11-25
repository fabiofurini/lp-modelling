---
hide:
  - navigation
---

# Interactive lab

The models of the course solved to optimality in the browser: change the data with the sliders or by
dragging the points, and a simplex method written in JavaScript recomputes the solution, with the same
numbers as the Python scripts and the lecture notes. Pick an app: it opens full page.

## Models side by side

<div class="grid cards" markdown>

-   :material-chart-timeline-variant: **Three LP models solved to optimality**

    ---

    Production and inventory, electric vehicle charging and the scenario newsvendor: pick the model, change the data with the sliders and the simplex method, in the browser, recomputes the optimal solution and the shadow prices.

    [Open the app →](three-lp-models.md)

-   :material-format-list-numbered: **Nine worked LP models**

    ---

    The nine worked models of chapter 4: production, transportation, diets, multi-period planning, blending and ratios. Change the data with the sliders: the simplex method, in the browser, recomputes the optimal solution, the optimal value and the shadow prices.

    [Open the app →](techniques.md)

</div>

## Deterministic models

<div class="grid cards" markdown>

-   :material-factory: **Production plan and shadow prices**

    ---

    The optimal three-month plan with the inventory: change demand, capacity and holding cost and see which months saturate the machine hours and what one more hour is worth.

    [Open the app →](production-plan.md)

-   :material-ev-station: **Minimum-cost overnight charging**

    ---

    Three vans to charge in the six hours from midnight to 6 am: charging follows the cheap hours as far as the meter limit allows. Change the limit, the energy needed and the prices and see the profile, the cost and the shadow prices.

    [Open the app →](ev-charging.md)

-   :material-bank: **DEA: efficiency and peers of a branch**

    ---

    Pick one of the 12 branches: the envelopment LP gives the efficiency θ, the peers on the frontier with their weights λ and the input targets, with constant (CCR) or variable (BCC) returns to scale.

    [Open the app →](dea-efficiency.md)

</div>

## Decisions under uncertainty

<div class="grid cards" markdown>

-   :material-bread-slice: **Newsvendor: optimal order over 10 scenarios**

    ---

    The expected cost and the CVaR of the cost as functions of the order quantity, over the 10 demand scenarios of the chapter: move the price and the risk aversion and watch the optimal order jump from one scenario to another.

    [Open the app →](newsvendor-scenarios.md)

-   :material-chart-bell-curve: **VaR and CVaR: minimum tail-risk portfolio**

    ---

    The 3 assets and 10 annual scenarios of the chapter: the losses of the minimum-CVaR portfolio, scenario by scenario, with mean, VaR and CVaR, and the return-CVaR frontier. Move the level α and the required return b and watch the shares and the shadow price change.

    [Open the app →](var-cvar.md)

-   :material-scale-balance: **Arbitrage and coherent prices**

    ---

    A risk-free asset, two risky assets and three states: the normalized LP detects arbitrage, the shadow prices give the risk-neutral probabilities. Move the prices and the rate r and watch the interval of coherent prices.

    [Open the app →](arbitrage.md)

</div>

## Optimization and machine learning

<div class="grid cards" markdown>

-   :material-chart-scatter-plot: **Least absolute deviations and quantile regression**

    ---

    The 60 days of the bakery: drag the points and see the least absolute deviations line (LP) and the τ-quantile line, with the support points and how many days stay below the line.

    [Open the app →](quantile-regression.md)

</div>
