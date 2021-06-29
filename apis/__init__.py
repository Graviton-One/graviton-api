from flask_restx import Api

from .waves import api as waves
from .gton import api as gton

api = Api(version='0.3', title='Graviton API', description='An Open API for Gravity, SuSy & Graviton')
api.add_namespace(waves)
api.add_namespace(gton)