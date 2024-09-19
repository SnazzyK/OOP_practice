import Base_Page
a = Base_Page.Rectangle(10, 20)
k = Base_Page.Circle(10, 20, 5)
c=Base_Page.Square(5)

assert a.__dict__ =={'lenght': 10, 'width': 20, 'radius': None, 'type': 'Прямоугольник'}
assert k.__dict__ =={'lenght': 10, 'width': 20, 'radius': 5, 'type': 'Круг'}
assert c.__dict__ =={'lenght': 5, 'width': None, 'radius': None, 'type': 'Квадрат'}

assert a.area()==200
assert k.area()==79
assert c.area()==25

assert a.perimetr()==60
assert k.perimetr()==31
assert c.perimetr()==20


print(f"Проверка завершена успешна")