from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")

mail = Mail(app)

projects = [
{
    "title": "ACK Note List",
    "description": "A responsive To-Do and Note List web application that allows users to create, edit, complete, and delete tasks.",
    "tech": "Python • Flask • SQLite • HTML • CSS",
    "image": "images/projects/ack-note-list.png",
    "github": "https://github.com/allamsetty-chaitanyakumar/todo_app",
    "demo": "https://ack-note-list.onrender.com",
    "features": [
        "Add and manage tasks",
        "Edit and delete notes",
        "Mark tasks as completed",
        "Responsive web interface"
    ]
},
    {
        "title": "Book Exchange Network",
        "description": "A web application designed to help users exchange books through an online platform.",
        "tech": "Python • Flask • PostgreSQL • HTML • CSS",
        "image": "images/projects/book-exchange.png",
        "github": "https://github.com/allamsetty-chaitanyakumar/book-exchange-network",
        "demo": "https://book-exchange-network.onrender.com/",
        "features": [
            "Book listing",
            "Book exchange",
            "User interaction",
            "Responsive web interface"
        ]
    },
]


@app.route("/")
def home():
    return render_template("index.html", projects=projects)

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    try:
        msg = Message(
            subject=f"Portfolio Contact from {name}",
            sender=app.config["MAIL_USERNAME"],
            recipients=["chaitanyaallamsetty9121@gmail.com"]
        )

        msg.body = f"""
New message from your portfolio website

Name: {name}
Email: {email}

Message:
{message}
"""

        mail.send(msg)

        return redirect(url_for("home") + "#contact")

    except Exception as e:
        print("Email error:", e)

        return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)