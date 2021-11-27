import math

class Triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def side(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2))
        print("Длина сторон: " + "\nAB: ", c, "\nBC: ", a, "\nCA: ", b)

    def per(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2))
        P = a + b + c
        print("Периметр:", P)

    def area(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2))
        p = (a + b + c)/ 2
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("Площадь:", S, "\n")


fis_trian = Triangle(1, 2, 5, 3, 7, 4)
fis_trian.side()
fis_trian.per()
fis_trian.area()
# fis_trian1 = Triangle(0, 0, 5, 5, 7, 4)
# fis_trian1.side()
# fis_trian1.per()
# fis_trian1.area()
