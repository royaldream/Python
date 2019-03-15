class Student1:

    def __init__(self):
        self.name = ""
        self.enrollment = 0
        self.age = 0
        self.grade = ""

    def __init__(self, name="", enrollment=0, age=0, grade=""):
        self.name = name
        self.enrollment = enrollment
        self.age = age
        self.grade = grade

    # @property
    def get_name(self):
        print("getter method called")
        return self.name

    # @set_name.setter
    def set_name(self, name):
        print("setter method called")
        self.name = name

    # @del_name.
    def del_name(self):
        del self.name

    name = property(get_name, set_name, del_name)


student1 = Student1()
student1.name = "Parth Roy"
print student1.name


del student1
# Inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print "Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear

x = Student("Mike", "Olsen", 2019)
x.welcome()
