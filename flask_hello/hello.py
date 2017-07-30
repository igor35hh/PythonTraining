from flask import Flask
from flask.helpers import make_response, url_for, flash
from flask import redirect, abort, render_template, session
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
	name = StringField('What id your name?', validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	#return '<h1>Hello World</h1>'
	#return render_template('index.html', current_time=datetime.utcnow())
	#name = None
	form = NameForm()
	if form.validate_on_submit():
		#name = form.name.data
		#form.name.data = ''
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	#return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())
	return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
	#return '<h1>Hello, %s</h1>' % name
	url1 = url_for('user', name=name, _external = False)
	url2 = url_for('user', name=name, _external = True)
	print(url1, url2)
	return render_template('user.html', name=name)
	

@app.route('/404')
def badrequest():
	return '<h1>Bad Request</h1>', 400

@app.route('/res')
def res():
	response = make_response('<h1>This document carries a cookie</h1>')
	response.set_cookie('answer', '42')
	return response

@app.route('/red')
def red():
	return redirect('http://www.google.com')

@app.route('/bad')
def bad():
	abort(404)
	return '<h1>Not found</h1>'

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	#app.run(debug=True)
	manager.run()