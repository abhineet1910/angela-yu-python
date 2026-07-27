from flask import Flask, render_template,request
import requests
blog_url='https://api.npoint.io/674f5423f73deab1e9a7'
response = requests.get(blog_url)
data = response.json()
# print(data)
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',all_posts=data)

#
@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
