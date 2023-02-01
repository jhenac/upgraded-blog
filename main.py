from flask import Flask, render_template, request
import requests
from datetime import date
import smtplib
import os

def send_email(name, email, phone, message):
    email_message = f"Subject:Upgraded Blog\n\nName: {name}\nEmail: {email}\n Phone:{phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiving_email,
                            msg=email_message)

#Create json in https://www.npoint.io/
posts = requests.get(url="https://api.npoint.io/dd906d71fd00e2528fde").json()

current_year = date.today().year
my_email = os.environ["EMAIL"]
my_password = os.environ["PASSWORD"]
receiving_email = os.environ["RECEIVER"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts, year=current_year)

@app.route("/post/<int:id_num>")
def get_post(id_num):
    return render_template("post.html", all_posts=posts, index=id_num, year=current_year)

@app.route("/about")
def about():
    return render_template("about.html", year=current_year)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(name=data["name"], email=data["email"], phone=data["phone"], message=data["message"])
        return render_template("contact.html", year=current_year)
    return render_template("contact.html", year=current_year)

if __name__ == "__main__":
    app.run(debug=True)