# from audioop import add
# from multiprocessing.sharedctypes import Value
# from random import random


# class Player():

#     def __init__(self,muz):
#         self.muz = muz

#     def showplaylist(self):
#         return self.muz

#     def add_toplaylist(self):
#         self.muz.append(add)

#     def playlist(self):
#         for i in self.muz:
#             print(i)
    
#     def delete_from_playlist(self):
#         self.muz.remove(Value)

#     def shuffle(self):
#         random.shuffle(self.playlist)
#         return self.playlist
        
# class AudioPlayer(Player):
#     pass
# class VideoPlayer(Player):
#     pass

# spotify = AudioPlayer()
# spotify.add_toplaylist('Deam inside')
# spotify.add_toplaylist('see you again')
# spotify.add_toplaylist('gimn kg')
# spotify.playlist()
# print(spotify.shuffle())






# class Animal():
#     def __init__(self,name):
#         self.name = name
    
#     def eat(self):
#         return f'{self.name} '
    
#     def sleep(self):
#         return "horhor"
    
#     def male_sound(self,sound):
#         return sound

# class AnimalWithHorn(Animal):
    
#     def gode(self):
#         return "bam"
    
# class Cow(AnimalWithHorn):
#     pass
# class Ram(Animal):
#     pass

# s = Cow('skow')
# print(s.eat()).male_sound('bebbebbebbbeb')
# print(s.sleep())
# a = Ram('n')
# print(a.gode())
# print(a.male_sound('bebbebbebbbeb'))


class Todo():

    def __init__(self):
        self.todo_items = []  
 
    def add_todo(self, items):
        self.todo_items.append(items)
 
    def list(self):
        for item in self.todo_items:
            print(str(item.num) + '.' + item.todo + ' (Выполнено)' * int(item.is_done))
        print()
 
    def find(self):
        return ((item.num, item.todo) for item in self.todo_items if item.todo.find() != -1)
 
    def run(self):
 
        while True:
            print('Меню')
            for i in Todo():
                print(num + '. ' + val, end='\n')
            command = input()
            if command:
                self.add_todo(input('Какре дело? '))
                print('Новой дело добавленвав')
            elif command:
                self.list()
            elif command:
                find = self.find(input('Введите ключевое слово '))
                for num, val in find:
                    print(str(num) + '. ' + val)
            elif command:
                num = int(input('Номер дела для выполнения: '))
                for item in self.todo_items:
                    if item.num == num:
                        item.check()
                        print(f'Дело {num} выполнено')
                        break
                else:
                    print(f'Дело {num} не найдено')
 
            elif command:
                num = int(input('Номер дела для повторения: '))
                for item in self.todo_items:
                    if item.num == num:
                        print(f'Дело {num} повторено')
                        break
                else:
                    print(f'Дело {num} не найдено')
 
            elif command:
                print('Программа завершена')
                break
class TodoItem:
    couner_do = 0
 
    def __init__(self, new_do):
        self.is_done = False
        TodoItem.couner_do += 1
        self.num = TodoItem.couner_do
        self.todo = new_do
 
   
 
if __name__ == '__main__':
    todo_1 = Todo()
    todo_1.run()