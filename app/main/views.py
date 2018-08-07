from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import current_app
from .. import db
from ..models import User
from . import main
from .forms import NameForm

@main.route('/',methods = ['POST','GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('.index'))
    return render_template('index.html',
            form=form,name=session.get('name'),
            known=session.get('known',False))
