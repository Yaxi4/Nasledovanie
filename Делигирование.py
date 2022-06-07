class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        print('Родительский класс')
        print(self)
    def __str__(self):
        return f'Person класс {self.name} {self.surname}'

class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor класс {self.name} {self.surname}'
p=Person('Иван','Иванов')
d=Doctor('Петр','Петров',25)

d.info()
print('-----------------------------')
p.info()