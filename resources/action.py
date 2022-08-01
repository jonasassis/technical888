from flask_restful import Resource
import sqlite3
from models.event import EventModel
from flask_jwt_extended import jwt_required


class StartEvent(Resource):

    @jwt_required()
    def post(self, name, sport):

        if not EventModel.find_event(name, sport):
            return {'message': 'Event not found.'.format(name)}, 404

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = "UPDATE event SET status = 'Started', " \
                "actual_start =  DATETIME() " \
                "WHERE name = '" + name + "' " \
                                          "AND sport = '" + sport + "'"

        try:
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to update event'}, 500
        return {'message': 'Event ' + name + ' started'}, 200


class StartEvents(Resource):

    @jwt_required()
    def post(self):

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = "UPDATE event SET status = 'Started', " \
                "actual_start =  DATETIME() " \
                "WHERE scheduled_start <= DATETIME() "

        try:
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to update event'}, 500
        return {'message': 'Events started'}, 200
