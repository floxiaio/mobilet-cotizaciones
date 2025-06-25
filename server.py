# Este archivo es opcional y solo necesario si se requiere un backend.
# Se puede implementar un servidor simple con Flask si es necesario.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    # Aquí se procesaría el formulario de contacto
    return jsonify({"message": "Formulario recibido"}), 200

if __name__ == '__main__':
    app.run(debug=True)