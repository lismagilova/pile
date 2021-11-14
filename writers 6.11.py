import operator
import tkinter as tk

class writers():
    def __init__(self, full_name, pseudonym, birth_death, country, works):
        self.full_name = full_name
        self.pseudonym = pseudonym
        self.birth_death = birth_death
        self.country = country
        self.works = works

    def get_full_info(self):
        full_info = f"{self.full_name} ({self.pseudonym}): {self.birth_death}, {self.country}, {self.works}"
        return full_info

class work():
    def __init__(self, name, author: list, publisher: list, year):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year

    def get_full_data(self):
        full_data = f'"{self.name}" {self.author} ({self.publisher}) в {self.year}'
        return full_data

class book(work):
    def __init__(self, binging, cover):
        super().__init__(name, author, publisher, year)
        self.binging = binging
        self.cover = cover

class magazine(work):
    def __init__(self, type_of_cover):
        super().__init__(name, author, publisher, year)
        self.type_of_cover = type_of_cover

class publication(work):
    def __init__(self, place_of_publication):
        super().__init__(name, author, publisher, year)
        self.place_of_publication = place_of_publication


writer1 = writers('Александр Сергеевич Пушкин', 'Француз', '1799-1837', 'Российская Империя', ["Евгений Онегин",
                                                                                               "Капитанская дочка",
                                                                                               "Дубровский"])
writer2 = writers('Лев Николаевич Толстой', 'псевдоним отсутствует', '1828-1910', 'Российская Империя', ["Анна Каренина",
                                                                                                         "Война и мир",
                                                                                                         "Кавказский пленник"])
work1 = work('Евгений Онегин', ['Александр Сергеевич Пушкин'], ['АСТ', 'Эксмо'], '1833')
work2 = work('Капитанская дочка', ['Александр Сергеевич Пушкин'], ['Эксмо'], '1841')

print(writer1.get_full_info())
print(writer2.get_full_info())
print(work1.get_full_data())
print(work2.get_full_data())

#objects = [work1, work2]
#result = sorted(objects, key=operator.attrgetter('author'))

#for work in result:
    #print(work.author)