from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:mypassword@database-1.ccldgbvrextx.us-east-1.rds.amazonaws.com:3306/database-1"

db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    username = request.form['Username']
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return "Done, " + username

if __name__ == '__main__':
    app.run()