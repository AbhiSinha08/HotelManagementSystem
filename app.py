from flask import Flask, render_template, request
import os

os.chdir(__file__.replace(os.path.basename(__file__), ''))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

app.debug = True
if __name__ == '__main__':
    app.run()