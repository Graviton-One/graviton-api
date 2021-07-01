from flask_restx import Resource, Api, Namespace, reqparse

from core.invoker.Invoker import Invoker
from core.invoker.constants import INFURA_URL

api = Namespace('gton', description='Gton related requests')

@api.route('/circulating')
class Circulating(Resource):
    def get(self):
        '''Returns GTON circulating supply. '''
        invoker = Invoker(INFURA_URL)
        supply = invoker.getGtonBalance()
        circulating = 21000000 - supply
        return circulating

# @api.route('/supplies')
# class SupplyCheck(Resource):
#     def get(self):
#         '''Returns supplies on blockchain pairs (waves and bsc) to check wrapped USDN supply consistency'''
#         usdn_amount_on_waves = waves_utils.count_usdn_locked_amount(contract_address=config.waves_luport_address)
#         usdn_amount_on_bsc = bsc.get_token_supply_data(contract_address='0xc4b6f32b84657e9f6a73fe119f0967be5ba8cf05')
#         return {'waves':usdn_amount_on_waves, 'bsc':usdn_amount_on_bsc}

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

