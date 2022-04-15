# class Person():

#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def set_age(self,value):
#         self.__age = value

#     @age.getter
#     def get_age(self):
#         return self.__age

# a = Person('timur',13)
# a.set_age = 23
# print(a.get_age)




class University:

    def __init__(self,universiyu_name):
        self.university_name = universiyu_name
        self.department = {}

    def add_deportment(self,name):
        self.department[name] = []

    def add_student(self,name):
        pass

        
class Student():
    
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        
    def __repr__(self):
        return f'{self.name},{self.lastname}'

a = Student('ulan','kurbanov')
b=University('oshmu')
b.add_deportment('med')
b.add_student(a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             