from flask import redirect, url_for
from application import wabapp, db
from application.models import Army

@wabapp.route('/')
def home():
    return '<br>'.join(str(t) for t in Army.query.all())


@wabapp.route('/create/<name>')
def create(name):
    army = Army(name=name)
    db.session.add(army)
    db.session.commit()
    return redirect(url_for('home'))


@wabapp.route('/update/<int:i>/<newarmy>')
def update(i, newarmy):
    army = Army.query.get(i)
    if newarmy:
        army.name = newarmy
    db.session.commit()
    return redirect(url_for('home'))


@wabapp.route('/delete/<int:i>')
def delete(i):
    army = Army.query.get(i)
    db.session.delete(army)
    db.session.commit()
    return redirect(url_for('home'))
