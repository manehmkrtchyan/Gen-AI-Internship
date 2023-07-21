class ValidType:
    def __init__(self, type_):
        self.type_ = type_

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise ValueError(
                f"Invalid type for '{self.name}', expected {self.type_.__name__}."
            )
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)


class Int(ValidType):
    def __init__(self):
        super().__init__(int)


class Float(ValidType):
    def __init__(self):
        super().__init__(float)


class List(ValidType):
    def __init__(self):
        super().__init__(list)


class Person:
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()
    name = ValidType(str)

    def __init__(self, name, age, height, tags, favorite_foods):
        self.name = name
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods


try:
    person1 = Person("Jack", 30, 1.75, ["smart", "friendly"], ["pizza", "ice cream"])
    person2 = Person("Jane", "thirty", 1.65, ["kind", "funny"], ("sushi", "pasta"))
except ValueError as e:
    print(f"ValueError: {e}")
