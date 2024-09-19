import math

# Базовый класс
class Shape:
    def __init__(self, type=None, lenght=None, width=None, radius=None):
        self.lenght = lenght
        self.width = width
        self.radius = radius
        self.type = type

    # "вычисляет площадь фигуры"
    def area(self):
        if isinstance(self, Rectangle):
            return self.lenght * self.width
        elif isinstance(self, Circle):
            return round(math.pi * self.radius ** 2)
        elif isinstance(self, Square):
            return self.lenght **2

    # вычисляет периметр фигуры.
    def perimetr(self):
        if isinstance(self, Rectangle):
            return self.lenght * 2 + self.width * 2
        elif isinstance(self, Circle):
            return round(2 * math.pi * self.radius)
        elif isinstance(self, Square):
            return self.lenght * 4

    # выводит информацию о фигуре: ее тип, площадь и периметр.
    def display_info(self):
        return f"Тип фигуры: {self.type}\nПлощадь: {self.area()}\nПериметр: {self.perimetr()}"


# ЭК Фигура - Прямоугольник
class Rectangle(Shape):
    def __init__(self, lenght=None, width=None, type="Прямоугольник"):
        super().__init__(type, lenght, width)


# ЭК Фигура - Круг
class Circle(Shape):
    def __init__(self, lenght=None, width=None, radius=None, type="Круг"):
        super().__init__(type, lenght, width, radius)

# ЭК Фигура - Квадрат
class Square(Shape):
    def __init__(self, lenght=None, type="Квадрат"):
        super().__init__(type, lenght)

