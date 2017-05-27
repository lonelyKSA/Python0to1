## animal is-a object(yes , sort of confusing) look at the extra credit

class Animal(object):
    pass
    
## Dog is-a animal
class Dog(Animal):
    def __init__(self,name):
        ## self has-a name
        self.name = name
        
        
        
## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self,name):
        ## self has-a name
        self.name = name
        
## Person is-a object

class Person(object):
    def __init__(self,name):
        ## Person has-a name
        self.name = name
        
        ## person has-a pet of some kind
        self.pet = None
        
## employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ##Employee has-a name and salary
        super(Employee, self).__init__(name)
        
        ##Employee has-a salary
        self.salary = salary