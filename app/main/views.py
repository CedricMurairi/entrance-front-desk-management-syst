from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash, jsonify
from . import main
from app.models import Visitor
from app import db



@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@main.route('/entrance', methods=['GET', 'POST'])
def entrance():
	name = request.form.get('name')
	email = request.form.get('email')
	person_visited = request.form.get('person_visited')

	try:
		visitor = Visitor(name=name, email=email, person_visited=person_visited)
		db.session.add(visitor)

		flash('Value successfully recorded')

	except Exception as e:
		print(e)
		flash('Value was not recorded, there is something wrong with the entered values')

	return redirect(url_for('.index'))

@main.route('/entries/actives', methods=['GET', 'POST'])
def actives_entries():
	actives_entries = Visitor.query.filter_by(is_out=False).all()
	for visitor in actives_entries:
		print(visitor.name)

	return render_template('actives_entries.html', actives_entries=actives_entries)


@main.route('/entries/all')
def all_entries():
	all_entries = Visitor.query.all()
	for visitor in all_entries:
		print(visitor.name)

	return render_template('all_entries.html', all_entries=all_entries)


@main.route('/exit', methods=['GET', 'POST'])
def exit():
	if request.method == 'POST':
		visitor_id = request.form.get('id')
		visitor = Visitor.query.filter_by(id=visitor_id).first()
		if(visitor.is_out):
			return jsonify({'visitor_already_out': True})
		visitor.is_out = True
		visitor.exit_time = datetime.utcnow()
		db.session.add(visitor)

		return jsonify({"exit": True, "visitor_out": True})
	return redirect(url_for('main.all_entries'))