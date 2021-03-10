from flask import Flask
from flask_restx import Resource, Api, reqparse
import json

from core import helpers
from core import config

app = Flask(__name__)
api = Api(app, version='0.1.0', title='Graviton API', description='An Open API for Gravity, SuSy & Graviton')

parser = reqparse.RequestParser()
parser.add_argument("request_id", type=str, required=True)

@api.route('/test')
class Test(Resource):
    def get(self):
        return {'status': 'OK'}

@api.route('/swaps')
class Swaps(Resource):
    @api.expect(parser)
    def get(self):
        '''Returns swap data associated with a specific tx id.'''
        data = helpers.get_contract_data(contract_address=config.waves_luport_address)
        filtered_by_request_id = [i for i in data if i.get('key').endswith(parser.parse_args()["request_id"])]
        return filtered_by_request_id

# @api.route('/supplies')
# class SupplyCheck(Resource):
#     def get(self):
#         '''Returns supplies on blockchain pairs to check supply consistency'''
#         data = helpers.get_contract_data_modified(contract_address=config.waves_luport_address)
        # filtered_data = [i for i in data if i.get('key').startswith('rq_amount')]
        # sum_amounts = sum([i.get('value') for i in filtered_data])
        # return sum_amounts

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

