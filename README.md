# Placement Portal (Naukri Shala)

## Overview

**Placement Portal (Naukri Shala)** is a web-based placement management system designed to streamline and centralize the campus recruitment process. The platform bridges the gap between students, recruiters, and administrators by providing a single interface for managing placement activities efficiently.

Traditional placement processes often rely on spreadsheets, emails, and manual coordination, leading to delays, communication gaps, and limited visibility into application status. Naukri Shala addresses these challenges by offering an organized, role-based system that simplifies the entire recruitment lifecycle.

---

## Problem Statement

Many educational institutions face challenges in managing campus placements due to:

* Delayed communication between stakeholders
* Manual tracking of student applications
* Lack of centralized placement information
* Difficulty in managing recruitment drives
* Limited transparency in the hiring process

Naukri Shala aims to eliminate these inefficiencies through a scalable and user-friendly placement management platform.

---

## Features

### Student Module

* Student registration and authentication
* View available placement drives
* Apply for job opportunities
* Track application status
* Access personalized dashboard

### Company Module

* Company registration and profile management
* Create and manage recruitment drives
* View and review student applications
* Shortlist candidates
* Update recruitment status

### Administrator Module

* Manage student and company accounts
* Approve or monitor company registrations
* Oversee all placement activities
* Monitor platform usage and recruitment statistics
* Ensure smooth operation of the placement process

---

## Tech Stack

| Component       | Technology                          |
| --------------- | ----------------------------------- |
| Backend         | Flask                               |
| Database        | SQLAlchemy, SQLite                  |
| Frontend        | HTML5, Bootstrap 5, Jinja2          |
| Authentication  | Flask Session / JWT (if applicable) |
| ORM             | SQLAlchemy                          |
| Version Control | Git & GitHub                        |

---

## System Architecture

The application follows a modular Flask architecture to ensure maintainability and scalability.

```text
Placement Portal (Naukri Shala)
│
├── Students
│   ├── Register
│   ├── View Drives
│   ├── Apply for Jobs
│   └── Track Applications
│
├── Companies
│   ├── Register
│   ├── Create Drives
│   ├── Review Applications
│   └── Shortlist Candidates
│
└── Administrators
    ├── Manage Users
    ├── Monitor Drives
    └── Oversee Recruitment Process
```

---

## Project Objective

The primary objective of this project is to provide:

* A centralized placement management system.
* Efficient communication between students, recruiters, and administrators.
* Transparent application tracking.
* Simplified recruitment drive management.
* Improved administrative control and reporting.

---

## Development Approach

The application was developed using the Flask web framework with a modular design pattern.

* Backend services are implemented using Flask and SQLAlchemy.
* Dynamic web pages are rendered using Jinja2 templates.
* Bootstrap is used to create a responsive and modern user interface.
* Database interactions are managed through SQLAlchemy ORM.
* The application follows a role-based access model for enhanced security and maintainability.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/naukri-shala.git

# Move into the project directory
cd naukri-shala

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

---

## Future Enhancements

* Resume parsing using AI/ML
* Email notifications for application updates
* Analytics dashboard for administrators
* Advanced filtering and search functionality
* Interview scheduling system
* Integration with external job platforms
* Multi-factor authentication (MFA)

---

## AI / LLM Usage Declaration

This project utilized AI assistance responsibly and transparently.

### AI Tools Used

* ChatGPT (GPT-5)

### Areas of Assistance

* Improving Flask project structure and modularization.
* Debugging SQLAlchemy-related issues.
* Enhancing documentation and README formatting.
* Providing guidance on template organization and best practices.

### Usage Estimate

AI assistance contributed approximately **10–15%** of the overall development effort and was primarily used for guidance, debugging support, and documentation improvements.

> All core functionalities, application logic, database design, testing, debugging, and final integration were implemented and validated manually by the developer.

---

## Author

**Ujjawal Bhardwaj**

* IIT Madras BS Degree (Data Science and Applications)
* Ethical Hacker & Security Enthusiast
* Full-Stack Developer

---

## License

This project is developed for academic and educational purposes. Feel free to explore, learn, and contribute.

---

> *"Simplifying campus placements, one application at a time."*
