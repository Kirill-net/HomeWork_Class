class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_rating_(self):
        list_ = [i for i in self.grades.values()]
        rating = sum(sum(list_, [])) / len(sum(list_, []))
        return rating

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and 0 < grade < 11 and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: '
                f'{self._average_rating_()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, some_student):
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
    def _average_rating_(self):
        list_ = [i for i in self.grades.values()]
        rating = sum(sum(list_, [])) / len(sum(list_, []))
        return rating

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self._average_rating_()}'

    def __lt__(self, some_lector):
        return (self._average_rating_() < some_lector._average_rating_())

   # def __gt__(self, some_lector):
        #return (self._average_rating_() > some_lector._average_rating_())

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java']
other_student = Student('Piter', 'Pen', 'your_gender')
other_student.courses_in_progress += ['Python', 'Java']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 7)

cool_lecturer = Lecturer('ivan', 'Petrovich')
cool_lecturer.courses_attached += ['Java']

other_lecturer = Lecturer('Nikolay', 'Pushkin')
other_lecturer.courses_attached += ['Java']

best_student.rate_hw(cool_lecturer, 'Java', 10)
best_student.rate_hw(cool_lecturer, 'Java', 9)
best_student.rate_hw(other_lecturer, 'Java', 8)
best_student.rate_hw(other_lecturer, 'Java', 8)

print(cool_lecturer)
print(other_lecturer)
print(best_student)
print(other_student)
print(cool_lecturer > other_lecturer)
print(other_student > best_student)