from storage import Storage
 
class HDD(Storage):
    def __init__(self, name, manufacturer, capacity_GB, size, rpm, total=0, allocated=0):
        super().__init__(name, manufacturer, capacity_GB, total, allocated)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, manufacturer={self._manufacturer!r}, ' \
               f'capacity_GB={self._capacity_GB}, size={self._size!r}, rpm={self._rpm}, ' \
               f'total={self._total}, allocated={self._allocated})'
