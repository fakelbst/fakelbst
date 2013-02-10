from flask import Flask
import fakelbst
#app = Flask(__name__)
app = fakelbst.app
'''
@app.route("/")
def hello():
    return "Hello World!"
'''
if __name__ == "__main__":
    app.run()

