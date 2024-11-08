from flask import Flask, jsonify
from flask_cors import CORS  # Importando CORS

app = Flask(__name__)
CORS(app, origins="*")  # Permite todas as origens, pode restringir se necessário

@app.route('/dados', methods=['GET'])
def get_dados():
    try:
        # Lendo o conteúdo do arquivo
        with open('dados_pedometro.txt', 'r') as file:
            dados = file.readlines()

        # Retornando os dados como resposta JSON
        return jsonify(dados)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Altere para '0.0.0.0' para permitir conexões externas
