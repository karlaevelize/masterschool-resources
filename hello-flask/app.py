import json
from flask import Flask, render_template

app = Flask(__name__)

# 1. Import the json file
# 2. Send the json as a variable
# 3. Render the posts on the screen

with open('posts.json') as file:
    posts = json.load(file)

# Home route
@app.route('/')
def home():
    return render_template('index.html', name="Karla", posts=posts)

# About route
@app.route('/about')
def about():
    return 'This is about page'

# Variable route
@app.route('/post/<int:post_id>')
def post(post_id):
    return f'This is post {post_id}'
