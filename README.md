<h1>Ski Factory</h1>

Leidulf Vigre and Benjamin L. Wood


## About
In this project, we developed a database system for a Ski factory, such as [Madshus](https://madshus.com/no-no/support/story), with RESTful APIs for different types of users. The example is a Ski equipment manufacturer that has several internal divisions such as, Sales & delivery, Factory, Storage and Administration.

## Project endpoints: 
- Public endpoint:
   - Retrieves list of ski types with model filter
   - Use endpoint: /get_ski_type

- Storekeeper:
   - Creates records newly produced skis
   - Use endpoint: /storekeeper/create_record
                   /storekeeper/skiis_available
                   /storekeeper/change_status

- Customer:
   - Retrieves a four week production plan summary
   - Deletes a given order
   - Use endpoint: /customer
                   /customer/prodPlanSummary
                   /customer/delete
                   /customer/new

- Customer rep:
   - Retrieves orders with status filter set to new
   - Changes the order state from new to open for an unassigned order
   - Use endpoint: /c_rep/get_orders
                   /c_rep/change_state

- Planner:
   - Creates new production plans
   - Use endpoint: /planner/make_prod_plan

- Shipper endpoint:
   - Creates a transition record for the order from ready-for-shipping to shipped for a ready-for-shipping order
   - Use endpoint: /shipper/change_status
