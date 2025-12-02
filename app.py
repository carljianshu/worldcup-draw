# app.py
from flask import Flask, jsonify, render_template
from fifaworldcupdraw import do_full_draw  # or main, but do_full_draw returns the list clearly

app = Flask(__name__)

@app.route("/")
def index():
    # Serve the HTML page
    return render_template("index.html")

@app.route("/api/draw", methods=["GET"])
def api_draw():
    """
    Call your World Cup draw simulator and return JSON like:
    [
      ["Brazil","Italy","Norway","Morocco"],
      ["Mexico","Iran","Algeria","Turkey"],
      ...
    ]
    """
    result = do_full_draw()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
