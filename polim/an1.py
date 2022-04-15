# class Rectangle:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b 

#     def get_rect_area(self):
#         return self.a * self.b

# class Square:

#     def __init__(self,a):
#         self.a = a
    
#     def get_square_area(self):
#         return self.a *  4

# class Circle:

#     def __init__(self,a):
#         self.a = a

#     def get_circle_area(self):
#         return 3.14 * self.a **2

# rec1 = Rectangle(3,5)
# rec2 = Rectangle(7,8)
# # print(rec1.get_rect_area(),rec2.get_rect_area())

# sq1 = Square(3)
# sq2 = Square(8)
# # print(sq1.get_square_area(),rec2.get_rect_area())

# cr1 = Circle(3)
# cr2 = Circle(7)
# # print(cr1.get_circle_area(),cr2.get_circle_area())

# figures = [rec1,rec2,sq1,sq2,cr1,cr2]
# for fig in figures:
#      if isinstance(fig,Rectangle):
#          print(fig.get_rect_area())
#      elif isinstance():

# from math import pi

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return "I am a two-dimensional shape."

#     def __str__(self):
#         return self.name


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

#     def area(self):
#         return self.length**2

#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2


# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())