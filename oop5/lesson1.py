class Verification:

    def __init__(self,login,password):
        self.login = login
        self.password = password

    def lenPassword(self):
        if len(self.password) < 8:
            raise ValueError('слищком короткий')

    def save(self):
        with open('users.txt','a')as file:
            file.write(f'{self.login,self.password}\n')

users1 = Verification('ramazan','12345678')
users1.save()