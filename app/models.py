from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(64), index=True, unique=True)
    token = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.userid)
