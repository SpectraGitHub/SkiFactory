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
# Function that retrieves data for the skis. The user can also use a model filter
# and a size filter at the same time. 
#
def GetSkiInfo():
    if request.method == 'GET':
        
        # Connceting to the DB: 
        cur=mysql.connection.cursor()

        # Getting the value of both possible parameters in the URL: 
        param = request.args.get("model")
        param2 = request.args.get("size")

        # To do: 
        # 1. Fix the duplicate problem for all requests. 
        #    Most the problem lies with the SQL requests or the logic of the DB

        # Checking first if there are no parameters: 
        if param == None and param2 == None:
            ski_type_info = cur.execute("SELECT ski_type.*, ski.* FROM ski_type LEFT OUTER JOIN ski ON ski_type.type_id = ski.type_id")
        # Then checking if there is only a model parameter: 
        elif param != None and param2 == None: 
            ski_type_info = cur.execute("SELECT ski_type.*, ski.* FROM ski_type INNER JOIN ski ON ski_type.type_id = ski.type_id WHERE ski_type.model=%s", [param] )
        # Then checking if there is only a size parameter: 
        elif param == None and param2 != None:
            ski_type_info = cur.execute("SELECT ski_type.*, ski.* FROM ski_type INNER JOIN ski ON ski_type.type_id = ski.type_id WHERE ski_type.size=%s", [param2])
        # Lastly checking if there exists two parameters at the same time: 
        elif param != None and param2 != None: 
            ski_type_info = cur.execute("SELECT ski_type.*, ski.* FROM ski_type INNER JOIN ski ON ski_type.type_id = ski.type_id WHERE ski_type.size=%s AND ski_type.model=%s", [param2, param])

        
    # Now we have to actually fetch the data, then present it to the user
    # on the screen: 
        if ski_type_info > 0: 
            ski_type_info = cur.fetchall()

            cur.close()
            return jsonify(ski_type_info),201
        else: return jsonify('Nothing Found'),404


