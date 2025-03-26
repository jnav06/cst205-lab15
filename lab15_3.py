# GITHUB LINK: https://github.com/jnav06/cst205-lab15

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/josue")

def main():
   return render_template("template-task3.html")