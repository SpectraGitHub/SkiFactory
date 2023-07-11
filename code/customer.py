import json
from re import M
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import hashlib
import random

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_project_v1.1"

mysql = MySQL(app)

#
# Function that gets called when the 
# 
def customer(x):
    # If the parameter is "prodPlanSummary" then this part of the function will be run: 
    if x == "prodPlanSummary": 
        if request.method == 'GET':
            
            # Connecting to the SQL DB:
            cur = mysql.connection.cursor()

            # Retrieving parameter from the request. 
            modelParam = request.args.get("model")

            # Cheks if a parameter is included in the request: 
            if modelParam != None:
            # Executing a SQL query:
            # This query is very long.. however if it works, it works ;)
                productionPlans = cur.execute("SELECT ski_type.type_id, ski_type.model, ski_type.type_of_ski, ski_type.size, ski_type.description, production_plans.id, production_plans.nr_ski_type_everyday, production_plans.ski_production_everyday, production_plans.start_date, production_plans.end_date FROM prod_plan_ski_type INNER JOIN ski_type ON prod_plan_ski_type.type = ski_type.type_id INNER JOIN production_plans ON prod_plan_ski_type.type_id = production_plans.id WHERE ski_type.model = %s", [param])


            # If there is no parameter included, then a general search is made
            elif modelParam == None: 
                productionPlans = cur.execute("SELECT ski_type.type_id, ski_type.model, ski_type.type_of_ski, ski_type.size, ski_type.description, production_plans.id, production_plans.nr_ski_type_everyday, production_plans.ski_production_everyday, production_plans.start_date, production_plans.end_date FROM prod_plan_ski_type INNER JOIN ski_type ON prod_plan_ski_type.type = ski_type.type_id INNER JOIN production_plans ON prod_plan_ski_type.type_id = production_plans.id")


            # If the productionPlans variable actually holds any tuples:
                if productionPlans > 0:
                    productionPlans = cur.fetchall()
                    cur.close()

                    return jsonify(productionPlans), 201
                else: return jsonify('Nothing found'), 404 

        elif request.method == 'PUT':
            return "Method not allowed"
    
    # If the parameter is "delete" then this part of the function will be run: 
    elif x == "delete": 
        if request.method == 'DELETE': 
            
            # Connecting to the SQL DB:
            cur = mysql.connection.cursor()
            
            #Retrieving the parameter which contains which order to delete: 
            deleteParam = request.args.get("delete")

            # If there is no parameter given in the URL, then an info message is returned: 
            if deleteParam == None: 
                return "Please use the parameter delete to choose which order you want to delete"
            # If there actually is a parameter included, we can continue with the deletion: 
            elif deleteParam != None: 
                # Deletes the order that are like the parameter: 
                cur.execute("DELETE FROM orders WHERE order.id = %s", [deleteParam])
                mysql.connection.commit()

                cur.close() # Closing the connection
                return jsonify('Your order with id %s has been deleted', [deleteParam]), 201
        
        elif request.method == 'GET' or request.method == 'PUT': 
            return "Method not allowed"

    # If the parameter is "new" then this part of the function will be run: 
    elif x == "new":
        if request.method == 'POST': 
            
            # Connecting to the SQL DB: 
            cur = mysql.connection.cursor()

            # Retrieving the parameters
            model        = request.args.get("model")
            customerID   = request.args.get("customerID")
            quantity     = request.args.get("quantity")
            customerType = request.args.get("customerType")


            if model != None and customerID != None and quantity != None and customerType != None:
                # Hent ut antall customer reps. Lagre dem i et array 
                # Få antall customer reps

                # Retriving the quantity of customer reps in the DB: 
                quantityOfCustomerReps = cur.execute("SELECT customer_rep.employee_number FROM `customer_rep`")

                # If there are any customer reps in the system
                if quantityOfCustomerReps > 0:
            
                    # Retrieving the tuples: 
                    quantityOfCustomerReps = cur.fetchall()

                    customerReps = [] # List with all the customer reps id's

                    # Adding the id's to a list with for loops: 
                    for i in range(len(quantityOfCustomerReps)):
                        for j in range(len(quantityOfCustomerReps[i])):
                             customerReps.append(quantityOfCustomerReps[i][j])

                    # Choosing a customer rep for the order: 
                    chosenCustomerRep = random.choice(customerReps)

                    # Retrieving the order id's that already exist: 
                    #orderIDs = cur.execute("SELECT order.order_number FROM `order`")
                  #  orderIDsList = [] # List with all the order id's

                    # If there are many order id's: 
                    #if orderIDs > 1: 
                    #    print("\n\nOrder id her: ", orderIDs)
                        # Adding the id's to a list with for loops: 
                      #  for i in range(len(orderIDs)):
                      #      for j in range(len(orderIDs[i])):
                      #          orderIDsList.append(orderIDs[i][j])
                    # If there is only one order id: 
                    #else:
                    #    print("hallo") # orderIDsList.append(orderIDs)
                
                # Important: Retrieving the order IDs currently do not work. 
                #            To do: Figure out how to retireve the order id's
                #            so that the code can compare the new order id with
                #            the ones that already exist!



                    # A new order id is given: 
                    newOrderID = random.randrange(1, 10000) 
                #    uniqueID = True # We're assuming that the order ID is unique!
                #    helper = False
                    
                # IMPORTANT: I have commented this part away, because at the time
                #            being the loop gets stuck in an infinite loop.
                #            To do: Figure out how the loop doesn't get stuck!
                #    while(helper == False):
                #        for i in range(len(orderIDsList)): 
                #            if newOrderID == orderIDsList[i]:
                #                newOrderID = random.randrange(1, 10000) # The order is given a new ID since it was equal to an already existing order id. 
                #                uniqueID == False # If the id already exist
                #                break                # we set the boolean to be false and we break
                       
                #       # If the ID is unique, then we can exit the loop: 
                #        if(uniqueID != False):
                #            helper == True
                         

                    # Retrieves the id for the selected model that the order is on: 
                    retrieveSkiID = cur.execute("SELECT ski_type.type_id FROM ski_type WHERE ski_type.model = %s", [model])

                    # Creating a price for the skis: 
                    value = quantity * 100

                    if retrieveSkiID > 0:
                        
                        if retrieveSkiID > 1:
                            ski_typeID = retrieveSkiID[0][0] # Stores the id in a variable

                            
                        else: 
                            ski_typeID = retrieveSkiID

                        # Retrieving the type of ski that the user wants to order: 
                        typeOfSki = cur.execute("SELECT ski_type.type_of_ski FROM ski_type WHERE ski_type.type_id = %s", [ski_typeID])

                        if typeOfSki > 1: 
                            typeOfSki2 = typeOfSki[0][0] # Storing the type of ski in a variable
                        else:
                            typeOfSki2 = typeOfSki

                        # Checks which types of customer it is:
                        if customerType == "franchise":
                            # Creates a new order: 
                            cur.execute("INSERT INTO `order` (order_number, franchise_id, individualStore_id, teamSki_id, s_number, ski_type, quantity, tot_price, state, state_change) VALUES (%s, %s, 1, 1, 1, %s, %s, %s, 'new', %s", [newOrderID, customerID, typeOfSki2, quantity, value, chosenCustomerRep]) 
                            mysql.connection.commit()
                        elif customerType == "individualStore":
                            # Creates a new order: 
                            cur.execute("INSERT INTO `order` (order_number, franchise_id, individualStore_id, teamSki_id, s_number, ski_type, quantity, tot_price, state, state_change) VALUES (%s, 1, %s, 1, 1, %s, %s, %s, 'new', %s", [newOrderID, customerID, typeOfSki2, quantity, value, chosenCustomerRep]) 
                            mysql.connection.commit()
                        elif customerType == "teamSkier":
                            # Creates a new order:
                            cur.execute("INSERT INTO `order` (order_number, franchise_id, individualStore_id, teamSki_id, s_number, ski_type, quantity, tot_price, state, state_change) VALUES (%s, 1, 1, %s, 1, %s, %s, %s, 'new', %s", [newOrderID, customerID, typeOfSki2, quantity, value, chosenCustomerRep]) 
                            mysql.connection.commit()

                        # We need to create a new tuple in the table for the relationship
                        # between the order and the ski type: 
                        cur.execute("INSERT INTO `order_skitype` (o_num, type, quantity) VALUES (%s, %s, %s)", [newOrderID, ski_typeID , quantity])
                        mysql.connection.commit()
                        cur.close()
                        return jsonify('Your order has been registered!'), 201

                    else: return jsonify('This model does not exist!'), 404

                else: return jsonify('There are no customer reps for you atm!'), 404

               # cur.execute("INSERT INTO order")
            else: 
                return "Please use the parameters model, customerID, quantity and customerType. IMPORTANT: Choose between the values franchise, individualStore and teamSkier for the values of the parameter customerType"


        
