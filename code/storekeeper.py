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
#   Creates a record
#

def CreateRecord():
   if request.method == "POST": # if method is POST

        data = request.get_json() # requests json data

        cur=mysql.connection.cursor() # opens db

        # data for ski
        ski_number = data['ski_number'] 
        emp_num = data['emp_num']
        production_date = data['production_date']

        # data for ski_type
        type_id = data['type_id']
        model =  data['model']
        type_of_ski =  data['type_of_ski']
        size =  data['size']
        description =  data['description']
        historical =  data['historical']
        photo_url =  data['photo_url']
        msrpp =  data['msrpp']
        
        # adds ski_type and ski
        cur.execute("INSERT INTO `ski_type` (`type_id`, `model`, `type_of_ski`, `size`, `description`, `historical`, `photo_url`, `msrpp`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [type_id,  model, type_of_ski, size, description, historical, photo_url, msrpp])        
        cur.execute("INSERT INTO `ski` (`ski_number`, `emp_num`, `type_id`, `production_date`) VALUES (%s, %s, %s, %s)", [ski_number, emp_num, type_id, production_date])
    
        # commits to db
        mysql.connection.commit()

        # prints out all data about the newly produced ski
        type= cur.execute("SELECT * FROM `ski_type` INNER JOIN `ski` ON ski_type.type_id = ski.type_id WHERE ski_number=%s", [ski_number]) 
        
        # WHERE `type_id`=%s", [type_id])


        if type >0:
            type = cur.fetchall() # retrieves all data
            cur.close()
            return jsonify(type),201 # sucess
        else:
            return jsonify('There was a problem fetching the data or the ski with that type id doesnt exist!'),404 # error


#
#   Retrieves all skis available
#

def OrderSkisAvailable():
    if request.method == 'GET':

        cur=mysql.connection.cursor()

        order_info= cur.execute("SELECT * FROM `order` WHERE `state`='skis_available'")

        if order_info >0:
            order_info = cur.fetchall()
            cur.close()
            return jsonify(order_info),200
        else:
            return jsonify("There are no orders with state = skiis_available!"),404



#
#   Changes skis to state = 'ready to be shipped'
#

def ChangeSkisAvailable(): 
    if request.method == 'PUT': # if method is PUT

        data = request.get_json()  # request josn data

        cur=mysql.connection.cursor() # open db

        order_number = data['order_number'] # store json data

        state = customer_rep.CurrentState(order_number) # get current state

        if state == "skis_available": # if state is skis_available changes state ti ready_to_be_shipped
            cur.execute("UPDATE `order` SET `state`='ready_to_be_shipped' WHERE `order_number`=%s", [order_number]) 
        else:                         # else error
            return jsonify("You can't change state since the state of this order is " + state),400

        mysql.connection.commit() # commits changes to db

        # prints out changed info about that order
        order = cur.execute("SELECT * FROM `order` WHERE `order_number`=%s", [order_number])

        if order >0:
            order = cur.fetchall()

            cur.close()
            return jsonify(order),201 # sucess 
        else: return jsonify('Nothign Found'),404 # else error