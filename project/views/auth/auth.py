from flask import request
from project.container import auth_service
from flask_restx import Namespace, Resource, abort

api = Namespace('auth')


@api.route('/register')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(401)

        return auth_service.create(data), 201


@api.route('/login')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(401)

        return auth_service.create_token(email, password), 200

    def put(self):
        token = request.json.get('refresh_token')
        tokens = auth_service.approve_token(token)
        return tokens, 200


