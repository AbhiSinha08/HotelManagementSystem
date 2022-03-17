# Main server app

from flask import Flask, render_template, request
import os
import database

os.chdir(__file__.replace(os.path.basename(__file__), ''))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()