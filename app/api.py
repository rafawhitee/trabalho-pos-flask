from flask import Flask, jsonify
from repository.partida_repository import PartidaRepository

app = Flask(__name__)
partida_repository = PartidaRepository()

@app.route('/api/teste', methods=['GET'])
def teste():
    return jsonify(partida_repository.get_dataframe().head(10).to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)