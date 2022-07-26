from flask import Flask, jsonify
from flask_restful import Api
from resources.sport import Sport
from resources.sports import Sports
from resources.event import Event
from resources.events import Events
from resources.selection import Selection
from resources.selections import Selections
from resources.user import User, UserRegister, UserLogin, UserLogout
from resources.displays import SportsMin, EventsSports, Display, EventsMin
from resources.action import StartEvent, StartEvents
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_database():
    db.create_all()


@jwt.token_in_blocklist_loader
def check_blacklist(self, token):
    return token['jti'] in BLACKLIST


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify({'message': 'Token expired'}), 401


@jwt.revoked_token_loader
def access_token_invalid(self, BLACKLIST):
    return jsonify({'message': 'You have been logged out'}), 401


api.add_resource(Sports, '/sports')
api.add_resource(Sport, '/sports/<string:name>')
api.add_resource(Events, '/events')
api.add_resource(Event, '/events/<string:name>/<string:sport>')
api.add_resource(Selections, '/selections')
api.add_resource(Selection, '/selections/<string:name>/<string:event>')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(SportsMin, '/sportsmin')
api.add_resource(EventsMin, '/eventsmin')
api.add_resource(EventsSports, '/events/sport')
api.add_resource(Display, '/display')
api.add_resource(StartEvent, '/startevent/<string:name>/<string:sport>')
api.add_resource(StartEvents, '/startevents')

if __name__ == '__main__':
    from sql_alchemy import db

    db.init_app(app)
    app.run(host='0.0.0.0')
