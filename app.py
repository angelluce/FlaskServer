from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    if post is None:
        abort(404)
    return posts

def get_post_by_id(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/posts')
def index():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:post_id>')
def post(post_id):
    post = get_post_by_id(post_id)
    return render_template('post.html', post=post)

@app.route("/")
def home():
    return {
        'mensaje': '¡Flask está ejecutándose!',
        'estado': True,
    }

if __name__ == "__main__":
    app.run(debug=True)
