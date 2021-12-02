class Vector2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def add(self, new):
        new_x = self.x + new.x
        new_y = self.y + new.y
        return Vector2D(new_x, new_y)

    def add2(self, new):
        self.x += new.x
        self.y += new.y

    def sub(self, new):
        new_x = self.x - new.x
        new_y = self.y - new.y
        return Vector2D(new_x, new_y)

    def sub2(self, new):
        self.x -= new.x
        self.y -= new.y

    def mult(self, num):
        new_x = self.x * num
        new_y = self.y * num
        return Vector2D(new_x, new_y)

    def mult2(self, num):
        self.x *= num
        self.y *= num

    def str(self):
        return 'Vector2D(x = ' + str(self.x) + ', y = ' + str(self.y) + ')'

    def len(self):
        return len((self.x ** 2 + self.y ** 2) ** 0.5)

    def scalarProduct(self, new):
        prod = self.x * new.x + self.y + new.y
        return Vector2D(prod)

    def cos(self, new):
        cs = (self.x * new.x + self.y * new.y) / ((self.x**2 + self.y**2)**0.5 * (new.x**2 + new.y**2)**0.5)
        return Vector2D(cs)

    def equals(self, new):
        len_old = (self.x**2 + self.y**2)**0.5
        len_new = (new.x**2 + new.y**2)**0.5
        if len_old > len_new:
            return 'Первый вектор длины ' + str(len_old) + ' больше'
        elif len_old < len_new:
            return 'Второй вектор длины ' + str(len_new) + ' больше'
        else:
            return 'Оба вектора длины ' + str(len_new) + ' = ' + str(len_old) + ' одинаковы'