from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'department'])

alina = Student(name='Alina', age='22', department='linguistics')
alex = Student(name='Alex', age='25', department='programming')
kate = Student(name='Kate', age='19', department='art')

print(alina)
print(alex)
print(kate)