from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

@app.route("/")
def home():
    intentos = 0
    conectado = False
    error_mensaje = ""

    while intentos < 5 and conectado == False:
        try:
            conexion = mysql.connector.connect(
                host="db",
                user="root",
                password="123456",
                database="practica7"
            )
            conexion.close()
            conectado = True
        except Exception as e:
            error_mensaje = str(e)
            intentos = intentos + 1
            time.sleep(3)

    if conectado == True:
        return "Hola Mundo. Aqui Bryan Jones, Conexion a MySQL exitosa."
    else:
        return "Error: " + error_mensaje

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
