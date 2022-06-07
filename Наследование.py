class Person:
    def mogy_dyshat(self):
        print('Человек может дышать')

    def mogy_xodit(self):
        print('Челочек может ходить')


class Doctor(Person):
    def mogy_lechit(self):
        print('Доктор может лечить')


class Architector(Person):
    def mogy_stroit(self):
        print('Архитектор может стороить')


d = Doctor()
a = Architector()
d.mogy_lechit()
d.mogy_dyshat()
a.mogy_stroit()
a.mogy_xodit()
print('---------------------------------------------------')
print(issubclass(Doctor, Person))
print(issubclass(Person, Doctor))
print(issubclass(Architector, Person))
print('---------------------------------------------------')
print(isinstance(d, Doctor))
print(isinstance(d, Person))
class Ortoped(Doctor):
    print('Я Доктор ортопед, класс Ortoped взял методы и алгоритмы от Person и Doctor')