from flask import Flask, render_template, request, jsonify
from cs50 import SQL

db = SQL("sqlite:///netflix_shows.db")
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get('q', '').strip()
    if q:
        shows = db.execute("SELECT * from netflix_shows where title LIKE ? LIMIT 50", "%" + q + "%")
    else:
        shows = []
    return render_template("search.html", shows=shows)


if __name__ == '__main__':
    app.run(debug=True)