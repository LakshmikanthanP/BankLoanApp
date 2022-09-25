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

class GetDecision(Resource):
    def __init__(self):
        pass

    def get(self):
        return json.dumps({"GetDecision": "here it is"})

    def post(self):
        # business details
        # accounting provider
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            loanrequest = json.loads(request.get_json())
            print(loanrequest)
            loanamount = 0.2 * int(loanrequest['loanAmount'])
            loanprocessed = False
            preassesment = int(loanrequest['preassesment'])

            if preassesment ==60:
                loanamount = 0.6 * loanamount
                loanprocessed = True
            elif preassesment == 100:
                loanamount = loanamount
                loanprocessed = True
            elif preassesment < 20:
                loanprocessed = False

            result = {"outcome": loanprocessed,"loanamount":loanamount}
            print(result)

            return result
        else:
            return 'Content-Type not supported!'
api.add_resource(GetDecision, '/decideloan')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001, debug=True)