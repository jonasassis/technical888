from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

args = reqparse.RequestParser()
args.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
args.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank")


class User(Resource):

    def get(self, user_id):

        user = UserModel.find_user(user_id)
        if user:
            return user.json(), 200
        return {'message': 'User id {} not found.'.format(user_id)}, 404

    @jwt_required()
    def delete(self, user_id):

        user = UserModel.find_user(user_id)

        if user:
            user.delete_user()
            return {'message': 'User deleted'}, 200
        return {'message': 'User not found'}, 404


class UserRegister(Resource):

    def post(self):

        data = args.parse_args()

        if UserModel.find_by_login(data['login']):
            return {'message': 'Login {} already exists .'.format(data['login'])}, 404

        user = UserModel(**data)
        user.save_user()

        return {'message': 'Login {} created :) .'.format(data['login'])}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = args.parse_args()
        user = UserModel.find_by_login(data['login'])

        if user and safe_str_cmp(user.password, data['password']):
            token_access = create_access_token(identity=user.user_id)
            return {'access_token': token_access}, 200

        return {'message': 'The login and password are incorrect .'}, 401


class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully .'}, 200

