from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddUnits(FlaskForm):
    unit_name = StringField("Unit Name")
    power_rating = IntegerField("Power Rating")
    movement = IntegerField("Movement")
    weapon_skill = IntegerField("Weapon Skill")
    ballistic_skill = IntegerField("Ballistic Skill")
    strength = IntegerField("Strength")
    toughness = IntegerField("Toughness")
    wounds = IntegerField("Wounds")
    attacks = IntegerField("Attacks")
    leadership = IntegerField("Leadership")
    armour_save = IntegerField("Armour Save")
    army_id = IntegerField("Army to link")