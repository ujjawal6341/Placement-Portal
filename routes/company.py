from flask import Blueprint, render_template, request, redirect, session
from models import Company, Drive, Application, db
from models import Student
from sqlalchemy import func

company = Blueprint("company", __name__)


@company.route("/register_company", methods=["GET","POST"])
def register_company():

    if request.method == "POST":

        name = request.form["company_name"]
        email = request.form["email"]
        website = request.form["website"]
        password = request.form["password"]

        new_company = Company(
            company_name=name,
            email=email,
            website=website,
            password=password
        )

        db.session.add(new_company)
        db.session.commit()

        return redirect("/login")

    return render_template("register_company.html")

@company.route("/company/dashboard")
def company_dashboard():

    company_id = session.get("company_id")

    drives = Drive.query.filter_by(company_id=company_id).all()

    drive_counts = {}

    for drive in drives:

        count = Application.query.filter_by(drive_id=drive.id).count()

        drive_counts[drive.id] = count

    return render_template(
        "company/dashboard.html",
        drives=drives,
        drive_counts=drive_counts
    )

@company.route("/create_drive", methods=["GET","POST"])
def create_drive():

    if request.method == "POST":

        title = request.form["title"]
        desc = request.form["description"]
        eligibility = request.form["eligibility"]
        deadline = request.form["deadline"]

        drive = Drive(
            company_id=session.get("company_id"),
            job_title=title,
            job_description=desc,
            eligibility=eligibility,
            deadline=deadline
        )

        db.session.add(drive)
        db.session.commit()

        return redirect("/company/dashboard")

    return render_template("company/create_drive.html")

@company.route("/applications/<int:drive_id>")
def view_applications(drive_id):

    if not session.get("company_id"):
        return redirect("/login")

    applications = Application.query.filter_by(drive_id=drive_id).all()

    students = {}

    for app in applications:
        student = Student.query.get(app.student_id)
        students[app.id] = student

    return render_template(
        "company/applications.html",
        applications=applications,
        students=students
    )

@company.route("/update_status/<int:app_id>/<status>")
def update_status(app_id, status):

    app = Application.query.get(app_id)

    app.status = status

    db.session.commit()

    return redirect(request.referrer)

@company.route("/update_application/<int:app_id>/<status>")
def update_application(app_id, status):

    application = Application.query.get(app_id)

    application.status = status

    db.session.commit()

    return redirect(request.referrer)