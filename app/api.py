from flask import Flask, jsonify
from services.estatistica_service import EstatisticaService
from services import PartidaService

app = Flask(__name__)

estatistica_service = EstatisticaService()
partida_service = PartidaService()

@app.route('/api/statistics', methods=['GET'])
def statistics():
    return jsonify(estatistica_service.statistics())

@app.route('/api/record/<id>', methods=['GET'])
def find_by_id(id):
    return jsonify(partida_service.find_by_id(int(id)))

if __name__ == '__main__':
    app.run(debug=True)