from utils.DateFormat import DateFormat

class Station:
    def __init__(self, id, name=None, location=None, altitude=None, instalation=None):
        self.id = id
        self.name = name
        self.location = location
        self.altitude = altitude
        self.instalation = instalation
        self.data = []

    def add_data(self, data):
        self.data = data

    def to_JSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "altitude": self.altitude,
            "instalation": DateFormat.convert_date(self.instalation),
            "data": [d.to_JSON() for d in self.data]
        }
