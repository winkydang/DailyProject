class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 5
        self.s = 1


    @property
    def diameter(self):
        print('diameter')
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        print('area')
        return 3.14 * self.radius ** 2


cir = Circle(3)
print(cir.diameter)
print(cir)