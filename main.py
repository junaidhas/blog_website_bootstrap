from flask import Flask,render_template
import requests

app = Flask(__name__)

NPOINT_data = requests.get("https://api.npoint.io/a04f5e705ee5ff9ef273").json()


@app.route('/')
def get_all_posts():
    return render_template("index.html",all_posts = NPOINT_data)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id_num>")
def read_blog(id_num):
    requested_post = None
    for blog_post in NPOINT_data:
        if blog_post["id"] == id_num:
            requested_post = blog_post

    return render_template("post.html",post = requested_post)


if __name__ =="__main__":
    app.run(debug=True)
