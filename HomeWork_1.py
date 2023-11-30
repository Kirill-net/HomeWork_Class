class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['C++']
        self.courses_in_progress = []
        self.grades = {}

    def _average_rating_(self):                       # подсчет средней оценки по всем курсам
        list_ = [i for i in self.grades.values()]
        if len(sum(list_, [])) != 0:                 # проверка наличия оценок
            rating = round(sum(sum(list_, [])) / len(sum(list_, [])),1)
        else:
            rating = "ошибка"
        return rating

    def rate_hw(self, lecturer, course, grade):       # высталяем оценки
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and 0 < grade < 11 and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):                                        # вывод Print по заданию
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: '
                f'{self._average_rating_()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, some_student):                             # операторы сравнения
        return self._average_rating_() < some_student._average_rating_()

    # def __gt__(self, some_student):
       #return self._average_rating_() > some_student._average_rating_()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def _average_rating_(self):               # подсчет средней оценки по всем курсам
        list_ = [i for i in self.grades.values()]
        if len(sum(list_, [])) != 0:          # проверка наличия оценок
            rating = round(sum(sum(list_, [])) / len(sum(list_, [])),1)
        else:
            rating = "ошибка"
        return rating

    def __str__(self):                          # вывод Print по заданию
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self._average_rating_()}'

    def __lt__(self, some_lector):             # операторы сравнения
        return (self._average_rating_() < some_lector._average_rating_())

   # def __gt__(self, some_lector):
        #return (self._average_rating_() > some_lector._average_rating_())

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):             # высталяем оценки
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):                                         # вывод Print по заданию
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def grades_students(students, course):            # считаем среднее значение в рамках курса всех студентов
    list_students = [student.grades[course] for student in students if course in student.grades]
    if len(sum(list_students, [])) != 0:         # проверка наличия оценок
        rating_st = round(sum(sum(list_students, [])) / len(sum(list_students, [])),2)
    else:
        rating_st = 'ошибка'
    return rating_st

def grades_lecturers(lecturers, course):         # считаем среднее значение в рамках курса всех лекторов
    list_lecturers = [lecturer.grades[course] for lecturer in lecturers if course in lecturer.grades]
    if len(sum(list_lecturers, [])) != 0:
        rating_lec = round(sum(sum(list_lecturers, [])) / len(sum(list_lecturers, [])),2)
    else:
        rating_lec = 'ошибка'
    return rating_lec
# создаем студентов и назначаем курсы
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java']
other_student = Student('Piter', 'Pen', 'your_gender')
other_student.courses_in_progress += ['Python', 'Java']

# создаем проверяющих, лекторов  и список их курсов
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Java']

cool_lecturer = Lecturer('ivan', 'Petrovich')
cool_lecturer.courses_attached += ['Java', 'Python']

other_lecturer = Lecturer('Nikolay', 'Pushkin')
other_lecturer.courses_attached += ['Java', 'Python']

# задаем оценки студентам по разным курсам
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 9)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(other_student, 'Python', 7)
cool_reviewer.rate_hw(other_student, 'Java', 6)
cool_reviewer.rate_hw(other_student, 'Java', 10)

# задаем оценки лекторам по разным курсам
best_student.rate_hw(cool_lecturer, 'Java', 10)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Java', 9)
best_student.rate_hw(other_lecturer, 'Java', 8)
best_student.rate_hw(other_lecturer, 'Python', 10)
best_student.rate_hw(other_lecturer, 'Python', 10)
best_student.rate_hw(other_lecturer, 'Java', 8)

#проверяем выводы
print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print(cool_lecturer > other_lecturer)
print(other_student < best_student)

#задаем список студентов и лекторов для проверки последней задачи
students = [best_student, other_student]
lecturers = [cool_lecturer, other_lecturer]

#проверяем выводы
print(grades_lecturers(lecturers, 'Python'))
print(grades_lecturers(lecturers, 'Java'))

print(grades_students(students, 'Python'))
print(grades_students(students, 'Java'))
