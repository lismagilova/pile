from random import choice

class Card:
    def init(self):
        self.value = [i for i in range(2, 15)]
        self.suit = ['diamonds', 'spades', 'clubs', 'hearts']

class Hand:
    def init(self):
        self.c_on_h = []

    def add_card(self):
        while len(self.c_on_h) != 5:
            g = [choice(P.suit), choice(P.value)]
            if g in self.c_on_h:
                continue
            else:
                self.c_on_h.append(g)
        return self.c_on_h

    def check(self):
        c_suits = {'spades': 0, 'hearts': 0, 'diamonds': 0, 'clubs': 0}
        flash = 0
        stg = 0
        values = []
        c_values = {}
        for i in range(5):
            values.append(self.c_on_h[i][1])
        for key in c_suits:
            for i in range(5):
                if key == self.c_on_h[i][0]:
                    c_suits[key] += 1
        for key in c_suits:
            if c_suits[key] == 5:
                flash = 1
                break
        for i in range(5):
            c_values[self.c_on_h[i][1]] = 0
        for i in range(5):
            c_values[self.c_on_h[i][1]] = c_values[self.c_on_h[i][1]] + 1
        setvalues = set(values)
        if sum(values) == (min(values) + max(values)) / 2 * len(values) and values == setvalues:
            stg = 1
        comb_val = {'Pair': 0, 'Triple': 0, 'Quad': 0}
        for key in c_values:
            if c_values[key] == 2:
                comb_val['Pair'] = comb_val['Pair'] + 1
        for key in c_values:
            if c_values[key] == 3:
                comb_val['Triple'] = comb_val['Triple'] + 1
        for key in c_values:
            if c_values[key] == 4:
                comb_val['Quad'] += 1
        if flash == 1 and stg == 1 and min(values) == 10:
            return 'Royal Flush'
        elif flash == 1 and stg == 1:
            return 'Straight Flush'
        elif stg == 1:
            return 'Street'
        elif comb_val['Quad'] == 1:
            return 'Kar'
        elif comb_val['Triple'] == 1 and comb_val['Pair'] == 1:
            return 'Full House'
        elif comb_val['Pair'] == 2:
            return 'Two pairs'
        elif flash == 1:
            return 'Flash'
        elif comb_val['Triple'] == 1:
            return 'Three'
        elif comb_val['Pair'] == 1:
            return 'Pair'
        else:
            return 'High card'

P = Card()
player = Hand()
print(player.add_card())
print(player.check())