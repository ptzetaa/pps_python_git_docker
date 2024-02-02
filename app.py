# app.py

from flask import Flask
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def index():
    # Llama a la función frotar sin limitar la cantidad de frases
    frases_auspiciosas = frotar()

    if frases_auspiciosas:
        # Extrae la primera frase auspiciosa si la lista no está vacía
        frase_auspiciosa = frases_auspiciosas[0]['frase']
        return f"<html><body><p>Frase Auspiciosa: {frase_auspiciosa}</p></body></html>"
    else:
        return "<html><body><p>No hay frases auspiciosas disponibles</p></body></html>"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return {"frases": frases}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
