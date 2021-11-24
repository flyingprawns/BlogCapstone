from flask import Flask, render_template
import requests

app = Flask(__name__)

# ------- Store blog posts ------- #
response = requests.get("https://api.npoint.io/88292704844daa394f39")
response.raise_for_status()
blog_posts = response.json()


# ------- Flask functions ------- #
@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/post/<post_id>')
def get_post(post_id):
    return render_template("post.html", post=blog_posts[int(post_id)-1])


if __name__ == "__main__":
    app.run(debug=True)
