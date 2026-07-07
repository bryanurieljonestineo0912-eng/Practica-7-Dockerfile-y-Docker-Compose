from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conexion = mysql.connector.connect(
            host="db",
            user="root",
            password="123456",
            database="practica7"
        )

        return "Hola Mundo. Aquí Bryan Jones,Conexion a MySQL exitosa."

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
