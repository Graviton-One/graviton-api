from flask_restx import Api

from .waves import api as waves

api = Api(version='0.3', title='Graviton API', description='An Open API for Gravity, SuSy & Graviton')
api.add_namespace(waves)