class Person:
    def __init__(self,first_name, last_name):
        print('jestem w __init___. self = ', self)
        self.f_name = first_name
        self.l_name = last_name

    def get_name(self,prefix=''):
        return prefix + ' ' + self.f_name + ' ' + self.l_name


abacki = Person('Jan', 'Abacki')

print(abacki.get_name('Szanowny'))


class Dog:
    sound = 'wow'

    def make_sound(self):
        print(self.sound)


azor = Dog()
reksio = Dog()
reksio.sound = 'hau hau'
azor.make_sound()
reksio.make_sound()
