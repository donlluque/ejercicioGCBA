from flask import Blueprint, jsonify, request

# Entities
from models.entities.station import Station
# Models
from models.stationsModel import StationsModel

main = Blueprint('stations_blueprint', __name__)

# Routes
@main.route('/')
def get_stations():
    try:
        stations = StationsModel.get_stations()
        return jsonify(stations)

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_station(id):
    try:
        station = StationsModel.get_station(id)
        if station != None:
            return jsonify(station)
        else:
            return jsonify({'message': 'No se ha encontrado la Estación'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/add', methods=['POST'])
def add_station():
    try:
        name = request.json["name"],
        location = request.json["location"],
        altitude = int(request.json["altitude"]),
        instalation = request.json["instalation"],

        station=Station(name, location, altitude, instalation)

        affected_rows = StationsModel.add_station(station)

        if affected_rows == 1:
            return jsonify(station.id)
        else:
            return jsonify({'message': 'Error al crear Estacion'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/delete/<id>', methods=['DELETE'])
def delete_station(id):
    try:
        station=Station(id)

        affected_rows = StationsModel.delete_station(station)

        if affected_rows == 1:
            return jsonify(station.id)
        else:
            return jsonify({'message': 'Error al borrar Estacion'}), 404
        

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500