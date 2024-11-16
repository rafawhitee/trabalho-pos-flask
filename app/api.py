import pandas as pd
from flask import Flask, request, jsonify
from services.estatistica_service import EstatisticaService
from services import PartidaService

app = Flask(__name__)

estatistica_service = EstatisticaService()
partida_service = PartidaService()

@app.route('/api/record/csv', methods=['POST'])
def update_dataframe():
    file = request.files['file']
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Somente CSV é permitido"}), 400
    return jsonify(partida_service.update_dataframe(pd.read_csv(file)))

@app.route('/api/record/<id>', methods=['GET'])
def find_by_id(id):
    return jsonify(partida_service.find_by_id(int(id)))

@app.route('/api/statistics', methods=['GET'])
def statistics():
    return jsonify(estatistica_service.statistics())

@app.route('/api/team/<team>', methods=['GET'])
def find_all_by_team(team):
    return jsonify(partida_service.find_all_by_team(team))

if __name__ == '__main__':
    app.run(debug=True)