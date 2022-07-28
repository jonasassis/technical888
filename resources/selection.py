from flask_restful import Resource, reqparse
from models.selection import SelectionModel
from flask_jwt_extended import jwt_required
import sqlite3


def check_inactivate_event(name):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = "UPDATE event SET active = 0 " \
            "WHERE name = '" + name + "' " \
            "AND NOT EXISTS ( " \
            "   SELECT * FROM selection s " \
            "WHERE s.event = '" + name + "' " \
            "AND s.active = 1 )"

    cursor.execute(query)
    conn.commit()
    cursor.close()


class Selection(Resource):
    args = reqparse.RequestParser()
    args.add_argument('event', type=str)
    args.add_argument('price', type=str)
    args.add_argument('active', type=bool)
    args.add_argument('outcome', type=str)

    def get(self, name, event):

        selection = SelectionModel.find_selection(name, event)
        if selection:
            return selection.json(), 200
        return {'message': 'Selection name {} not found.'.format(name)}, 404

    #@jwt_required()
    def post(self, name, event):

        data = Selection.args.parse_args()

        if SelectionModel.find_selection(name, event):
            return {'message': 'Selection name {} already exists.'.format(name)}, 400

        new_selection = SelectionModel(name, **data)
        try:
            new_selection.save_selection()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save Selection'}, 500
        return new_selection.json(), 201

    #@jwt_required()
    def put(self, name, event):

        data = Selection.args.parse_args()
        selection = SelectionModel.find_selection(name, event)

        if selection:
            selection.update_selection(name, **data)
            selection.save_selection()
            return selection.json(), 200

        new_selection = SelectionModel(name, **data)
        new_selection.save_selection()
        return selection.json(), 201

    #@jwt_required()
    def delete(self, name, event):

        selection = SelectionModel.find_selection(name, event)
        selection.active = 0

        if selection:
            selection.save_selection()
            check_inactivate_event(event)
            return {'message': 'Selection inactivate'}, 200
        return {'message': 'Selection not found'}, 404


