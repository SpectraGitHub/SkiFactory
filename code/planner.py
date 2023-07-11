from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="db_project_v1.1"

mysql = MySQL(app)

@app.route('/')
def index():
    return "Welcome!"


# http://127.0.0.1:5000/planner/make_prod_plan   


#
# Makes a production plan
#

def MakeProdPlan():

    if request.method == 'POST': # if method is POST 

        data = request.get_json() # request json data

        # stored data from json
        id = data['id']
        nr_ski_type = data['nr_ski_type_everyday']
        ski_production = data['ski_production_everyday']
        start_date = data['start_date']
        end_date = data['end_date']
        type_id = data['type_id']
        type = data['type']


        cur=mysql.connection.cursor() # open db

        # makes prod plan
        cur.execute("INSERT INTO `production_plans` (`id`, `nr_ski_type_everyday`,`ski_production_everyday`, `start_date`, `end_date`) VALUES (%s, %s, %s, %s, %s)", (id, 
        nr_ski_type, ski_production ,start_date, end_date))

        cur.execute("INSERT INTO `prod_plan_ski_type` (`type_id`, `type`) VALUES (%s, %s)", (type_id, type))


        mysql.connection.commit() # commits changes to db

        # prints out production plan
        plan = cur.execute("SELECT * FROM `production_plans` INNER JOIN `prod_plan_ski_type` ON production_plans.id = prod_plan_ski_type.type_id")

        if plan >0:
            plan = cur.fetchall()

            cur.close()
            return jsonify(plan),201 # sucess 

        else: return jsonify('Nothing Found'),404 # else error


