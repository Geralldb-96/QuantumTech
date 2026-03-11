from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder="../Frontend", static_url_path="")
CORS(app)

usuarios = [
    {"email": "admin", "password": "1234", "rol": "Administrador"},
    {"email": "cliente", "password": "abcd", "rol": "Cliente"}
]

# Ruta principal -> abre index.html
@app.route("/")
def home():
    return app.send_static_file("index.html")


# Ruta para login
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


# Permite abrir login.html directamente
@app.route("/login.html")
def login_page():
    return app.send_static_file("login.html")


if __name__ == "__main__":
    app.run(debug=True)