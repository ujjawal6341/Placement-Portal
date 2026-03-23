from flask import Blueprint, render_template, request, redirect, session
from models import Student, Company, Admin, db

auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    return render_template("index.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        student = Student.query.filter_by(email=email, password=password).first()
        company = Company.query.filter_by(email=email, password=password).first()
        admin = Admin.query.filter_by(username=email, password=password).first()

        if student:
            session["student_id"] = student.id
            return redirect("/student/dashboard")

        if company and company.approval_status == "Approved":
            session["company_id"] = company.id
            return redirect("/company/dashboard")

        if admin:
            session["admin_id"] = admin.id
            return redirect("/admin/dashboard")

    return render_template("login.html")

@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/login")