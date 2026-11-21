# Deterministic models

Three chapters where every datum is known: you decide under certainty, and the
value lies in interrogating the solution (how much is one more unit of a resource
worth? where does the plan break?). The workflow is always the same: build the LP,
solve it, read the duals, move the data and see what holds.

<div class="grid cards" markdown>

-   :material-factory: **Production and inventory**

    ---

    Multi-period LP with inventory: the solver discovers pre-building, the duals
    say how much an hour of capacity is worth.

    [:octicons-arrow-right-24: LP](production.md)

-   :material-ev-station: **Electric vehicle charging**

    ---

    Minimum cost versus peak shaving, hourly energy prices and the duals of the
    energy requirements.

    [:octicons-arrow-right-24: LP](ev-charging.md)

-   :material-bank: **Data Envelopment Analysis**

    ---

    The relative efficiency of twelve branches with one LP per branch: the
    dual gives peers and targets, the CCR/BCC comparison the scale inefficiency.

    [:octicons-arrow-right-24: LP](dea.md)

</div>
