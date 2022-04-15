from a import Verification


class v2(Verification):
    
   def save(self):
       with open('users.txt','r')as new:
           for i in new:
               if f'{self.login,self.password}\n'==i:
                   raise ValueError('такое уже есть!')


user2 = v2('ramazan','12345678')
user2.save()