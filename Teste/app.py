from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# =========================
# ESTADO DO JOGO
# =========================

player = {
    "HP": 100,
    "INT": 10,
    "FOR": 8,
    "DEF": 5
}

# =========================
# ROTAS DO SITE
# =========================

@app.route("/")
def index():
    return render_template("index.html", player=player)

@app.route("/atacar")
def atacar():
    player["HP"] -= 10
    return redirect(url_for("index"))

@app.route("/curar")
def curar():
    player["HP"] += 10
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    player["HP"] = 100
    return redirect(url_for("index"))

# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    app.run(debug=True)