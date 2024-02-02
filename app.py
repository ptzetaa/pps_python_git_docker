from flask import Flask
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hello_world():
    frases = frotar(1)
    return jsonify({"mensaje": "Hola mundo", "frases": frases})

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def frotar_endpoint(n_frases):
    frases = frotar(n_frases)
    return "\n".join(frases)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
