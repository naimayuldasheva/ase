# def a(x):
#     print('first')
#     def b():
#         print('second')
#         x()
#     return b()

# @a
# def c():
#     print('third')




# def saen(s):
#     print('alina')
#     def sin():
#         print('asd')
#         s()
#     return sin()
# @saen
# def srer():
#     print('qwer')




# class Test:

#     def print_text(self):
#         print("это родительский класс test")
# class Test2(Test):
#     def print_text(self):
#         print("это дочепный класс test2")
# test2 = Test2()
# test2.print_text()



# class test:
#     test = None
# print(test.test)

# import abc


# class Aggregate:
    
    # @abs.abstractmethod
#     def iterator(self):
#         pass


# class Iterator():
#     def __init__(self, collection, cursor):
#         self._collection = collection
#         self._cursor = cursor

#     @abc.abstractmethod
#     def first(self):

#         pass

#     @abc.abstractmethod
#     def next(self):
        
#         pass

#     @abc.abstractmethod
#     def current(self):
        
#         pass



# from lib2to3.pgen2 import driver
# from re import L


# class Car:

#     def __init__(self,make,madel,year):
#         self.make = make
#         self.model = madel
#         self.year = year
#         self.odometor =0
#         self.fuel =70

#     def drive(self,km):
#         if driver in km:
#             print


# class Subscriber:

#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
    
#     def __str__(self)






# class Student:

#     def __init__(self,name,lastname,department,year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance

#     def get_student_info(self):
#         return f"{self.name},{self.lastname}, поступил факультет программирование {self.department}"
 
# a = Student('вася','иванова',2017,'программирований')
# print(a.get_student_info())

# class Subscriber:

#      def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#      def __str__(self):
#         return self.firstname+self.lastname

# r  = Subscriber('naima', 'kurbanova')
# print(r)




# class Person:

#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname

#     def info_about_human(self):
       
#         return f"{self.name},{self.surname}"

# s = Person('azamat','mirahimov')
# s = Person('azamat','mirahimov')
# s = Person('azamat','mirahimov')
# print(s.name)
# print(s.surname)

# 6. Создайте класс Car. Пропишите в конструкторе параметры make, model, year, odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте, хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого пусть метод drive также отнимет потраченное количество бензина с помощью приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill more!!1


# class Car:

#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometor = 0
#         self.fuel = 70

#     def drive(self,km):
#         if dr in km:
#             print()



# class car:

#     def __init__(self,model,make,year,mik):
#         self.model = model
#         self.make = make
#         self.year = year
#         self.mik = mik

#     def __set__(self):
#         return f'{self.model}+{self.year}'

# a = car('toyota',',',12,'mk')
# print(a.__set__)