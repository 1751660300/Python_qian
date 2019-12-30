# -*- coding:utf-8 -*-
class Stu(object):
    def __init__(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def del_grade(self):
        self.grade = None
        print("shanchu ")

    grades = property(get_grade, set_grade, del_grade, "this is grade of student")


if __name__ == '__main__':
    jack = Stu(50)
    print(jack.grades)
    jack.grades = 61
    print(jack.grades)
    print(Stu.grades.__doc__)
    del jack.grades

