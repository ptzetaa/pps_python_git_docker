from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hello_world():
    frase = frotar(1)[0]
    return f"<html><body>{frase}</body></html>"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def frotar_endpoint(n_frases):
    if n_frases > 0:
        frases = frotar(n_frases)
        return jsonify({"frases": frases})
    else:
        return "Número de frases debe ser mayor a 0"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
