from flask_restful import Resource, reqparse, inputs
import sqlite3


class Sports(Resource):

    def get(self):

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        path_paramns = reqparse.RequestParser()
        path_paramns.add_argument('name', type=str)
        path_paramns.add_argument('slug', type=str)
        path_paramns.add_argument('active', type=inputs.boolean)
        data = path_paramns.parse_args()

        data = {key: data[key] for key in data if data[key] is not None}

        where = ""

        if data.get('name'):
            where += "name LIKE ?"

        if data.get('active') is not None:
            if where != "":
                where += " and "
            where += "active = ?"

        if where != "":
            where = " WHERE " + where
        query = "SELECT * FROM sport" + where

        tupla = tuple([data[key] for key in data])
        result = cursor.execute(query, tupla)

        sports = []
        for line in result:
            sports.append(
                {
                    'name': line[0],
                    'slug': line[1],
                    'active': line[2]
                }
            )

        return {'sports': sports}
