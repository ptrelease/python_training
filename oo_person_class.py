class Person(object):

    def __init__(self):
        self.fname = 'john'
        self.lname = 'Doe'
        self.age = 33

    def get_details(self):
        return '%s, %s, %s' % (self.fname, self.lname, self.age)

class Employee(Person):

    def __init__(self):
        Person.__init__(self)
        self.occupation = 'teacher'
        self.salary = '34000'

    def get_details(self):
        # return '%s, %s, %s' % (self.fname, self.lname, self.age)
        return Person.get_details(self) + ' who earns %s as a %s.' % (self.salary, self.occupation)


class PeopleList(list):

    def find(self, a_person):
        # return 'this guy'
        for p in self:
            if a_person.fname == p.fname:
                return p

p = Person()

e = Employee()

people = PeopleList()
people.append(p)
people.append(e)


for some_guy in people:
    print(some_guy.get_details())

rv = people.find(p)
print('you have found %s' % rv.fname)

print('done')
