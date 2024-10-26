from flask import Flask, render_template, request, jsonify
from cs50 import SQL

db = SQL("sqlite:///shows_title.db")
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q", '')
    if q:
        shows = db.execute("SELECT * from shows_title where originalTitle LIKE ? AND CAST(startYear AS UNSIGNED) >= 2003 LIMIT 50", "%" + q + "%")
    else:
        shows = []
    return render_template("search.html", shows=shows)


if __name__ == '__main__':
    app.run(debug=True)