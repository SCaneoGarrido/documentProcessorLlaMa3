from flask import Flask, render_template, jsonify #type: ignore

app = Flask(__name__, template_folder="templates", static_folder="static")


# renderizador
@app.route("/")
def home():
  return render_template("index.html")


if __name__ == "__main__":
  app.run(debug=True)