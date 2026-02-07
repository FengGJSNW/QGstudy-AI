import math

class Shape:
    count = 0
    def __init__(self):
        self.__area = 0.0
        Shape.count += 1

    @property
    def area(self):
        return self.__area

    def _set_area(self, value: float):
        if value < 0.0:
            raise ValueError("面积必须大于等于0")
        self.__area = value

    def calc_area(self):
        print("当前图形使用了未重载的函数 calc_area()")


class Circle(Shape):
    count = 0

    def __init__(self, r: float):
        super().__init__()
        if r < 0:
            raise ValueError("半径必须大于等于0")
        self.__r = r
        Circle.count += 1
        self.calc_area()

    def calc_area(self):
        area = math.pi * self.__r ** 2
        self._set_area(area)
        return self.area


class Rectangle(Shape):
    count = 0
    def __init__(self, base: float, height: float):
        super().__init__()
        self.__base = base
        self.__height = height
        Rectangle.count += 1
        self.calc_area()

    def calc_area(self):
        area = self.__base * self.__height
        self._set_area(area)
        return self.area


a = [Rectangle(i, i + 1) for i in range(3, 10)]
b = [Circle(i) for i in range(1, 10)]

for index, element in enumerate(a):
    print(f"Rectangle[{index}] || area: {element.area}")

for index, element in enumerate(b):
    print(f"Circle[{index}] || area: {element.area}")

