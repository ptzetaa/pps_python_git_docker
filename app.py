# app.py
from flask import Flask, jsonify, request
from bayeta import frotar, agregar_frase_auspiciosa

app = Flask(__name__)

IMAGEN_URL = "/static/panda.png"

@app.route('/')
def index():
    # Invoca la función frotar sin límite en la cantidad de frases
    resultado_frotar = frotar()

    # Retorna una frase auspiciosa aleatoria como respuesta en la ruta raíz
    return f'<img src="{IMAGEN_URL}" width="300" height="200"><h1>{resultado_frotar[0]["frase"]}</h1>'

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    resultado_frotar = frotar(n_frases)
    return jsonify({"frases": resultado_frotar})

@app.route('/frotar/add', methods=['POST'])
def agregar_frases():
    try:
        datos_json = request.get_json()
        nuevas_frases = datos_json['frases']

        for frase in nuevas_frases:
            agregar_frase_auspiciosa(frase)

        return jsonify({"mensaje": "Frases agregadas correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
