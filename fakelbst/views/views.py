from fakelbst import app
from flask import  render_template, Blueprint
from fakelbst.models import models

projects = Blueprint('fakelbst', __name__)
app.config.from_pyfile('config.cfg', silent = True)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/mark')
def markpage():
    #if not g.user:
        #return redirect(url_for('public_mark'))
    return render_template('mark.html', weblink=models.query_db('''select * from mark '''))

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/labs')
def labpage():
    return render_template('labs.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/labs/forcedirected')
def forcedirected():
    return render_template('/labs/ForceDirected.html')

@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")

@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

'''
@app.before_request
def before_request():
    g.user = None
    if 'tag_id' in session:
        g.user = query_db('select * from user where tag_id = ?',
                          [session['user_id']], one=True)
'''

