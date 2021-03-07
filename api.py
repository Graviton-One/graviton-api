from flask import Flask
from flask_restx import Resource, Api, reqparse
import helpers
import config
import json

app = Flask(__name__)
api = Api(app, version='0.1.0', title='Graviton API', description='An Open API for Gravity, SuSy & Graviton')

parser = reqparse.RequestParser()
parser.add_argument("request_id", type=str)

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

if __name__ == '__main__':
    app.run()




