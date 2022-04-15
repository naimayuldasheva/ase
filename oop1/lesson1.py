# class auto:

#     def __init__(self,model,mark,color,year,obem):
#         self.model = model
#         self.mark = mark
#         self.color = color
#         self.year = year
#         self.obem = obem

#     def info(self):
#         return f'model',{self.model}


# class Teacher:

#     def __init__(self,name,year,professia,zarplata):
#         self.name = name
#         self.year = year 
#         self.profession = professia
#         self.zarplata = zarplata

#     def num(self):
#         return f'{self.name},{self.year},{self.profession},{self.zarplata}'

# num = Teacher('zarina',18,'teacher',1990)
# print(num.num())


class Car:

    def __init__(self, mark, model, color, year):
        self.mark = mark
        self.model = model
        self.color = color
        self.year = year
        self.fuel = 500
        self.odometr = 0
        self.is_going = False
    
    def start(self, km):
        if self.fuel <= 0:
            self.is_going = False
            print('No fuel!')
        
        else:
            self.is_going = True
            self.odometr += km
            self.fuel -= km * 12
            print(f'{self.mark} is going {self.odometr}')

    def stop(self):
        self.is_going = False

t34 = Car('tank', 't34', 'pink', 1940)

