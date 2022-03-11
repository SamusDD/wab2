from flask import redirect, url_for
from application import wabapp, db
from application.models import Army
from application.models import Units


@wabapp.route('/')
def home():
    return f"{Army.query.count()} armies: <br>" + '<br>'.join(str(t.name) for t in Army.query.all()) + '<br>' + f"{Units.query.count()} units: <br>" + '<br>'.join(str(t.unit_name) for t in Units.query.all())
    

@wabapp.route('/create-army/<name>')  
def create_army(name):
    army = Army(name=name)
    db.session.add(army)
    db.session.commit() 
    return redirect(url_for('home'))

@wabapp.route('/create-unit/<int:pnum>/<name>/<powerrating>/<movement>/<weaponskill>/<ballisticskill>/<strength>/<toughness>/<wounds>/<attacks>/<leadership>/<armoursave>')
def create_unit(pnum, name, powerrating, movement, weaponskill, ballisticskill, strength, toughness, wounds, attacks, leadership, armoursave):
    new_unit = Units(unit_name = name, power_rating = powerrating, movement = movement, weapon_skill = weaponskill, ballistic_skill = ballisticskill, strength = strength, toughness = toughness, wounds = wounds, attacks = attacks, leadership = leadership, armour_save = armoursave, army_id = pnum)
    db.session.add(new_unit)
    db.session.commit()
    return redirect(url_for('home'))

@wabapp.route('/update-army/<int:pk>/<newarmy>')
def update_army(pk, newarmy):
    army = Army.query.get(pk)
    if newarmy:
        army.name = newarmy
    db.session.commit()
    return redirect(url_for('home'))

@wabapp.route('/update-unit/<int:pk>/<newunit>')
def update_unit(pk, newunit):
    unit = Units.query.get(pk)
    if newunit:
        unit.name = newunit
    db.session.commit()
    return redirect(url_for('home'))

@wabapp.route('/delete-army/<int:pk>')
def delete_army(pk):
    army = Army.query.get(pk)
    db.session.delete(army)
    db.session.commit()
    return redirect(url_for('home'))

@wabapp.route('/delete-unit/<int:pk>')
def delete_unit(pk):
    unit = Units.query.get(pk)
    db.session.delete(unit)
    db.session.commit()
    return redirect(url_for('home'))
