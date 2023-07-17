from storage import Storage
 
class SSD(Storage):
    def __init__(self, name, manufacturer, capacity_GB, interface, total=0, allocated=0):
        super().__init__(name, manufacturer, capacity_GB, total, allocated)
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, manufacturer={self._manufacturer!r}, ' \
               f'capacity_GB={self._capacity_GB}, interface={self._interface!r}, ' \
               f'total={self._total}, allocated={self._allocated})'
