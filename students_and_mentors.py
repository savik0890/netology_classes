class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        average_rate = self.student_get_avg_rate()
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average_rate}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_get_avg_rate() == other.student_get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является студентом'

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.student_get_avg_rate() != other.student_get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является студентом'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.student_get_avg_rate() < other.student_get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является студентом'

    def __le__(self, other):
        if isinstance(other, Student):
            return self.student_get_avg_rate() <= other.student_get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является студентом'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.student_get_avg_rate() > other.student_get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является студентом'

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.student_get_avg_rate() >= other.student_get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является студентом'

    def student_get_avg_rate(self):
        avg_rate = []
        for value in self.grades.values():
            avg_rate += value
        try:
            return sum(avg_rate) / len(avg_rate)
        except ZeroDivisionError:
            return 'У студента нет оценок'

    def rate_lector(self, lector, grade, course):
        if isinstance(lector, Lecturer):
            if course in self.courses_in_progress or course in self.finished_courses:
                if course in lector.courses_attached:
                    if course in lector.grades:
                        lector.grades[course] += [grade]
                    else:
                        lector.grades[course] = [grade]
                else:
                    print('This Lector doesnt teach this course')
            else:
                print('You dont study this course')
        else:
            print('You can rate only Lecturer')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        rate = self.get_avg_rate()
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {rate:.1f}'''

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_rate() == other.get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является лектором'

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_rate() != other.get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является лектором'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_rate() < other.get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является лектором'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_rate() <= other.get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является лектором'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_rate() > other.get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является лектором'

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_rate() >= other.get_avg_rate()
        else:
            return f'{other.name} {other.surname} не является лектором'

    def get_avg_rate(self):
        avg_rate = []
        for value in self.grades.values():
            avg_rate += value
        try:
            return sum(avg_rate) / len(avg_rate)
        except ZeroDivisionError:
            return 'Данному лектору еще не ставили оценки'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'C++', 'Java']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Java', 10)
print(best_student.grades)


new_mentor = Lecturer('Some', 'Buddy')
new_mentor.courses_attached += ['Python', 'Java']
best_student.rate_lector(new_mentor, 10, 'Python')
best_student.rate_lector(new_mentor, 10, 'Python')
best_student.rate_lector(new_mentor, 3, 'Java')
best_student.rate_lector(cool_mentor, 10, 'Python')
best_student.rate_lector(new_mentor, 10, 'C++')
print(new_mentor.grades)


print(cool_mentor)
print(new_mentor)
print(best_student)


student1 = Student('Михаил', 'Данилин', 'your_gender')
student2 = Student('Михаил2', 'Данилин2', 'your_gender')
student1.courses_in_progress += ['Python', 'C++', 'Java']
student2.courses_in_progress += ['Python', 'C++', 'Java']

cool_mentor.courses_attached += ['Java']


cool_mentor.rate_hw(student1, 'Python', 10)
cool_mentor.rate_hw(student1, 'Python', 5)
cool_mentor.rate_hw(student1, 'Java', 10)
cool_mentor.rate_hw(student2, 'Python', 10)
cool_mentor.rate_hw(student2, 'Python', 10)
cool_mentor.rate_hw(student2, 'Java', 10)
print(student1.grades)
print(student2.grades)


def students_avg_rate(students: list, course: str):
    rate_list = []
    for student in students:
        if isinstance(student, Student):
            rate_list += student.grades.get(course)
        else:
            print(f"{student.name} не является студентом")
    return sum(rate_list) / len(rate_list)


students_rate = students_avg_rate([student1, student2, new_mentor], 'Python')
print(students_rate)


def lectors_avg_rate(lectors: list, course: str):
    rate_list = []
    for lector in lectors:
        if isinstance(lector, Lecturer):
            rate_list += lector.grades.get(course)
        else:
            print(f"{lector.name} не является лектором")
    return sum(rate_list) / len(rate_list)


lectors_rate = lectors_avg_rate([new_mentor, student1], 'Python')
print(lectors_rate)


new_mentor1 = Lecturer('Some', 'Buddy')
new_mentor1.courses_attached += ['Python', 'Java']
new_mentor2 = Lecturer('Some', 'Buddy')
new_mentor2.courses_attached += ['Python', 'Java']
best_student.rate_lector(new_mentor1, 10, 'Python')
best_student.rate_lector(new_mentor1, 10, 'Python')
best_student.rate_lector(new_mentor2, 10, 'Python')
best_student.rate_lector(new_mentor2, 10, 'Python')

print(student1)
print(student2)
print(new_mentor1 <= student2)
