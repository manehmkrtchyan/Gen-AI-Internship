class Int:
    def __init__(self, value, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.value = value

    def __set_name__(self, owner, name):
        self.name = name

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer.")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be greater than or equal to {self.min_value}.")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be less than or equal to {self.max_value}.")
        return value

    def __set__(self, instance, value):
        validated_value = self.validate(value)
        instance.__dict__[self.name] = validated_value


class Point2D:
    def __init__(self, x, y):
        self.x = Int(x)
        self.y = Int(y)

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer.")
        if value < 0:
            raise ValueError(f"{self.name} must be a non-negative integer.")
        instance.__dict__[self.name] = value


class Point2DSequence:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = name

    def validate(self, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError(f"{self.name} must be a sequence.")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"{self.name} must have at least {self.min_length} elements.")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"{self.name} cannot have more than {self.max_length} elements.")
        for point in value:
            if not isinstance(point, Point2D):
                raise ValueError(f"Each element in {self.name} must be an instance of Point2D.")
        return value

    def __set__(self, instance, value):
        validated_value = self.validate(value)
        instance.__dict__[self.name] = validated_value


class Polygon:
    def __init__(self, *vertices):
        self.vertices = Point2DSequence(min_length=3, max_length=10)
        if vertices:
            self.vertices = list(vertices)

    def append(self, point):
        if len(self.vertices) >= self.vertices.max_length:
            raise ValueError("Cannot append more vertices. Maximum length reached.")
        self.vertices.append(point)
