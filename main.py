
class Student:
    def __init__(self, name, surname, age):
        self.imya = name
        self.surname = surname
        self.age = age
        self.kabinet = 0
        self.budj = ''
        self.marks = 0


    @classmethod
    def specialityChange(cls, spec):
        cls.speciality = spec

    @classmethod
    def vartistChange(cls, cina):
        cls.vartist = int(cina)

    @classmethod
    def otchislen(cls, otchislen):
        cls.otchislen1 = otchislen

    @classmethod
    def teacher(cls, teacher):
        cls.teacher1 = teacher


    def teacher_class(self):
        if self.teacher1 == 'Tatiana Kravchuk':
            self.kabinet = 33
        elif self.teacher1 == 'Oleg Boyko':
            self.kabinet = 21
        elif self.teacher1 == 'Alex White':
            self.kabinet = 18
        else:
            self.kabinet = "we don't have this kabinet"



    def student_marks(self):
        if self.otchislen1 == 'student expelled':
            self.marks = 4
        elif self.otchislen1 == 'student expelled':
            self.marks = 5
        elif self.otchislen1 == 'student expelled':
            self.marks = 6
        else:
            if self.marks >= 6:
                self.otchislen1 = 'student not expelled'

    def auditory(self):
        if self.speciality == 'Python':
            self.kabinet = 33
        elif self.speciality == 'UI/UX':
            self.kabinet = 21
        elif self.speciality == 'Economy':
            self.kabinet = 18
        else:
            self.kabinet = 'we dont have this speciality'

    def budj_or_kontract(self):
        if self.vartist == 0:
            self.budj = 'budjet'
        elif 10000 > self.vartist > 0:
            self.budj = 'kontract'
        elif self.vartist > 10000:
            self.budj = f'zaborgovannist - {self.vartist - 10000} grn'
        else:
            self.budj = 'ca"t be -'

    def ShowInfo(self):
        return f'name:{self.imya},surname:{self.surname},age:{self.age}\n' \
               f'speciality:{self.speciality}\n' \
               f'cabinet-{self.kabinet}\n' \
               f'vartist navchannya:{self.vartist}\n' \
               f'student marks - {self.marks}\n' \
               f'forma oplaty:{self.budj}\n' \
               f'teacher - {self.teacher1}' \


    @staticmethod
    def info_about_programm():
        print('This programm can help u to find info about all students')

    @staticmethod
    def enter_y_or_n():
        print('Enter y or n to take info about student')

    @staticmethod
    def end():
        print('Thank u for using our app')

    @staticmethod
    def ia_ne_znayu():
        print('я не знаю что еще добавить')



Student.info_about_programm()
Student.enter_y_or_n()
Student.ia_ne_znayu()
while True:
    try:
        a = input('do u want to know info about student?: ')
        if a == 'y':
            name, surname, age, speciality, price, otchislen1, teacher1 = map(str, input(
                'enter name,  surname, age, speciality, price, marks, kabinet (with Space): ').split())
            Student.specialityChange(speciality)
            Student.teacher(teacher1)
            Student.vartistChange(price)
            Student.otchislen(otchislen1)
            stud = Student(name, surname, age)
            stud.auditory()
            stud.student_marks()
            stud.budj_or_kontract()
            stud.teacher_class()
            print(stud.ShowInfo())

        elif a == 'n':
            Student.end()
            break
        else:
            print('input only y or n')
    except:
        print('not correct info')
