from sql_alchemy import db


class SelectionModel(db.Model):
    __tablename__ = 'selection'
    name = db.Column(db.String(80), primary_key=True)
    event = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Float(precision=2))
    # Either true or false
    active = db.Column(db.Boolean)
    # Unsettled, Void, Lose or Win)
    outcome = db.Column(db.String(20))

    def __init__(self, name, event, price, active, outcome):
        self.name = name
        self.event = event
        self.price = price
        self.active = active
        self.outcome = outcome

    def json(self):
        return {
            'name': self.name,
            'event': self.event,
            'price': self.price,
            'active': self.active,
            'outcome': self.outcome,
        }

    @classmethod
    def find_selection(cls, name):

        selection = cls.query.filter_by(name=name).first()

        if selection:
            return selection
        return None

    def save_selection(self):
        try:
            db.session.add(self)
            db.session.commit()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save selection'}, 500

    def update_selection(self, name, event, price, active, outcome):
        self.name = name
        self.event = event
        self.price = price
        self.active = active
        self.outcome = outcome

    def delete_selection(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to delete selection'}, 500
