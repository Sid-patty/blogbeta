from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory database (you can later replace it with a proper database)
posts = [
    {"id": 1, "title": "Welcome to my blog", "content": "This is the first blog post."},
    {"id": 2, "title": "Flask is amazing", "content": "Flask allows you to create apps quickly and easily."}
]

# Home Page
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

# View Single Post
@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post) if post else "Post not found", 404

# Create New Post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {"id": len(posts) + 1, "title": title, "content": content}
        posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True)
