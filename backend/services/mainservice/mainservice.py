from flask import Flask
from flask_restful import Api, Resource, reqparse, request
from flask_cors import CORS,cross_origin
import json
import requests

from model import DataModels
from rules.rule import RuleEngine
from model.DataModels import BusinessDetails,BalanceSheetSummary,LoanRequestInfo
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
CORS(app, allow_headers=['Content-Type', 'Access-Control-Allow-Origin',
                         'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE')
    response.headers["Access-Control-Allow-Headers"] = \
        "Access-Control-Allow-Headers,  Access-Control-Allow-Origin, Origin,Accept, " + \
        "X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    return response


class Home(Resource):
    def __init__(self):
        pass

    def get(self):
        return json.dumps({"Message": "Fine"})


api.add_resource(Home, '/')

class GetBalanceSheet(Resource):
    def __init__(self):
        pass

    def get(self):
        return json.dumps({"BalanceShet": "here it is"})

    def post(self):
        # business details
        # accounting provider
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            print("get balancesheet")
            data = request.get_json()
            print(data)
            balancesheet = requests.post('http://accountingservice:5002/getaccounts', json=data)
            print(balancesheet.text)

            # find average assets for last 12 months
            # find profitLastYear

            jsondata = balancesheet.text
            print(jsondata)
            return jsondata
        else:
            return 'Content-Type not supported!'


api.add_resource(GetBalanceSheet, '/balancesheet')


class ProcesLoan(Resource):

    def __init__(self):
        self.ruleEngine = RuleEngine()

    def get(self):
        return json.dumps({"Processing Loan": "applying the rules"})

    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            print(data)

            # process the rules for the balance sheet input
            # calculate the results of the profit for last 1 year
            # apply rule
            # get preassement value
            businessdetails = data['businessdetails']
            profitlastyear = data['profitlastyear']
            averageassets = data['averageassets']
            loanAmount = data['loanAmount']

            balancesheetinfo = BalanceSheetSummary(businessdetails, profitlastyear, averageassets, loanAmount)

            print(balancesheetinfo)

            preassement = self.ruleEngine.calculatePreAssesment(balancesheetinfo)
            print(preassement)

            loanrequest = {"businessdetails": balancesheetinfo.BusinessDetails,
                           "loanAmount": balancesheetinfo.LoanAmount,
                           "preassesment": preassement}

            # call decision engine with user details, balance sheet and preassement

            loanresult = requests.post('http://decisionservice:5001/decideloan', json=json.dumps(loanrequest))
            print(loanresult.content)

            return loanresult.text

        else:
            return 'Content-Type not supported!'


api.add_resource(ProcesLoan, '/procesloan')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
