class Rectangle():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def side(self):
        a = self.x2 - self.x1
        b = self.y2 - self.y3
        c = self.x3 - self.x4
        d = self.y1 - self.y4
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)

    def per(self):
        a = self.x2 - self.x1
        b = self.y2 - self.y3
        c = self.x3 - self.x4
        d = self.y1 - self.y4
        P = a + b + c + d
        print("Периметр:", P)

    def area(self):
        a = self.x2 - self.x1
        b = self.y2 - self.y3
        S = a * b
        print("Площадь:", S, "\n")


fis_rec = Rectangle(5, 4, 6, 4, 6, 2, 5, 2)
fis_rec.side()
fis_rec.per()
fis_rec.area()
# fis_trap1 = Rectangle(0, 0, 3, 3, 6, 3, 9, 0)
# fis_trap1.side()
# fis_trap1.per()
# fis_trap1.area()
