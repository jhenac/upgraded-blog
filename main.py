from flask import Flask, render_template
import requests
from datetime import date

#Create json in https://www.npoint.io/
posts = requests.get(url="https://api.npoint.io/dd906d71fd00e2528fde").json()

app = Flask(__name__)

@app.route("/")
def home():
    current_year = date.today().year
    return render_template("index.html", all_posts=posts, year=current_year)

@app.route("/post/<int:id_num>")
def get_post(id_num):
    return render_template("post.html", all_posts=posts, index=id_num)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)