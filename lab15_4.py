# GITHUB LINK: https://github.com/jnav06/cst205-lab15

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")

def main():
   return render_template("template-task4.html")