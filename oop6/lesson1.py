# class Publication:

#     def __init__(self,name,data,pages,library,type):
#         self.name = name
#         self.data = data
#         self.pages = pages
#         self.library = library
#         self.type = type
# class Book(Publication):

#     def __init__(self, name, data, pages, library, type):
#         super().__init__(name, data, pages, library, type='book')

# class Magazine(Book):

#     def __init__(self, name, data, pages, library, type):
#         super().__init__(name, data, pages, library, type = 'magazine')

# class Newspaper(Magazine):

#     def __init__(self, name, data, pages, library, type):
#         super().__init__(name, data, pages, library, type = 'newspaper')

# class Publication(Newspaper):

#     def get_code_in_library(self):
#         return f'{self.library[:2]}_{self.type}_{self.name[:2]}_{self.pages}'


       
       
        # name = self.name[:2]
        # data = self.data[: 2]
        # pages = self.pages[:2]
        # library = self.library[:2]
        # type = self.type[:2]





# class Airplane:

#     def __init__(self,make,model,year):
#         self.make = make
#         self.model =model
#         self.year = year
#         self.odometor = 0
    
#     def take_off(self):
#         self.is_flying = True
#         print('взлет')
    
#     def fly(self,a):
#         self.odometor+=a
#         print('летит')

#     def land(self):
#         self.is_flying = False
#         print('признание')

# a = Airplane('','',1005)
# a.take_off()
# a.fly(2)
# a.land()
    




# from turtle import color


# class Weapon:

#     def __init__(self,name,model,magazin,range,color,weight,max_store):
#         self.name = name
#         self.model = model
#         self.magazin = magazin
#         self.range = range
#         self.color = color
#         self.weifht = weight
#         self.max_store = max_store
#         self.ballet = 0
#         self.obves = []

#     def ammo(self):
#         return (self.ballet)

#     def fill_ammo(self):
#         self.ballet += self.max_store

#     def fire(self,kaliches):
#         self.ballet = kaliches
    
#     def change_color(self):
#         self.color = color

#     def add_extension(self,name):
#         self.obves.append(name)

#     def remove_extension(self,name):
#         self.obves.remove(name)

# class Storage:

#     def __init__(self):
#         self.storage = []
    
#     def add_weapon(self,a):
#         self.storage.append(a)
    
#     def take_waepon(self):
#         self.name += self.storage

#     def take_waepon(self):
#         self.storage

        