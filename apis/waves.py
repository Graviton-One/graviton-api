from flask_restx import Resource, Api, Namespace, reqparse

from core import waves_utils, bsc_utils
from core.invoker.Invoker import Invoker
from core.invoker.constants import INFURA_URL

api = Namespace('waves', description='Waves related requests')

parser = reqparse.RequestParser()
parser.add_argument("port_address", type=str, required=True)
parser.add_argument("request_id", type=str, required=True)

@api.route('/test')
class Test(Resource):
    def get(self):
        return {'status': 'OK'}

@api.route('/swaps')
class Swaps(Resource):
    @api.expect(parser)
    def get(self):
        '''Returns swap data associated with a specific port address and tx id.'''
        args = parser.parse_args()
        return waves_utils.get_and_restructure_contract_data(contract_address=args.get('port_address'), tx_id=args.get('request_id'))

@api.route('/supply')
class Supply(Resource):
    def get(self):
        '''Returns GTON circulating supply. '''
        invoker = Invoker(INFURA_URL)
        supply = invoker.getGtonBalance()
        return 21000000 - supply

# @api.route('/supplies')
# class SupplyCheck(Resource):
#     def get(self):
#         '''Returns supplies on blockchain pairs (waves and bsc) to check wrapped USDN supply consistency'''
#         usdn_amount_on_waves = waves_utils.count_usdn_locked_amount(contract_address=config.waves_luport_address)
#         usdn_amount_on_bsc = bsc.get_token_supply_data(contract_address='0xc4b6f32b84657e9f6a73fe119f0967be5ba8cf05')
#         return {'waves':usdn_amount_on_waves, 'bsc':usdn_amount_on_bsc}

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

