from resources import Resource
 
class Storage(Resource):
    def __init__(self, name, manufacturer, capacity_GB, total=0, allocated=0):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, manufacturer={self._manufacturer!r}, ' \
               f'capacity_GB={self._capacity_GB}, total={self._total}, allocated={self._allocated})'
