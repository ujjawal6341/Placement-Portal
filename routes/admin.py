from flask import Blueprint, render_template, redirect
from models import Company, Student, Drive, Application, db

admin = Blueprint("admin", __name__)

@admin.route("/admin/dashboard")
def admin_dashboard():

    students = Student.query.count()
    companies = Company.query.count()
    drives = Drive.query.count()
    applications = Application.query.count()

    return render_template(
        "admin/dashboard.html",
        students=students,
        companies=companies,
        drives=drives,
        applications=applications
    )

@admin.route("/admin/companies")
def view_companies():

    companies = Company.query.all()

    return render_template(
        "admin/companies.html",
        companies=companies
    )

@admin.route("/approve_company/<int:id>")
def approve_company(id):

    company = Company.query.get(id)

    company.approval_status = "Approved"

    db.session.commit()

    return redirect("/admin/companies")

@admin.route("/admin/drives")
def view_drives():

    drives = Drive.query.all()

    return render_template(
        "admin/drives.html",
        drives=drives
    )

@admin.route("/approve_drive/<int:id>")
def approve_drive(id):

    drive = Drive.query.get(id)

    drive.status = "Approved"

    db.session.commit()

    return redirect("/admin/drives")

@admin.route("/admin/students")
def view_students():

    students = Student.query.all()

    return render_template(
        "admin/students.html",
        students=students
    )

@admin.route("/admin/search_students", methods=["GET","POST"])
def search_students():

    if request.method == "POST":

        keyword = request.form["keyword"]

        students = Student.query.filter(
            Student.name.contains(keyword)
        ).all()

        return render_template(
            "admin/students.html",
            students=students
        )

    return redirect("/admin/students")

@admin.route("/blacklist_student/<int:id>")
def blacklist_student(id):

    student = Student.query.get(id)

    student.active = False

    db.session.commit()

    return redirect("/admin/students")

@admin.route("/blacklist_company/<int:id>")
def blacklist_company(id):

    company = Company.query.get(id)

    company.active = False

    db.session.commit()

    return redirect("/admin/companies")

@admin.route("/admin/applications")
def all_applications():

    applications = Application.query.all()

    return render_template(
        "admin/applications.html",
        applications=applications
    )

