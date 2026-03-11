from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="../Frontend", static_url_path="")
CORS(app)

usuarios = [
    {"email": "admin", "password": "1234", "rol": "Administrador"},
    {"email": "cliente", "password": "abcd", "rol": "Cliente"}
]

@app.route("/")
def home():
    return send_from_directory("../Frontend", "login.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    for user in usuarios:
        if user["email"] == email and user["password"] == password:
            return jsonify({
                "status": "ok",
                "user": user["email"],
                "rol": user["rol"]
            })

    return jsonify({
        "status": "error",
        "message": "Credenciales incorrectas"
    }), 401

if __name__ == "__main__":
    app.run(debug=True)