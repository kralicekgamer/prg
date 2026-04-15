import math as m

cities = [
    {"name": "Varnsdorf", "lat": 50.9110, "lon": 14.6180},
    {"name": "Rumburk", "lat": 50.9515, "lon": 14.5570},
    {"name": "Liberec", "lat": 50.7671, "lon": 15.0562},
    {"name": "Hrádek nad Nisou", "lat": 50.8528, "lon": 14.8446},
    {"name": "Děčín", "lat": 50.7816, "lon": 14.2148},
    {"name": "Ústí nad Labem", "lat": 50.6607, "lon": 14.0323},
    {"name": "Česká Kamenice", "lat": 50.7978, "lon": 14.4173},
    {"name": "Krásná Lípa", "lat": 50.9130, "lon": 14.5080},
    {"name": "Česká Lípa", "lat": 50.6855, "lon": 14.5376},
    {"name": "Nový Bor", "lat": 50.7570, "lon": 14.5560}
]

class Geo:
    def __init__(self, cities):
        self.cities = cities
        self.start = None
        self.end = None

    def _find_city(self, name):
        for city in self.cities:
            if city["name"] == name:
                return city
        return None

    def from_point(self, city_name):
        city = self._find_city(city_name)
        if city:
            self.start = (city["lat"], city["lon"])
        return self

    def to_point(self, city_name):
        city = self._find_city(city_name)
        if city:
            self.end = (city["lat"], city["lon"])
        return self

    def in_km(self):
        lat1, lon1 = self.start
        lat2, lon2 = self.end

        lat1 = m.radians(lat1)
        lon1 = m.radians(lon1)
        lat2 = m.radians(lat2)
        lon2 = m.radians(lon2)

        a = m.sin((lat2 - lat1) / 2)**2 \
            + m.cos(lat1) * m.cos(lat2) * m.sin((lon2 - lon1) / 2)**2

        c = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))

        return 6371 * c

distance = Geo(cities).from_point("Varnsdorf").to_point("Liberec").in_km()
print(distance)