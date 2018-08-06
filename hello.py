import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask import flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))            #获取当前文件所在路径

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/xuemc_db'
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64),unique = True)
    users = db.relationship(u'User',backref ='role',lazy="dynamic")


    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('Host')
    #return '<h1>your browser is %s</h1>' % user_agent
    #return redirect('http://www.baidu.com')
    return render_template('user.html',name = name)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',name = session.get('name'),form = form,known = session.get('known',False))

if __name__ == '__main__':
    app.run()
