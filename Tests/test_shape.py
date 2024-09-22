import base_page
rectangle_class = base_page.Rectangle(10, 20)
circle_class = base_page.Circle(10, 20, 5)
square_class=base_page.Square(5)


def test_rectangle():
    assert rectangle_class.__dict__ == {'length': 10, 'width': 20, 'radius': None, 'type': 'Прямоугольник'} ,'Данные не соответствуют '
    assert rectangle_class.perimetr()==60 ,  'Периметр прямоугольника посчиталась некорректно'
    assert rectangle_class.area() == 200 ,  'Площадь прямоугольника посчиталась некорректно'
    assert isinstance(rectangle_class,base_page.Rectangle) ,'экземпляр класса соответствует классу '



def test_circle():
    assert circle_class.__dict__ == {'length': 10, 'width': 20, 'radius': 5, 'type': 'Круг'} , 'Данные не соответствуют '
    assert circle_class.perimetr()==31 , 'Периметр круга посчиталась некорректно'
    assert circle_class.area()==79 , 'Площадь круга посчиталась некорректно'
    assert isinstance(circle_class, base_page.Circle) ,'экземпляр класса соответствует классу '



def test_square():
    assert square_class.__dict__ =={'length': 5, 'width': None, 'radius': None, 'type': 'Квадрат'}, 'Данные не соответствуют '
    assert square_class.area()==25 ,'Площадь квадрата посчиталась некорректно'
    assert square_class.perimetr()==20 , 'Периметр квадрата посчиталась некорректно'
    assert isinstance(square_class, base_page.Square) ,'экземпляр класса соответствует классу '






