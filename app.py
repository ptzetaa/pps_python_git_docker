# app.py

from flask import Flask, jsonify
from moodle import instanciar, consultar

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Llamar a la función de consulta con una frase
    cliente_mongo = instanciar()
    frase = consultar(cliente_mongo, 1)[0]
    cliente_mongo.close()

    return f"<html><body>{frase}</body></html>"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def frotar_endpoint(n_frases):
    if n_frases > 0:
        # Llamar a la función de consulta con N frases y devolver en formato JSON
        cliente_mongo = instanciar()
        frases = consultar(cliente_mongo, n_frases)
        cliente_mongo.close()
        return jsonify({"frases": frases})
    else:
        return "Número de frases debe ser mayor a 0"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
