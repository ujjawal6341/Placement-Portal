from flask import Flask
from config import Config
from models import db

from routes.auth import auth
from routes.admin import admin
from routes.student import student
from routes.company import company

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(student)
app.register_blueprint(company)

if __name__ == "__main__":
    app.run(debug=True)