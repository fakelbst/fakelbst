#!/usr/bin/env python


import time
import sys
import os
import json
from views import views
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from flask import Flask, Request, Response, session, render_template, url_for, g, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash

application = app = Flask('wsgi')

# configuration
DATABASE = './mark.db'
PER_PAGE = 30
DEBUG = True


app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/mark')
def markpage():
    return render_template('mark.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/lab')
def labpage():
    return render_template('lab.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


'''
@app.route('/mongo')
def mongotest():
    from pymongo import Connection
    uri = mongodb_uri()
    conn = Connection(uri)
    coll = conn.db['ts']
    coll.insert(dict(now=int(time.time())))
    last_few = [str(x['now']) for x in coll.find(sort=[("_id", -1)], limit=10)]
    body = "\n".join(last_few)
    return Response(body, content_type="text/plain;charset=UTF-8")
'''
'''
def mongodb_uri():
    local = os.environ.get("MONGODB", None)
    if local:
        return local
    services = json.loads(os.environ.get("VCAP_SERVICES", "{}"))
    if services:
        creds = services['mongodb-1.8'][0]['credentials']
        uri = "mongodb://%s:%s@%s:%d/%s" % (
            creds['username'],
            creds['password'],
            creds['hostname'],
            creds['port'],
            creds['db'])
        print >> sys.stderr, uri
        return uri
    else:
        raise Exception, "No services configured"
'''

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db

@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

@app.before_request
def before_request():
    g.user = None
    if 'tag_id' in session:
        g.user = query_db('select * from user where tag_id = ?',
                          [session['user_id']], one=True)

def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv
  

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
