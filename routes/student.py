from flask import Blueprint, render_template, request, redirect, session
from models import Student, Drive, Application, db

student = Blueprint("student", __name__)


@student.route("/register_student", methods=["GET","POST"])
def register_student():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        new_student = Student(
            name=name,
            email=email,
            password=password
        )

        db.session.add(new_student)
        db.session.commit()

        return redirect("/login")

    return render_template("register_student.html")


@student.route("/student/dashboard")
def student_dashboard():

    drives = Drive.query.filter_by(status="Approved").all()

    return render_template("student/dashboard.html", drives=drives)

@student.route("/apply/<int:drive_id>")
def apply(drive_id):

    student_id = session.get("student_id")

    if not student_id:
        return redirect("/login")

    existing = Application.query.filter_by(
        student_id=student_id,
        drive_id=drive_id
    ).first()

    if existing:
        return "You already applied for this drive"

    new_application = Application(
        student_id=student_id,
        drive_id=drive_id,
        status="Applied"
    )

    db.session.add(new_application)
    db.session.commit()

    return redirect("/student/applications")

@student.route("/student/applications")
def student_applications():

    student_id = session.get("student_id")

    apps = Application.query.filter_by(student_id=student_id).all()

    return render_template(
        "student/applications.html",
        applications=apps
    )

@student.route("/student/drives")
def student_drives():

    drives = Drive.query.filter_by(status="Approved").all()

    return render_template(
        "student/drives.html",
        drives=drives
    )