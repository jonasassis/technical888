from sql_alchemy import db


class EventModel(db.Model):
    __tablename__ = 'event'
    name = db.Column(db.String(80))
    # url friendly version of name
    slug = db.Column(db.String(80))
    # Either true or false
    active = db.Column(db.Bolean)
    # Either preplay or inplay
    type = db.Column(db.String(80))
    sport = db.Column(db.String(80))
    # Pending, Started, Ended or Cancelled
    status = db.Column(db.String(10))
    # UTC datetime
    scheduled_start = db.Column(db.Datetime)
    # created at the time the event has the status changed to "Started"
    actual_start = db.Column(db.Datetime)

    def __init__(self, name, slug, active, type, sport, status, scheduled_start, actual_start):
        self.name = name
        self.slug = slug
        self.active = active
        self.type = type
        self.sport = sport
        self.status = status
        self.scheduled_start = scheduled_start
        self.actual_start = actual_start

    def json(self):
        return {
            'name': self.name,
            'slug': self.slug,
            'active': self.active,
            'type': self.type,
            'sport': self.sport,
            'status': self.status,
            'scheduled_start': self.scheduled_start,
            'actual_start': self.actual_start
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
        self.scheduled_start = scheduled_start
        self.actual_start = actual_start

    def delete_event(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to delete event'}, 500
