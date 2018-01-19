from flask import Flask, request
from flask_restplus import Resource, Api, reqparse, abort, fields
import db
from logging.handlers import RotatingFileHandler
import logging

app = Flask(__name__)
api = Api(app, version='1.0', title='Pets API',
          description='A pets API',
          )


ns = api.namespace('pets', description='Pets operations')


def is_gender(value):
    if value != 'm' and value != 'w':
        #        msg = "%r is not a gender" % value
        #        app.logger.error('is_gender error occurred %r', value)
        raise ValueError()
    return value


parser = reqparse.RequestParser()
parser.add_argument('gender', type=is_gender, required=True,
                    help='No gender or invalid value', location='json')
parser.add_argument('species', type=str, required=True,
                    help='No species provided', location='json')
parser.add_argument('birthday', type=str, required=True,
                    help='No birthday provided', location='json')
parser.add_argument('name', type=str, required=True,
                    help='No name provided', location='json')


model = api.model('Pet', {
    'gender': fields.String(default='m', description='Possible values: ', enum=['m', 'w'], required=True),
    'species': fields.String(required=True),
    'birthday': fields.Date(dt_format='ISO8601', required=True),
    'name': fields.String(required=True)
})


@api.route('/api/pet/<petId>', endpoint='pet')
@api.doc(params={'petId': 'An ID'})
class Pet(Resource):
    def get(self, petId):
        return db.getPet(petId)

#    @ns.response(204, 'Pet deleted')
#    def delete(self, petId):
#        return '', 204

#    @api.doc(model='Pet')
    @api.expect(model)
    def put(self, petId):
        args = parser.parse_args(strict=True)
        item_data = request.json
        db.updatePet(petId, item_data)
        return args, 200

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)

# TodoList
# shows a list of all pets, and lets you POST to add new pet -> not implemented yet


@api.route('/api/pets', endpoint='pets')
class Pets(Resource):
    def get(self):
        return db.getPets()

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)


if __name__ == '__main__':
    handler = RotatingFileHandler('log.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)
