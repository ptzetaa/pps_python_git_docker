from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hello_world():
    frases = frotar(3)  # Prueba con 3 frases aleatorias
    return jsonify({"mensaje": "Hola mundo", "frases": frases})

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def frotar_endpoint(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
    app.run(debug=True)