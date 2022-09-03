class Rodovia:
    def __init__(self, identi=None, concessionaria=None, sp=None, sentido=None,
                 municipio=None, latitude=None, longitude=None, evento=None):
        self._identi = identi
        self._concessionaria = concessionaria
        self._sp = sp
        self._sentido = sentido
        self._municipio = municipio
        self._latitude = latitude
        self._longitude = longitude
        self._evento = evento

    @property
    def identi(self):
        return self._identi

    @identi.setter
    def identi(self, identi):
        self._identi = identi

    @property
    def concessionaria(self):
        return self._concessionaria

    @concessionaria.setter
    def concessionaria(self, concessionaria):
        self._concessionaria = concessionaria

    @property
    def sp(self):
        return self._sp

    @sp.setter
    def sp(self, sp):
        self._sp = sp

    @property
    def sentido(self):
        return self._sentido

    @sentido.setter
    def sentido(self, sentido):
        self._sentido = sentido

    @property
    def municipio(self):
        return self._municipio

    @municipio.setter
    def municipio(self, municipio):
        self._municipio = municipio

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        self._longitude = longitude

    @property
    def evento(self):
        return self._evento

    @evento.setter
    def evento(self, evento):
        self._evento = evento

    def __iter__(self):
        for key in self.__dict__:
            yield key.replace('_', ''), self.__getattribute__(key)
