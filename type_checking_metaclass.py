class TypeCheckedMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        annotations = cls.__annotations__

        def setattr_with_type_checking(instance, key, value):
            if key in annotations:
                expected_type = annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(f"Attribute '{key}' must be of type '{expected_type.__name__}'")
            instance.__dict__[key] = value

        cls.__setattr__ = setattr_with_type_checking


class MyClass(metaclass=TypeCheckedMeta):
    name: str
    age: int
    height: float
    is_student: bool


my_instance = MyClass()

my_instance.name = "John Doe"
my_instance.age = 30
my_instance.height = 1.8
my_instance.is_student = True

try:
    my_instance.age = "thirty" 
except TypeError as e:
    print(e)  

try:
    my_instance.height = "six feet"  
except TypeError as e:
    print(e) 

try:
    my_instance.is_student = 1  
except TypeError as e:
    print(e) 
