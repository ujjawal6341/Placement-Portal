from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    resume = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    website = db.Column(db.String(200))
    password = db.Column(db.String(100))
    approval_status = db.Column(db.String(20), default="Pending")
    active = db.Column(db.Boolean, default=True)


class Drive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    job_title = db.Column(db.String(100))
    job_description = db.Column(db.Text)
    eligibility = db.Column(db.String(200))
    deadline = db.Column(db.String(50))
    status = db.Column(db.String(20), default="Pending")


class Application(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

    drive_id = db.Column(db.Integer, db.ForeignKey("drive.id"))

    application_date = db.Column(db.DateTime, default=datetime.utcnow)

    status = db.Column(db.String(50), default="Applied")