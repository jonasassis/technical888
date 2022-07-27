from flask_restful import Resource, reqparse
from models.selection import SelectionModel
from flask_jwt_extended import jwt_required
import sqlite3


class Selection(Resource):
    args = reqparse.RequestParser()
    args.add_argument('event', type=str)
    args.add_argument('price', type=str)
    args.add_argument('active', type=bool)
    args.add_argument('outcome', type=str)

    def get(self, name):

        selection = SelectionModel.find_selection(name)
        if selection:
            return selection.json(), 200
        return {'message': 'Selection name {} not found.'.format(name)}, 404

    #@jwt_required()
    def post(self, name):

        if SelectionModel.find_selection(name):
            return {'message': 'Selection name {} already exists.'.format(name)}, 400

        data = Selection.args.parse_args()
        new_selection = SelectionModel(name, **data)
        try:
            new_selection.save_selection()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save Selection'}, 500
        return new_selection.json(), 201

    #@jwt_required()
    def put(self, name):

        data = Selection.args.parse_args()
        selection = SelectionModel.find_selection(name)

        if selection:
            selection.update_selection(name, **data)
            selection.save_selection()
            return selection.json(), 200

        new_selection = SelectionModel(name, **data)
        new_selection.save_selection()
        return selection.json(), 201

    #@jwt_required()
    def delete(self, name):

        selection = SelectionModel.find_selection(name)

        if selection:
            selection.delete_selection()
            return {'message': 'Selection deleted'}, 200
        return {'message': 'Selection not found'}, 404
