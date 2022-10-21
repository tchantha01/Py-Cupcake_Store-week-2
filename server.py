from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html")

@app.route("/individual_cupcake")
def individual_cupcake():
    return render_template("individual_cupcake.html")

@app.route("/cupcake_order")
def cupcake_order():
    return render_template("cupcake_order.html")






if __name__ == "__main__":
    app.run()
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")