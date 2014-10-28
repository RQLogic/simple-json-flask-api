from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/')
def hello_world():
    return {'hello': 'world'}

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')
