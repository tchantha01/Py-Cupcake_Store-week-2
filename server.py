from flask import Flask, render_template, request

app = Flask(__name__)

from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

@app.route("/")
def home():
    cupcakes = get_cupcakes("cupcakes.csv")
    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("index.html", cupcakes=cupcakes, items_num=len(order), order_total=order_total)

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