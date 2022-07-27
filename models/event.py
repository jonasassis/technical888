from sql_alchemy import db
from datetime import datetime


class EventModel(db.Model):
    __tablename__ = 'event'
    name = db.Column(db.String(80), primary_key=True)
    # url friendly version of name
    slug = db.Column(db.String(80))
    # Either true or false
    active = db.Column(db.Boolean)
    # Either preplay or inplay
    type = db.Column(db.String(80))
    sport = db.Column(db.String(80), primary_key=True)
    # Pending, Started, Ended or Cancelled
    status = db.Column(db.String(10))
    # UTC datetime
    scheduled_start = db.Column(db.DateTime)
    # created at the time the event has the status changed to "Started"
    actual_start = db.Column(db.DateTime)

    def __init__(self, name, slug, active, type, sport, status, scheduled_start, actual_start):

        self.name = name
        self.slug = slug
        self.active = active
        self.type = type
        self.sport = sport
        self.status = status
        self.scheduled_start = datetime.strptime(scheduled_start, '%d-%m-%Y %H:%M:%S')
        self.actual_start = datetime.strptime(actual_start, '%d-%m-%Y %H:%M:%S')

    def json(self):

        return {
            'name': self.name,
            'slug': self.slug,
            'active': self.active,
            'type': self.type,
            'sport': self.sport,
            'status': self.status,
            'scheduled_start': self.scheduled_start.strftime('%d-%m-%Y %H:%M:%S'),
            'actual_start': self.actual_start.strftime('%d-%m-%Y %H:%M:%S')
        }

    @classmethod
    def find_event(cls, name):

        event = cls.query.filter_by(name=name).first()

        if event:
            return event
        return None

    def save_event(self):
        try:
            db.session.add(self)
            db.session.commit()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save event'}, 500

    def update_event(self, name, slug, active, type, sport, status, scheduled_start, actual_start):
        self.name = name
        self.slug = slug
        self.active = active
        self.type = type
        self.sport = sport
        self.status = status
        self.scheduled_start = datetime.strptime(scheduled_start, '%d-%m-%Y %H:%M:%S')
        self.actual_start = datetime.strptime(actual_start, '%d-%m-%Y %H:%M:%S')

    def delete_event(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to delete event'}, 500
