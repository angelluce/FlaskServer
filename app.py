from flask import Flask, render_template
import sqlite3
import json
from werkzeug.exceptions import abort

app = Flask(__name__)

# funciones para conexiones a la db

def get_db_connection():
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_db_connection_by_cursor():
    conn = sqlite3.connect('db/database.db')
    return conn.cursor()

# funciones para consultas a la db (ui)

def get_all_posts_ui():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    if post is None:
        abort(404)
    return posts

def get_post_by_id_ui(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# funciones para consultas a la db (post)

def get_all_posts_json():
    cursor = get_db_connection_by_cursor()
    cursor.execute('SELECT * FROM posts')
    data = cursor.fetchall()
    return json.dumps(data)

def get_post_by_id_json(post_id):
    cursor = get_db_connection_by_cursor()
    cursor.execute('SELECT * FROM posts WHERE id = ?', [post_id])
    data = cursor.fetchall()
    return json.dumps(data)

# funciones para respuestas (ui)

@app.route('/ui')
def index():
    posts = get_all_posts_ui()
    return render_template('index.html', posts=posts)

@app.route('/ui/<int:post_id>')
def post(post_id):
    post = get_post_by_id_ui(post_id)
    return render_template('post.html', post=post)

# funciones para respuestas (post)

@app.route('/json')
def indexJson():
    return get_all_posts_json()

@app.route('/json/<int:post_id>')
def postJson(post_id):
    return get_post_by_id_json(post_id)

# función index (post)

@app.route("/")
def home():
    return {
        'mensaje': '¡Flask está ejecutándose!',
        'estado': True,
    }


if __name__ == "__main__":
    app.run(debug=True)
