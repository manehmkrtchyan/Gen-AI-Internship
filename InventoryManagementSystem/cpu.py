from resources import Resource

class CPU(Resource):
    def __init__(self, name, manufacturer, cores, socket, power_watts, total=0, allocated=0):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, manufacturer={self._manufacturer!r}, ' \
               f'cores={self._cores}, socket={self._socket!r}, power_watts={self._power_watts}, ' \
               f'total={self._total}, allocated={self._allocated})'
