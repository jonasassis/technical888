from sql_alchemy import db


class SportModel(db.Model):
    __tablename__ = 'sport'
    name = db.Column(db.String(80), primary_key=True)
    # url friendly version of name
    slug = db.Column(db.String(80))
    # either true or false
    active = db.Column(db.Boolean)

    def __init__(self, name, slug, active):
        self.name = name
        self.slug = slug
        self.active = active

    def json(self):
        return {
            'name': self.name,
            'slug': self.slug,
            'active': self.active
        }

    @classmethod
    def find_sport(cls, name):

        sport = cls.query.filter_by(name=name).first()

        if sport:
            return sport
        return None

    def save_sport(self):
        try:
            db.session.add(self)
            db.session.commit()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to save sport'}, 500

    def update_sport(self, name, slug, active):
        self.name = name
        self.slug = slug
        self.active = active

    def delete_sport(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except(Exception,):
            return {'message': 'An internal error ocurred trying to delete sport'}, 500
