from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remembre_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('mian.index')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('main.index'))
