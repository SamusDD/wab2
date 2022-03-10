from application import db

class Units(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    unit_name = db.Column(db.String(50))
    power_rating = db.Column(db.Integer)
    movement = db.Column(db.Integer)
    weapon_skill = db.Column(db.Integer)
    ballistic_skill = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    toughness = db.Column(db.Integer)
    wounds = db.Column(db.Integer)
    attacks = db.Column(db.Integer)
    leadership = db.Column(db.Integer)
    armour_save = db.Column(db.Integer)
    def __str__(self):
        return f"Name: {self.unit_name}, power rating: {self.power_rating}, movement: {self.movement}, weapon skill: {self.weapon_skill}, ballistic skill: {self.ballistic_skill}, strength: {self.strength}, toughness: {self.toughness}, wounds: {self.wounds}, attacks: {self.attacks}, leadership: {self.leadership}, armour save: {self.armour_save}"

class Army(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    proj_items = db.relationship('Units', backref='Army')
    def __str__(self):
        return f"{self.name}"

