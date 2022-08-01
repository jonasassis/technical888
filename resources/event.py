from flask_restful import Resource, reqparse, inputs
from models.event import EventModel
from flask_jwt_extended import jwt_required
import sqlite3


def check_inactivate_event(name):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = "UPDATE sport SET active = 0 " \
            "WHERE name = '" + name + "' " \
            "AND NOT EXISTS ( " \
            "   SELECT * FROM event e " \
            "WHERE e.sport = '" + name + "' " \
            "AND e.active = 1 )"

    cursor.execute(query)
    conn.commit()
    cursor.close()


class Event(Resource):
    args = reqparse.RequestParser()
    args.add_argument('slug', type=str)
    args.add_argument('active', type=bool)
    args.add_argument('type', type=str)
    args.add_argument('sport', type=str)
    args.add_argument('status', type=str)
    args.add_argument('scheduled_start', type=str)
    args.add_argument('actual_start', type=str)

    def get(self, name, sport):

        event = EventModel.find_event(name, sport)
        if event:
            return event.json(), 200
        return {'message': 'Event name {} not found.'.format(name)}, 404

    @jwt_required()
    def post(self, name, sport):

        if EventModel.find_event(name, sport):
            return {'message': 'Event name {} already exists.'.format(name)}, 400

        data = Event.args.parse_args()
        new_event = EventModel(name, **data)
        try:
            new_event.save_event()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save event'}, 500
        return new_event.json(), 201

    @jwt_required()
    def put(self, name, sport):

        data = Event.args.parse_args()
        event = EventModel.find_event(name, sport)

        if event:
            event.update_event(name, **data)
            event.save_event()
            return event.json(), 200

        new_event = EventModel(name, **data)
        new_event.save_event()
        return new_event.json(), 201

    @jwt_required()
    def delete(self, name, sport):

        event = EventModel.find_event(name, sport)
        event.active = 0

        if event:
            event.save_event()
            check_inactivate_event(sport)
            return {'message': 'Event inactivate'}, 200
        return {'message': 'Event not found'}, 404

