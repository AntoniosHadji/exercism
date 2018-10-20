class SpaceAge(object):
    _seconds_in_earth_year = 31557600
    _mercury = 0.2408467
    _venus = 0.61519726
    _mars = 1.8808158
    _jupiter = 11.862615
    _saturn = 29.447498
    _uranus = 84.016846
    _neptune = 164.79132

    def __init__(self, seconds):
        self.earth_seconds = seconds
        self.earth_year = self.earth_seconds/self._seconds_in_earth_year

    def on_earth(self):
        return round(self.earth_seconds/self._seconds_in_earth_year, 2)

    def on_jupiter(self):
        return round(self.earth_year/self._jupiter, 2)

    def on_mercury(self):
        return round(self.earth_year/self._mercury, 2)

    def on_mars(self):
        return round(self.earth_year/self._mars, 2)

    def on_neptune(self):
        return round(self.earth_year/self._neptune, 2)

    def on_saturn(self):
        return round(self.earth_year/self._saturn, 2)

    def on_uranus(self):
        return round(self.earth_year/self._uranus, 2)

    def on_venus(self):
        return round(self.earth_year/self._venus, 2)

    @property
    def seconds(self):
        return self.earth_seconds
