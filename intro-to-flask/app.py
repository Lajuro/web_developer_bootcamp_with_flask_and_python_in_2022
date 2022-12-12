from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'jinja_intro.html',
        name='Roberto',
        template_name='Jinja2'
    )
