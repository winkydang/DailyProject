class Circle:
    def __init__(self, radius):
        self._radius = radius
        self.s = 1

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return 3.14 * self.radius ** 2

cir = Circle(radius=3)
print(cir)