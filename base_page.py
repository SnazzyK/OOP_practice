import math
from faker import Faker
# Базовый класс
class Shape:
    def __init__(self, type=None, length=None, width=None, radius=None):
        self.length = length
        self.width = width
        self.radius = radius
        self.type = type

    # "вычисляет площадь фигуры"
    def area(self):
        if isinstance(self, Rectangle):
            return self.length * self.width
        elif isinstance(self, Circle):
            return round(math.pi * self.radius ** 2)
        elif isinstance(self, Square):
            return self.length **2

    # вычисляет периметр фигуры.
    def perimetr(self):
        if isinstance(self, Rectangle):
            return self.length * 2 + self.width * 2
        elif isinstance(self, Circle):
            return round(2 * math.pi * self.radius)
        elif isinstance(self, Square):
            return self.length * 4

    # выводит информацию о фигуре: ее тип, площадь и периметр.
    def display_info(self):
        return f"Тип фигуры: {self.type}\nПлощадь: {self.area()}\nПериметр: {self.perimetr()}"


# ЭК Фигура - Прямоугольник
class Rectangle(Shape):
    def __init__(self, length=None, width=None, type="Прямоугольник"):
        super().__init__(type, length, width)


# ЭК Фигура - Круг
class Circle(Shape):
    def __init__(self, length=None, width=None, radius=None, type="Круг"):
        super().__init__(type, length, width, radius)

# ЭК Фигура - Квадрат
class Square(Shape):
    def __init__(self, length=None, type="Квадрат"):
        super().__init__(type, length)


