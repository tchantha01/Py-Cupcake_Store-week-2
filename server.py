from flask import Flask, render_template, request

app = Flask(__name__)

from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

@app.route("/")
def home():
    cupcakes = get_cupcakes("cupcakes.csv")
    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("index.html", cupcakes=cupcakes, items_num=len(order), order_total=order_total)

@app.route("/individual_cupcake/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    
    if cupcake:
        return render_template("individual_cupcake.html", cupcake=cupcake)
    else:
        return "Sorry cupcake not found."

@app.route("/cupcake_order")
def cupcake_order():
    cupcakes = get_cupcakes("orders.csv")
    
    cupcakes_counted = []
    cupcake_set = set()
    
    for cupcake in cupcakes:
        cupcake_set.add(cupcake["name"], cupcake["price"], cupcake.count(cupcake))
    
    
    return render_template("cupcake_order.html", cupcakes=cupcake_set)


if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")
    app.env = "development"
   