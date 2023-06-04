
# Завдання 1
# Використовуючи поняття множинного успадкування,
# створіть клас «Коло, поміщене в квадрат».
# class Circle:
#     def __init__(self, size, name):
#         self.size = size
#         self.name = name
#
#     def showInfo(self):
#         print(f'Circle size - {self.size}')
#         print(f'Circle name - {self.name}')
#
#
# class Square:
#     def __init__(self, size2, name2):
#         self.size2 = size2
#         self.name2 = name2
#
#     def showInfo2(self):
#         print(f'Square size - {self.size2}')
#         print(f'Square name - {self.name2}')
#
#
# class Circle_in_Square(Circle, Square):
#     def __init__(self, size, name, size2, name2):
#         Circle.__init__(self, size, name)
#         Square.__init__(self, size2, name2)
#
#     def showInfo3(self):
#         print(f'Circle size - {self.size}')
#         print(f'Circle name - {self.name}')
#         print(f'Square size - {self.size2}')
#         print(f'Square name - {self.name2}')


# circle_in_square = Circle_in_Square(23, 'Black', 34, 'Yellow')
# circle_in_square.showInfo3()


# Завдання 2
# Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
# «Колеса», «Двигун», «Двері» та ін.

# class Auto:
#     def __init__(self, name):
#         self.name = name
#
#     def showInfo(self):
#         print(f'car name - {self.name}')
#
#
# class Wheels:
#     def __init__(self, wheels):
#         self.wheels = wheels
#
#     def showInfo2(self):
#         print(f'How much wheels {self.wheels}')
#
#
# class Engine:
#     def __init__(self, engine_capacity):
#         self.engine_capacity = engine_capacity
#
#     def showInfo3(self):
#         print(f'Engine capacity - {self.engine_capacity}')
#
#
# class Doors:
#     def __init__(self, doors):
#         self.doors = doors
#
#     def showInfo4(self):
#         print(f'How much doors - {self.doors}')
#
#
# class All_This(Auto, Wheels, Engine, Doors):
#     def __init__(self, name, wheels, engine_capacity, doors):
#         Auto.__init__(self, name)
#         Wheels.__init__(self, wheels)
#         Engine.__init__(self, engine_capacity)
#         Doors.__init__(self, doors)
#
#     def showInfo5(self):
#         print(f'car name - {self.name}')
#         print(f'How much wheels {self.wheels}')
#         print(f'Engine capacity - {self.engine_capacity}')
#         print(f'How much doors - {self.doors}')
#
# all_this = All_This(23, 23, 23, 23)
# all_this.showInfo5()


# Завдання 3
# Створіть базовий клас «Домашня тварина» та похідні
# класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
# конструктора встановіть ім’я кожної тварини та її характеристики. Реалізуйте для кожного із класів наступні
# методи:
# ■ Sound — видає звук тварини (пишемо текстом в консоль);
# ■ Show — відображає ім’я тварини;
# ■ Type — відображає підвид тварини.


# class Dog:
#     def __init__(self, sound, show, type_):
#         self.sound = sound
#         self.show = show
#         self.type = type_
#
#     def showInfo(self):
#         print(f'Dog sound - {self.sound}')
#         print(f'Dog name - {self.show}')
#         print(f'Dog type - {self.type}')
#
# class Cat:
#     def __init__(self, sound1, show1, type_1):
#         self.sound1 = sound1
#         self.show1 = show1
#         self.type1 = type_1
#
#     def showInfo(self):
#         print(f'Cat sound - {self.sound1}')
#         print(f'Cat name - {self.show1}')
#         print(f'Cat type - {self.type1}')
#
#
# class Parrot:
#     def __init__(self, sound2, show2, type_2):
#         self.sound2 = sound2
#         self.show2 = show2
#         self.type2 = type_2
#
#     def showInfo(self):
#         print(f'Parrot sound - {self.sound2}')
#         print(f'Parrot name - {self.show2}')
#         print(f'Parrot type - {self.type2}')
#
# class Hamster:
#     def __init__(self, sound3, show3, type_3):
#         self.sound3 = sound3
#         self.show3 = show3
#         self.type3 = type_3
#
#     def showInfo(self):
#         print(f'Hamster sound - {self.sound3}')
#         print(f'Hamster name - {self.show3}')
#         print(f'Hamster type - {self.type3}')
#
# class Pets(Dog, Cat, Parrot, Hamster):
#     def __init__(self, sound, show, type_, sound1, show1, type_1, sound2, show2, type_2, sound3, show3, type_3 ):
#         Dog.__init__(self, sound, show, type_)
#         Cat.__init__(self, sound1, show1, type_1)
#         Parrot.__init__(self, sound2, show2, type_2)
#         Hamster.__init__(self, sound3, show3, type_3)
#
#     def showInfo2(self):
#         print(f'Dog sound - {self.sound}')
#         print(f'Dog name - {self.show}')
#         print(f'Dog type - {self.type}\n')
#         print(f'Cat sound - {self.sound1}')
#         print(f'Cat name - {self.show1}')
#         print(f'Cat type - {self.type1}\n')
#         print(f'Parrot sound - {self.sound2}')
#         print(f'Parrot name - {self.show2}')
#         print(f'Parrot type - {self.type2}\n')
#         print(f'Hamster sound - {self.sound3}')
#         print(f'Hamster name - {self.show3}')
#         print(f'Hamster type - {self.type3}')
#
# pets = Pets(23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23)
# pets.showInfo2()


# Завдання 4
# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця. Для базового класу це може бути рядок із написом
# «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.


# class Employer:
#     def __init__(self):
#         pass
#
#     def showInfo(self):
#         print(f'This is Employer class\n')
#
#
# class President(Employer):
#
#     def showInfo1(self):
#         print(f'This is president class\n')
#
#
# class Manager(Employer):
#
#     def showInfo2(self):
#         print(f'This is manager class\n')
#
#
# class Worker(Employer):
#
#     def showInfo3(self):
#         print(f'This is worker class')
#
#
# employer = Employer()
# employer.showInfo()
# president = President()
# president.showInfo1()
# manager = Manager()
# manager.showInfo2()
# worker = Worker()
# worker.showInfo3()


# Завдання 5
# Для класів із попереднього завдання реалізуйте магічний метод str, а також метод int (який повертає вік
# службовця).


class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Employer class - {self.name}\n' \
               f'Employer age - {self.age}'





class President(Employer):
    def __str__(self):
        return f'President class - {self.name}\n' \
               f'President age - {self.age}'


class Manager(Employer):
    def __str__(self):
        return f'Manager class - {self.name}\n' \
               f'Manager age - {self.age}'



class Worker(Employer):
    def __str__(self):
        return f'Worker class - {self.name}\n' \
               f'Worker age - {self.age}'




employer = Employer('Kate', 23)
print(employer)
president = President('Oliver', 28)
print(president)
manger = Manager('Brand', 34)
print(manger)
worker = Worker('John', 26)
print(worker)
