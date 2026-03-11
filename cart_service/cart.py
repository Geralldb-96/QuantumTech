from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cart = []

@app.route("/cart/add", methods=["POST"])
def add_product():

    data = request.json

    cart.append(data)

    return jsonify({
        "status": "ok",
        "cart": cart
    })


@app.route("/cart", methods=["GET"])
def get_cart():

    return jsonify(cart)


@app.route("/cart/clear", methods=["DELETE"])
def clear_cart():

    cart.clear()

    return jsonify({
        "status": "cart cleared"
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)