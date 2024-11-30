from cs50 import SQL
from flask import Flask, render_template, request, redirect
from livereload import Server

app = Flask(__name__)

db = SQL("sqlite:///database.db")


@app.route("/")
def home():
    return render_template("page.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()

    print(f"Received username: '{username}', password: '{password}'")

    rows = db.execute("SELECT * FROM users WHERE username = ?", username)
    print(f"Found user: {rows}")

    if rows and rows[0]["password"] == password:
        assets = db.execute("select * from assets")
        print(assets)
        return render_template("assets.html", assets=assets)
    else:
        return "Invalid credentials, try again."


@app.route("/delete_asset/<int:asset_id>", methods=["POST"])
def delete_asset(asset_id):
    db.execute("delete from assets where asset_id = ?", asset_id)
    assets = db.execute("select * from assets")
    return render_template("assets.html", assets=assets)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        asset_name = request.form.get("asset_name")
        asset_category = request.form.get("asset_category")
        asset_value = request.form.get("asset_value")
        db.execute(
            "insert into assets (asset_name, category, value) values (?,?,?)",
            asset_name,
            asset_category,
            asset_value,
        )
        assets = db.execute("select * from assets")
        return render_template("assets.html", assets=assets)


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch("templates/*.html")
    server.watch("static/*.*")
    server.serve(port=5000, debug=True)
