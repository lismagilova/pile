class Triangle():
    def init(self, a, b):
        self.a = a
        self.b = b

    def calc_hypothesis(self):
        self.c = (self.a + self.b) ** 0.5
        return self.c

    def calc_p(self):
        calc_hypothesis(self)
        return self.a + self.b + self.c

    def calc_s(self):
        return self.a * self.b * 0.5



triangle_1 = Triangle(2, 3)
print(calc_hypothesis(triangle_1))
print(calc_p(triangle_1))
print(calc_s(triangle_1))