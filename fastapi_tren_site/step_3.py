# Классы, как типы
# Можно короче класс объявить, как тип переменной

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

# этот код эквивалентен вот этому

# class Person:
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def get_name(self):
#         return self.name


p1 = Person("ALice")

print(get_person_name(p1))

