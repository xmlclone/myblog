from flask import Flask, render_template


def init_app(app: Flask):
    @app.errorhandler(404)
    def error_404(exc):
        return render_template('error/404.html', error=f'404: {exc}')