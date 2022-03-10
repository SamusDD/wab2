from application import db

class Army(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    def __str__(self):
        return f"{self.name}"