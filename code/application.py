from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import hashlib
import public_endpoint
import customer
import customer_rep
import planner 
import storekeeper
import shipper_endpoint

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="db_project_v1.1"

mysql = MySQL(app)

#
# Function that just greets the user when he/she doesn't use any endpoints
#
@app.route('/')
def index():
    return "Welcome!"

#
# When the get_ski_type endpoint is used, we call the GetskiInfo function 
# for the public endpoint
#
@app.route('/get_ski_type',methods=['GET'])
def publicEndpoint():
    return public_endpoint.GetSkiInfo()


# CUSTOMER ENDPOINTS

@app.route('/customer', methods = ['PUT', 'GET'])
def default():
    return "Use the endpoints customer/prodPlanSummary or customer/delete"

#
# When the customer/prodPlanSummary endpoint is used, we call the customer 
# function. 
#
@app.route('/customer/prodPlanSummary', methods = ['GET'])
def customerProdPlanSum(): 
    return customer.customer("prodPlanSummary")

#
# When the customer/delete endpoint is used we call the same function as
#
@app.route('/customer/delete', methods = ['PUT'])
def customerDeleteOrder():
    return customer.customer("delete")


#
# When the customer/new endpoint is used, we call the customer function. 
#
@app.route('/customer/new', methods = ['POST'])
def customerNewOrder(): 
    return customer.customer("new")



# CUSTOMER_REP ENDPOINTS



#
#  When /c_rep/get_orders endpoint is used call Get_state_info
#
@app.route('/c_rep/get_orders',methods=['GET'])
def customerGetOrders(): 
    return customer_rep.Get_state_info()

#
# When /c_rep/change_state endpoint is used call Set_state
#
@app.route('/c_rep/change_state', methods=['PUT'])
def customerSetState():
    return customer_rep.Set_state()



# PLANNER ENDPOINTS

#
#  When /planner/make_prod_plan endpoint is used call MakeProdPlan()
#
@app.route('/planner/make_prod_plan',methods=['POST'])
def plannerMakePlan():
    return planner.MakeProdPlan()


# STOREKEEPER ENDPOINTS


#
# When /storekeeper/create_record endpoint is used call CreateRecord()
#
@app.route('/storekeeper/create_record', methods=['POST'])
def recordSki():
    return storekeeper.CreateRecord()

#
# When /storekeeper/skiis_available endpoint is used call OrderSkiesAvailable()
#
@app.route('/storekeeper/skiis_available', methods=['GET'])
def getSkisAvailable():
    return storekeeper.OrderSkisAvailable() 

#
# When /storekeeper/change_status endpoint is used call ChangeSkisAvailable
#
@app.route('/storekeeper/change_status', methods=['PUT'])
def changeSkisAvailable():
    return storekeeper.ChangeSkisAvailable()


# SHIPPER ENDPOINT

#
# When /shipper/change_status endpoint is used call shipmentOrder()
#
@app.route('/shipper/change_status', methods=['PUT'])
def shipperChangeStatus():
    return shipper_endpoint.shipmentOrder()





# for debugging
if  __name__ == '__main__':
    app.run(debug=True)
