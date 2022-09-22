from flask import Flask, render_template

def init_app(app: Flask):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/blog/view/<int:blog_id>')
    def blog_view(blog_id: int):
        return render_template('blogview.html', blog_id=blog_id)

    @app.route('/blog/udpate/<int:blog_id>')
    def blog_edit(blog_id: int):
        return render_template('blogupdate.html', blog_id=blog_id)