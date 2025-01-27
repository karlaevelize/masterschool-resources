# Goals for today: Create a Blog with Flask
#
# 1. Create a Homepage with all the blog posts
# 2. Create a page for each blog post

import json
from flask import Flask, render_template

# Assign blog posts to variable
with open('posts.json') as file:
    posts = json.load(file)

app = Flask(__name__)

# Route for the homepage: all blog posts
@app.route('/')
def home():
    return render_template('index.html', name="Karla", posts=posts)

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for each blog post
@app.route('/post/<int:post_id>')
def post(post_id):
    return f'This is post {post_id}'