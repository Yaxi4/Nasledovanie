class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Я стал доктором. Жду поздравления!')

    def can_build(self):
        print('Я доктор, но тоже умею строить, правда не очень качественно')


class Builder:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Я стал строителем. Жду поздравления!')

    def can_build(self):
        print('Я строитель и я умею хорошо строить')


class Person(Builder, Doctor):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.degree=degree

    def __str__(self):
        return f'Person {self.rank} {self.degree}'

a=Doctor(6)
p=Person(5,'super')
print(a.degree)
print(p)
print(Doctor.degree)