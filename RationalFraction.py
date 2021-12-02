class RationalFraction():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def reduce(self):
        if self.x > self.y:
            divis = self.x
        else:
            divis = self.y
        while divis != 1:
            if self.x % divis == 0 and self.y % divis == 0:
                return self.x // divis, self.y // divis
            else:
                divis -= 1
        return self.x, self.y

    def add(self, new):
        if self.y == new.y:
            new_x = self.x + new.x
            new_y = self.y
        else:
            new_x = self.x * new.y + new.x * self.y
            new_y = self.y * new.y
        return RationalFraction(new_x, new_y).reduce()

    def add2(self, new):
        if self.y == new.y:
            self.x = self.x + new.x
            self.y = self.y
        else:
            self.x = self.x * new.y + new.x * self.y
            self.y = self.y * new.y

    def sub(self, new):
        if self.y == new.y:
            new_x = self.x - new.x
            new_y = self.y
        else:
            new_x = self.x * new.y - new.x * self.y
            new_y = self.y * new.y
        return RationalFraction(new_x, new_y).reduce()

    def sub2(self, new):
        if self.y == new.y:
            self.x = self.x - new.x
            self.y = self.y
        else:
            self.x = self.x * new.y - new.x * self.y
            self.y = self.y * new.y

    def mult(self, new):
        new_x = self.x * new.x
        new_y = self.y * new.y
        return RationalFraction(new_x, new_y).reduce()

    def mult2(self, new):
        self.x = self.x * new.x
        self.y = self.y * new.y

    def div(self, new):
        new_x = self.x * new.y
        new_y = new.x * self.y
        return RationalFraction(new_x, new_y).reduce()

    def div2(self, new):
        self.x = self.x * new.y
        self.y = self.y * new.x

    def str(self):
        return str(self.x) + '/' + str(self.y)

    def value(self):
        return self.x / self.y

    def equals(self, new):
        if self.x / self.y > new.x / new.y:
            return 'Первая дробь ' + str(self.x) + '/' + str(self.y) + ' больше'
        elif self.x / self.y < new.x / new.y:
            return 'Вторая дробь ' + str(new.x) + '/' + str(new.y) + ' больше'
        else:
            return 'Значения дробей равны ' + str(self.x) + '/' + str(self.y) + ' = ' +  str(new.x) + '/' + str(new.y)

    def numberPart(self):
        return int(self.x / self.y)