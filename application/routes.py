from flask import redirect, url_for, render_template, request
from application import wabapp, db
from application.models import Army
from application.models import Units
from application.forms import AddUnits


@wabapp.route('/')
def home():
    num_units = Units.query.count()
    units = [str(unit) + " " + str(unit.army) for unit in Units.query.all()]
    return render_template('index.html', num = num_units, units = units)
    

@wabapp.route('/create-army/<name>')  
def create_army(name):
    army = Army(name=name)
    db.session.add(army)
    db.session.commit() 
    return redirect(url_for('home'))

@wabapp.route('/create-unit', methods=['GET', 'POST'])
def create_unit():
    form = AddUnits()
    if request.method == 'POST':
        unit_name = form.unit_name.data
        power_rating = form.power_rating.data
        movement = form.movement.data
        weapon_skill = form.weapon_skill.data
        ballistic_skill = form.ballistic_skill.data
        strength = form.strength.data
        toughness = form.toughness.data
        wounds = form.wounds.data
        attacks = form.attacks.data
        leadership = form.leadership.data
        armour_save = form.armour_save.data
        army_id = form.army_id.data
        new_unit = Units(unit_name = unit_name, power_rating = power_rating, movement = movement, weapon_skill = weapon_skill, ballistic_skill = ballistic_skill, strength = strength, toughness = toughness, wounds = wounds, attacks = attacks, leadership = leadership, armour_save = armour_save, army_id = army_id)
        db.session.add(new_unit)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_unit.html', form = form)

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
