from flask import Flaks, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return "HUZZAH"