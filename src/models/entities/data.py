class Data():


    def __init__(self, id, station_id, temperature=None, humidity=None, pressure=None, timestamp=None) -> None:
        self.id = id
        self.station_id = station_id
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.timestamp = timestamp


    def to_JSON(self):
        return {
            'id': self.id,
            'station_id': self.station_id,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'pressure': self.pressure,
            'timestamp': self.timestamp
        }