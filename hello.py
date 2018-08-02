from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

Bootstrap(app)


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
def idnex():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name  = form.name.data
        form.name.data = ''
    return render_template('index.html',name = name,form = form)

if __name__ == '__main__':
    app.run()
