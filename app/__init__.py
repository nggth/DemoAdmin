from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app.secret_key = "b'1I\xa0\xfb\xd7\x95\x18\x1a\xdeG\x86O~\x01c_'"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345@localhost/loginadmindb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

admin = Admin(app=app, name="Quan ly ban hang", template_mode="bootstrap3")

login = LoginManager(app=app)