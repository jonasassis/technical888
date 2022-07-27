from flask import Flask, jsonify
from flask_restful import Api
from resources.sport import Sport
from resources.sports import Sports
from resources.event import Event
from resources.events import Events
from resources.selection import Selection
from resources.selections import Selections

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)

api.add_resource(Sports, '/sports')
api.add_resource(Sport, '/sports/<string:name>')
api.add_resource(Events, '/events')
api.add_resource(Event, '/events/<string:name>')
api.add_resource(Selections, '/selections')
api.add_resource(Selection, '/selections/<string:name>')


if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)