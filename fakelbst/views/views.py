import urllib
from fakelbst import app
from flask import  render_template, Blueprint, redirect, url_for
from fakelbst.models import models
from fakelbst.models.mark import Mark
from flask.views import MethodView
from fakelbst.models.auth import *

projects = Blueprint('fakelbst', __name__, template_folder="templates")

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/mark')
def markpage():
    marks = Mark.objects.all()
    return render_template('mark.html', marks=marks)

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

@app.route('/secret')
@requires_auth
def secret_page():
    marks = Mark.objects.all()
    return render_template('secret_page.html', marks=marks)

@app.route('/add_mark', methods=['POST'])
def add_mark():
    import BeautifulSoup
    url = request.form['weblink']
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))
    title = soup.title.string
    newMark = Mark(title=title, link=url, tag_id=1)
    newMark.save()
    return redirect(url_for("secret_page"))


'''
@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")
'''
'''
@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()
'''
'''
@app.before_request
def before_request():
    g.user = None
    if 'tag_id' in session:
        g.user = query_db('select * from user where tag_id = ?',
                          [session['user_id']], one=True)
'''

