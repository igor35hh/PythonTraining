from flask import redirect, render_template, session, current_app, url_for
from flask.helpers import flash
from datetime import datetime
from app.email import send_email
from app.main import main
from app.main.forms import NameForm
from app import db
from app.models import User

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/old', methods=['GET', 'POST'])
def indexold():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name')
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), 
                        known=session.get('known', False), current_time=datetime.utcnow())
