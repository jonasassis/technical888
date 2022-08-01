from flask_restful import Resource, reqparse, inputs
import sqlite3


class Events(Resource):

    def get(self):

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        path_paramns = reqparse.RequestParser()
        path_paramns.add_argument('name', type=str)
        path_paramns.add_argument('active', type=inputs.boolean)
        path_paramns.add_argument('scheduled_start_min', type=str)
        path_paramns.add_argument('scheduled_start_max', type=str)
        path_paramns.add_argument('sport', type=str)
        path_paramns.add_argument('status', type=str)
        data = path_paramns.parse_args()

        data = {key: data[key] for key in data if data[key] is not None and data[key] != ""}

        where = ""

        if data.get('name'):
            where += "name LIKE ?"

        if data.get('active') is not None:
            if where != "":
                where += " and "
            where += "active = ?"

        if data.get('scheduled_start_min') and data.get('scheduled_start_max'):
            if where != "":
                where += " and "
            where += 'scheduled_start BETWEEN ? AND ? '

        if data.get('sport'):
            if where != "":
                where += " and "
            where += "sport = ?"

        if data.get('status'):
            if where != "":
                where += " and "
            where += "status = ?"

        if where != "":
            where = " WHERE " + where

        query = "SELECT * FROM event" + where

        tupla = tuple([data[key] for key in data])
        result = cursor.execute(query, tupla)

        events = []
        for line in result:
            events.append(
                {
                    'name': line[0],
                    'slug': line[1],
                    'active': line[2],
                    'type': line[3],
                    'sport': line[4],
                    'status': line[5],
                    'scheduled_start': line[6],
                    'actual_start': line[7]
                }
            )

        return {'events': events}