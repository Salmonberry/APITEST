from flask import Flask, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "ddddd"

db = SQLAlchemy(app)


@app.route('/', methods=["Get"])
def hello_world():  # put application's code here
    return 'Hello World!'


# @app.route("/bilibili")
# def bilibili():
#     return redirect()

@app.route("/test/data", methods=["POST"])
def my_post():
    try:
        my_json = request.get_json()
        age = my_json.get("age")

        if not all([my_json("age", my_json("name"))]):
            return jsonify(error="argum less")

        age += 10

        return jsonify(name=my_json.get("name"), age=age)
    except Exception as e:

        return jsonify(error="error")


if __name__ == '__main__':
    app.run()
