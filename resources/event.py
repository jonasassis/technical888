from flask_restful import Resource, reqparse, inputs
from models.event import EventModel
from flask_jwt_extended import jwt_required
import sqlite3


class Event(Resource):
    args = reqparse.RequestParser()
    args.add_argument('slug', type=str)
    args.add_argument('active', type=bool)
    args.add_argument('type', type=str)
    args.add_argument('sport', type=str)
    args.add_argument('status', type=str)
    args.add_argument('scheduled_start', type=str)
    args.add_argument('actual_start', type=str)

    def get(self, name):

        event = EventModel.find_event(name)
        if event:
            return event.json(), 200
        return {'message': 'Event name {} not found.'.format(name)}, 404

    #@jwt_required()
    def post(self, name):

        if EventModel.find_event(name):
            return {'message': 'Event name {} already exists.'.format(name)}, 400

        data = Event.args.parse_args()
        new_event = EventModel(name, **data)
        try:
            new_event.save_event()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save event'}, 500
        return new_event.json(), 201

    #@jwt_required()
    def put(self, name):

        data = Event.args.parse_args()
        event = EventModel.find_event(name)

        if event:
            event.update_event(name, **data)
            event.save_event()
            return event.json(), 200

        new_event = EventModel(name, **data)
        new_event.save_event()
        return new_event.json(), 201

    #@jwt_required()
    def delete(self, name):

        event = EventModel.find_event(name)

        if event:
            event.delete_event()
            return {'message': 'Event deleted'}, 200
        return {'message': 'Event not found'}, 404
