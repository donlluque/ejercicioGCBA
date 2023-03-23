from database.db import get_connection
from .entities.station import Station
from .entities.data import Data
import json

class StationsModel():

    # INFO GENERAL DE TODAS LAS ESTACIONES
    @classmethod
    def get_stations(cls):
        try:
            connection = get_connection()
            stations = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, ST_AsGeoJSON(location), altitude, instalation FROM weather_stations ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    # Obtener las coordenadas de longitud y latitud del objeto GeoJSON
                    coordinates = json.loads(row[2])['coordinates']
                    longitude = coordinates[0]
                    latitude = coordinates[1]

                    # Mostrar la estación con las coordenadas convertidas
                    station = Station(row[0], row[1], {'longitude': longitude, 'latitude': latitude}, row[3], row[4])
                    stations.append(station.to_JSON())

            connection.close()
            return stations

        except Exception as ex:
            raise Exception(ex)


    # INFO DETALLADA DE 1 ESTACION
    @classmethod
    def get_station(cls, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                # Obtener la información de la estación y su correspondiente información de datos
                cursor.execute("""
                    SELECT s.id, s.name, ST_AsGeoJSON(s.location), s.altitude, s.instalation,
                    d.id, d.station_id, d.temperature, d.humidity, d.pressure, d.timestamp
                    FROM weather_stations s
                    LEFT JOIN weather_data d ON s.id = d.station_id
                    WHERE s.id = %s
                    ORDER BY name DESC
                """, (id,))
                rows = cursor.fetchall()

                if rows:
                    # Crear la estación y agregar sus datos
                    station_data = []
                    for row in rows:
                        if row[5] is not None:
                            data = Data(row[5], row[6], row[7], row[8], row[9], row[10])
                            station_data.append(data)
                    
                    # Obtener las coordenadas de latitud y longitud del objeto JSON de la ubicación
                    coordinates = json.loads(rows[0][2])['coordinates']
                    longitude = coordinates[0]
                    latitude = coordinates[1]

                    station = Station(rows[0][0], rows[0][1], {"latitude": latitude, "longitude": longitude}, rows[0][3], rows[0][4])
                    station.add_data(station_data)

                    # Convertir el objeto Station a formato JSON
                    station_json = station.to_JSON()

                else:
                    station_json = None

            connection.close()
            return station_json

        except Exception as ex:
            raise Exception(ex)
        

    # CREAR UNA ESTACION
    @classmethod
    def add_station(cls, station):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO weather_stations (id, name, location, altitude, instalation) 
                                VALUES (%s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326), %s, %s)""", 
                                (station.id, station.name, station.location["longitude"], 
                                station.location["latitude"], station.altitude, station.instalation))

                affected_rows = cursor.rowcount
                connection.commit()               


            connection.close()

            return affected_rows

        except Exception as ex:
            raise Exception(ex)
        

    # BORRAR UNA ESTACION
    @classmethod
    def delete_station(cls, station):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM weather_stations WHERE id = %s", (station.id))

                affected_rows = cursor.rowcount
                connection.commit()               

            connection.close()

            return affected_rows

        except Exception as ex:
            raise Exception(ex)