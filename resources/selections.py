from flask_restful import Resource, reqparse, inputs
import sqlite3


class Selections(Resource):

    def get(self):

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        path_paramns = reqparse.RequestParser()
        path_paramns.add_argument('event', type=str)
        path_paramns.add_argument('active', type=inputs.boolean)
        path_paramns.add_argument('outcome', type=str)
        data = path_paramns.parse_args()

        data = {key: data[key] for key in data if data[key] is not None}

        where = ""

        if data.get('event'):
            where += "event LIKE ?"

        if data.get('active') is not None:
            if where != "":
                where += " and "
            where += "active = ?"

        if data.get('outcome'):
            if where != "":
                where += " and "
            where += "outcome = ?"

        if where != "":
            where = " WHERE " + where

        query = "SELECT * FROM selection" + where

        tupla = tuple([data[key] for key in data])
        result = cursor.execute(query, tupla)

        selections = []
        for line in result:
            selections.append(
                {
                    'name': line[0],
                    'event': line[1],
                    'price': line[2],
                    'active': line[3],
                    'outcome': line[4]
                }
            )

        return {'selections': selections}