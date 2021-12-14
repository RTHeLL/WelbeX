from app import db


class Rows(db.Model):
    __tablename__ = 'rows'

    id = db.Column(db.Integer, primary_key=True, index=True)
    date = db.Column(db.Date, index=True, nullable=False)
    title = db.Column(db.String(128), index=True, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Float, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'date': self.date.strftime("%Y-%m-%d"),
            'title': self .title,
            'count': self.count,
            'distance': self.distance
        }

    def __repr__(self):
        return f'Row: {self.id} - {self.title} - {self.date} - {self.count} - {self.distance}'
