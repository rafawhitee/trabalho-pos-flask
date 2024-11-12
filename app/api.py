from flask import Flask, jsonify
from services import PartidaService

app = Flask(__name__)
partida_service = PartidaService()

@app.route('/api/statistics', methods=['GET'])
def statistics():
    return jsonify(partida_service.get_dataframe().head(10).to_dict(orient='records'))

@app.route('/api/record/<id>', methods=['GET'])
def find_by_id(id):
    return jsonify(partida_service.find_by_id(int(id)))

if __name__ == '__main__':
    app.run(debug=True)