from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
@app.route('/')
@app.route('/user/<name>')
def index(name):
    user_agent = request.headers.get('Host')
    #return '<h1>your browser is %s</h1>' % user_agent
    #return redirect('http://www.baidu.com')
    return render_template('user.html',name = name)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
