from flask_restplus import Api

from .pets import api as pets

api = Api(
    title='API',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(pets, path='/apiPets')
# ...
#api.add_namespace(nsX, path='/prefix/of/ns1'))