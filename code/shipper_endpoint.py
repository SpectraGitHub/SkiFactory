import json
from operator import mod
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import hashlib
import customer_rep

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="db_project_v1.1"

mysql = MySQL(app)


#
# Changes state from 'ready_to_be_shipped' to 'shipped'
#
def shipmentOrder():
    # if method is put
    if request.method == "PUT":

        # requests json data
        data = request.get_json() 

        # opens connection to db
        cur=mysql.connection.cursor()

        # retrieves order number from json
        order_number = data['order_number']

        # gets current state based on the order_number
        state = customer_rep.CurrentState(order_number)

        # if state = ready_to_be_shipped do:
        if state == "ready_to_be_shipped":
            cur.execute("UPDATE `order` SET `state`='shipped' WHERE `order_number`=%s", [order_number]) 
        # else error
        else:
            return jsonify("You can't change state since the state of this order is " + state),400

        # commits the sql query
        mysql.connection.commit()

        # prints out ecerything from that order based on order_number
        order = cur.execute("SELECT * FROM `order` WHERE `order_number`=%s", [order_number])

        if order >0: # checks if orders are greater than 0 and fetches all data
            order = cur.fetchall()

            # close db
            cur.close()
            return jsonify(order),201 # return sucess
        else: return jsonify('Nothign Found'),404  # return error