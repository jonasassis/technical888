from flask_restful import Resource, reqparse, inputs
import sqlite3


class Display(Resource):

    def get(self):

        conn = sqlite3.connect('database.db')
        cursor_sports = conn.cursor()
        cursor_events = conn.cursor()
        cursor_selections = conn.cursor()

        path_paramns = reqparse.RequestParser()
        path_paramns.add_argument('active', type=int, default=1)
        data = path_paramns.parse_args()

        data = {key: data[key] for key in data if data[key] is not None}
        tupla = tuple([data[key] for key in data])

        query_sports = "SELECT * FROM sport WHERE active = ?"

        result_sports = cursor_sports.execute(query_sports, tupla)

        sports = []
        for line_sports in result_sports:

            query_events = "SELECT * FROM event WHERE active = ? and sport = '" + line_sports[0] + "'"
            result_events = cursor_events.execute(query_events, tupla)

            events = []
            for lines_events in result_events:

                query_selections = "SELECT * FROM selection WHERE active = ? and event = '" + lines_events[0] + "'"
                result_selections = cursor_selections.execute(query_selections, tupla)

                selections = []
                for line in result_selections:
                    selections.append(
                        {
                            'name': line[0],
                            'event': line[1],
                            'price': line[2],
                            'active': line[3],
                            'outcome': line[4]
                        }
                    )

                events.append(
                    {
                        'name': lines_events[0],
                        'slug': lines_events[1],
                        'active': lines_events[2],
                        'type': lines_events[3],
                        'sport': lines_events[4],
                        'status': lines_events[5],
                        'scheduled_start': lines_events[6],
                        'actual_start': lines_events[7],
                        'selections': selections
                    })

            sports.append({'name': line_sports[0],
                           'slug': line_sports[1],
                           'active': line_sports[2],
                           'events': events})

        return {'result': sports}


class SportsMin(Resource):

    def get(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        path_paramns = reqparse.RequestParser()
        path_paramns.add_argument('minimum', type=int)
        data = path_paramns.parse_args()

        data = {key: data[key] for key in data if data[key] is not None}

        query = "SELECT s.name, count(*) " \
                "FROM sport s INNER JOIN " \
                "event e ON s.name = e.sport " \
                "GROUP BY s.name " \
                "HAVING count(*) >= ?"

        tupla = tuple([data[key] for key in data])
        result = cursor.execute(query, tupla)

        selections = []
        for line in result:
            selections.append({'name': line[0]})

        return {'sport': selections}


class EventsSports(Resource):

    def get(self):

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        path_paramns = reqparse.RequestParser()
        path_paramns.add_argument('minimum', type=int)
        data = path_paramns.parse_args()

        data = {key: data[key] for key in data if data[key] is not None}

        query = "SELECT s.name, count(*) " \
                "FROM sport s INNER JOIN " \
                "event e ON s.name = e.sport " \
                "GROUP BY s.name " \
                "HAVING count(*) >= ?"

        tupla = tuple([data[key] for key in data])
        result = cursor.execute(query, tupla)

        selections = []
        for line in result:

            query = "SELECT * FROM event WHERE sport = '" + line[0] + "'"

            result_events = cursor.execute(query)

            events = []
            for line_events in result_events:
                events.append(
                    {
                        'name': line_events[0],
                        'slug': line_events[1],
                        'active': line_events[2],
                        'type': line_events[3],
                        'sport': line_events[4],
                        'status': line_events[5],
                        'scheduled_start': line_events[6],
                        'actual_start': line_events[7]
                    }
                )

            selections.append({line[0]: events})

        return {'sport': selections}
