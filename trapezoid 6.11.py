import math


class trapezoid():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def checking(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))

        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

    def side(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)

    def per(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        P = a + b + c + d
        print("Периметр:", P)

    def area(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        S = ((a + b) / 2) * (math.sqrt((c ** 2) - ((((b - a) ** 2) + (c ** 2) - (d ** 2)) / (2 * (b - a)))))
        print("Площадь:", S, "\n")


fis_trap = trapezoid(0, 0, 2, 2, 4, 2, 6, 0)
fis_trap.checking()
fis_trap.side()
fis_trap.per()
fis_trap.area()
fis_trap1 = trapezoid(0, 0, 3, 3, 6, 3, 9, 0)
fis_trap1.checking()
fis_trap1.side()
fis_trap1.per()
fis_trap1.area()