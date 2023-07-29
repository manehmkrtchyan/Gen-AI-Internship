class SlottedStructMeta(type):
    def __new__(mcs, name, bases, namespace):
        
        if '__slots__' in namespace:
            slots = namespace['__slots__']
            dimension = len(slots)

        def __init__(self, *args):
            if len(args) != dimension:
                raise ValueError('wrong qunatity of coordinates')
            for i, var in enumerate(slots):
                setattr(self, var, args[i])

        def __repr__(self):
            coordinates = ", ".join(str(getattr(self, f"_coord{i}")) for i in range(1, len(self.__slots__) + 1))
            return f"{self.__name__}({coordinates})"

        def __eq__(self, other):
            return isinstance(other, self.__class__) and all(
                getattr(self, slot) == getattr(other, slot) for slot in slots
            )

        def __hash__(self):
            return hash(tuple(getattr(self, i) for i in slots))

        namespace['__init__'] = __init__
        namespace['__eq__'] = __eq__
        namespace['__hash__'] = __hash__
        namespace['__repr__'] = __repr__

        return super().__new__(mcs, name, bases, namespace)
        

class Point2D(metaclass=SlottedStructMeta):
    __slots__ = ('x', 'y')


class Point3D(metaclass=SlottedStructMeta):
    __slots__ = ('x', 'y', 'z')


p2 = Point2D(5, 4)
p21 = Point2D(5, 5)
print(p2 == p21)
print(hash(p2))