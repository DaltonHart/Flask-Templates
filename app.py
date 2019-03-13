from flask import Flask, g
from flask import render_template, flash, redirect, url_for
import json


DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'


@app.route('/')
def index():
    with open('subs.json') as json_data:
        subs = json.load(json_data)
        return render_template('subs.html', subs=subs)


@app.route('/r')
@app.route('/r/<sub>')
def r(sub=None):
    sub_id = int(sub)
    with open('subs.json') as json_data:
        subs = json.load(json_data)
        if id == None:
            return render_template('subs.html', subs=subs)
        else:
            return render_template('sub.html', sub=subs[sub_id])


@app.route('/posts')
@app.route('/posts/<id>')
def posts(id=None):
    post_id = int(id)
    with open('posts.json') as json_data:
        posts = json.load(json_data)
        if id == None:
            return render_template('posts.html', posts=posts)
        else:
            return render_template('post.html', post=posts[post_id])


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
