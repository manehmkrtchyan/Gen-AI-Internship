class Resource:
    def __init__(self, name, manufacturer, total=0, allocated=0):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def __str__(self):
        return self._name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, manufacturer={self._manufacturer!r}, ' \
               f'total={self._total}, allocated={self._allocated})'

    @property
    def category(self):
        return self.__class__.__name__.lower()

    def claim(self, n):
        if self._total - self._allocated >= n:
            self._allocated += n
            print(f"Successfully claimed {n} {self._name}(s).")
        else:
            print(f"Not enough {self._name}s available to claim {n}.")

    def freeup(self, n):
        if self._allocated >= n:
            self._allocated -= n
            print(f"Successfully freed up {n} {self._name}(s).")
        else:
            print(f"Invalid number of allocated {self._name}s to free up.")

    def died(self, n):
        if self._total >= n:
            self._total -= n
            if self._allocated > self._total:
                self._allocated = self._total
            print(f"Successfully removed {n} {self._name} from the pool.")
        else:
            print(f"Invalid number of total {self._name}s to remove.")

    def purchased(self, n):
        if n >= 0:
            self._total += n
            print(f"Successfully purchased {n} {self._name}(s).")
        else:
            print(f"Invalid number of {self._name}s to purchase.")