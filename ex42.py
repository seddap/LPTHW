#Exercise 42: Is-A, Has-A, Objects and Classes

#Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#make a class named Dog that is-a(n) Animal
class Dog(Animal):

    def __init__(self, name):
        #class Dog has-a __init__ that takes self and name params
        #dog has-a name
        self.name = name

#make a class named Cat that is-a(n) Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has-a name
        self.name = name

        #Person has-a pet of some kind
        self.pet = None

#make a class named Employee that is-a Person
class Employee(Person):

    def __init__(self, name, salaray):
        #class Employee has-a __init__ that takes name param
        super(Employee, self).__init__(name)
        #Employee has-a name
        self.salary = salary

#make a class named Fish that is-a object
class Fish(object):
    pass

#make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

#make a class named Halibut that is-a fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

#from mary get the pet attribute and set it to the variable satan
mary.pet = satan

#frank is-a instance of Employee with the params name and salary
frank = Employee("Frank", 120000)

#from frank get the pet attribute and set it to the variable rover
frank.pet = rover

#set flipper to an instance of class Fish()
flipper = Fish()

#set crouse to an instance of class Salmon()
crouse = Salmon()

#set harry to an instance of class Halibut()
harry = Halibut()
