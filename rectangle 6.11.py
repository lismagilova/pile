class Rectangle():
    def init(self, a, b):
        self.a = a
        self.b = b

    def calc_p(self):
        return (self.a + self.b) * 2

    def calc_sq(self):
        return self.a * self.b

rec1 = Rectangle(2, 9)

