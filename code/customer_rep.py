from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="db_project_v1.1"

mysql = MySQL(app)

#
# Kommenterer bort denne, pga application tar seg av dette:  
#
#@app.route('/')
#def index():
#    return "Welcome!"


# http://127.0.0.1:5000/c_rep/get_orders?state={state}

# Kommenterer også bort routen siden application også tar seg av dette.
#@app.route('/c_rep/get_orders',methods=['GET'])
def Get_state_info():

    if request.method == 'GET': # if method is GET

        cur=mysql.connection.cursor()  # opens connection to db
        
        param = request.args.get("state")  # gets state based on what you specify

        if param != "" and param != None: # checks if the url has a state specified and not empty
            if param == "new":
                orders_info = cur.execute("SELECT * FROM `order` WHERE `state`='new'")  # if new run this
            elif param == "open":
                orders_info = cur.execute("SELECT * FROM `order` WHERE `state`='open'") # if open run this
            elif param == "skis_available":
                orders_info = cur.execute("SELECT * FROM `order` WHERE `state`='skis_available'") # if skis_available run this
        else: 
            return jsonify('State not correct or you need to specify state in URL! E.g: ?state=new') # else error

        if orders_info > 0:
            orders_info = cur.fetchall() # retrieves all data

            cur.close()                  # clsoe db
            return jsonify(orders_info),200 # sucess


        else: return jsonify('Nothing Found'),404 # else error



#  http://127.0.0.1:5000/c_rep/change_state   eks json. {"order_number": 1}

#
#   Changes state for an order a given a order_number
#
def Set_state():

    if request.method == 'PUT':
        data = request.get_json()  # requests json data

        cur=mysql.connection.cursor()  # opens connection to db
        
        order_number = data['order_number']  # gets order_number from json
       
        state = CurrentState(order_number)  # gets current state
    
        if state == "new":      # if current state is new it will set it to open
            cur.execute("UPDATE `order` SET `state`='open' WHERE `order_number`=%s", [order_number])
        elif state == "open":   # if current state is open it will set it to skis_available
            cur.execute("UPDATE `order` SET `state`='skis_available' WHERE `order_number`=%s", [order_number])
        else:                   # else if skis_available = skis available 
            return jsonify('State already set to ' + state + " and cannot be changed"), 406
            # for test purpose comment the return and uncomment the line under to set it to new: 
            #cur.execute("UPDATE `order` SET `state`='new' WHERE `order_number`=%s", [order_number])
  
        mysql.connection.commit() # commits to db

        orders = cur.execute("SELECT * FROM `order`") # prints out all orders

        if orders >0:
            orders = cur.fetchall() # fetch data
        
            cur.close()
            return jsonify(orders),201 # sucess

        else: return jsonify('Nothing Found'),404 # else error


#
#   Returns the current state of order based on number 
#
def CurrentState(number):
    # Connecting to the DB
    cur=mysql.connection.cursor()
    # Gets state based on order number
    state = cur.execute("SELECT `state` FROM `order` WHERE `order_number`=%s", [number])
    # Converts tuple to string
    state = str(cur.fetchone()[0]) 
    # returns current state
    return state


