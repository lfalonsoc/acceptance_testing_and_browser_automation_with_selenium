from typing import Any, List

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts: List[Any] = []


@app.route('/')
def homepage() -> str:
    return render_template('home.html')


@app.route('/blog')
def blog_page() -> str:
    return render_template('blog.html', posts=posts)


@app.route('/post', methods=['GET', 'POST'])
def add_post() -> Any:
    if request.method == 'POST':
        title: str = request.form['title']
        content: str = request.form['content']
        global posts

        posts.append({
            'title': title,
            'content': content
        })

        return redirect(url_for('blog_page'))
    return render_template('new_post.html')


@app.route('/post/<string:title>')
def see_post(title: str) -> str:
    global posts

    for post in posts:
        if post['title'] == title:
            return render_template('post.html', post=post)

    return render_template('post.html', post=None)


if __name__ == '__main__':
    app.run()
