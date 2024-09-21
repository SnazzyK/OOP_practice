import base_page
a = base_page.Rectangle(10, 20)
k = base_page.Circle(10, 20, 5)
c=base_page.Square(5)


def test_rectangle():
   try:
    assert a.__dict__ == {'length': 10, 'width': 20, 'radius': None, 'type': 'Прямоугольник'}
    assert a.perimetr()==60
    assert a.area() == 200
    assert isinstance(a,base_page.Rectangle)
    return f"Проверка успешна\nФигура:Прямоугольник\n--------------------"
   except:
    return f"Проверка провалена!!!!\nФигура:Прямоугольник\n--------------------"


def test_circle():
   try:
    assert k.__dict__ == {'length': 10, 'width': 20, 'radius': 5, 'type': 'Круг'}
    assert k.perimetr()==31
    assert k.area()==79
    assert isinstance(a, base_page.Rectangle) #Негативная проверка
    return f"Проверка успешна\nФигура:Круг\n----------------"
   except:
       return f"Проверка провалена!!!!\nФигура:Круг\n----------------"


def test_square():
   try:
    assert c.__dict__ =={'length': 5, 'width': None, 'radius': None, 'type': 'Квадрат'}
    assert c.area()==25
    assert c.perimetr()==20
    assert isinstance(a, base_page.Square)
    return f"Проверка успешна\nФигура:Квадрат\n----------------"
   except:
       return f"Проверка провалена!!!!\nФигура:Квадрат\n----------------"



print(test_rectangle())
print(test_circle())
print(test_square())
