from flask import Flask, jsonify, render_template
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hello_world():
    frase = frotar(1)[0]
    return render_template('index.html', frase=frase)

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def frotar_endpoint(n_frases):
    if n_frases == 1:
        frases = frotar(n_frases)
        return jsonify({"frases": frases})
    else:
        frase = frotar(1)[0]
        return render_template('index.html', frase=frase)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
