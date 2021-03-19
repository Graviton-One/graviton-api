from flask import Flask
from flask_restx import Resource, Api, reqparse
import json

from core import waves, bsc, config

app = Flask(__name__)
api = Api(app, version='0.3', title='Graviton API', description='An Open API for Gravity, SuSy & Graviton')

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
        args = parser.parse_args()
        print(args)
        data = waves.get_and_restructure_contract_data(contract_address=config.waves_luport_address, tx_id=args.get('request_id'))
        return data


@api.route('/supplies')
class SupplyCheck(Resource):
    def get(self):
        '''Returns supplies on blockchain pairs (waves and bsc) to check wrapped USDN supply consistency'''
        usdn_amount_on_waves = waves.count_usdn_locked_amount(contract_address=config.waves_luport_address)
        usdn_amount_on_bsc = bsc.get_token_supply_data(contract_address='0xc4b6f32b84657e9f6a73fe119f0967be5ba8cf05')
        return {'waves':usdn_amount_on_waves, 'bsc':usdn_amount_on_bsc}

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

