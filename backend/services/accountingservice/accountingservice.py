import decimal
import random

from flask import Flask
from flask_restful import Api, Resource, reqparse, request
import json

app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE')
    return response

class BalancesheetMockReports:

    @staticmethod
    def GenerateReport():
        year =2021
        months = [x for x in range(1,12)]
        yearlyInfo = []

        for month in months:
            yearlyInfo.append({"year": year, "month":month, "profitOrLoss":random.randrange(-1, 23433443), "assetsvalue": random.randrange(-109855, 38090009)})
        netprofit = sum(y['profitOrLoss'] for y in yearlyInfo)
        netavgasset = sum(y['assetsvalue'] for y in yearlyInfo)

        balancesheet = {"profitLastYear": netprofit, "netaverageassets": netavgasset,
                        "yearlyreport":yearlyInfo}
        return  balancesheet

class GenerateBalSheet(Resource):
    def __init__(self):
        pass

    def get(self):
        return json.dumps({"BalanceShet": "here it is"})

    def post(self):
        # business details
        # accounting provider
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            jsondata = request.json
            yearlybalancesheet = BalancesheetMockReports.GenerateReport()
            print(yearlybalancesheet)

            #return "string"
            return json.loads(json.dumps(yearlybalancesheet))
        else:
            return 'Content-Type not supported!'
api.add_resource(GenerateBalSheet, '/getaccounts')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5002, debug=True)