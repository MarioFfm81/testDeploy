import flask
app = flask.Flask(__name__)
wsgi_app = app.wsgi_app
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>TestDeploy</h1>"

if __name__ == '__main__':
    app.run()