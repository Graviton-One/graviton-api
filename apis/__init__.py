from flask_restx import Api

from .gton import api as gton

api = Api(version='0.3', title='GTON API', description='An Open API for GTON')
api.add_namespace(gton)