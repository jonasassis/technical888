from flask_restful import Resource, reqparse
from models.sport import SportModel
from flask_jwt_extended import jwt_required
import sqlite3

path_paramns = reqparse.RequestParser()
path_paramns.add_argument('name', type=str)
path_paramns.add_argument('slug', type=str)
path_paramns.add_argument('active', type=bool)


class Sport(Resource):
    args = reqparse.RequestParser()
    args.add_argument('slug', type=str)
    args.add_argument('active', type=bool)

    def get(self, name):

        sport = SportModel.find_sport(name)
        if sport:
            return sport.json(), 200
        return {'message': 'Sport name {} not found.'.format(name)}, 404

    #@jwt_required()
    def post(self, name):

        if SportModel.find_sport(name):
            return {'message': 'Sport name {} already exists.'.format(name)}, 400

        data = Sport.args.parse_args()
        new_sport = SportModel(name, **data)
        try:
            new_sport.save_sport()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save sport'}, 500
        return new_sport.json(), 201

    #@jwt_required()
    def put(self, name):

        data = Sport.args.parse_args()
        sport = SportModel.find_sport(name)

        if sport:
            sport.update_sport(name, **data)
            sport.save_sport()
            return sport.json(), 200

        new_sport = SportModel(name, **data)
        new_sport.save_sport()
        return new_sport.json(), 201

    #@jwt_required()
    def delete(self, name):

        sport = SportModel.find_sport(name)

        if sport:
            sport.delete_sport()
            return {'message': 'Sport deleted'}, 200
        return {'message': 'Sport not found'}, 404
