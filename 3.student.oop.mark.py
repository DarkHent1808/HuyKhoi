import math
import numpy as np

class Course:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def _get_name(self):
        return self.__name

    def _get_id(self):
        return self.__id

    def display(self):
        print(f"Course name: {self.__name}, Course ID: {self.__id}")


course_List = []
numOfCourse = int(input("Enter number of Course: "))
for i in range(numOfCourse):
    C_Name = input(f"Enter course {i + 1} name: ")    #{i+1} idea source: NgvGiang
    C_Id = input(f"Enter course {i + 1} id: ")
    course_List.append(Course(C_Name, C_Id))


for i in range(numOfCourse):
    Course.display(course_List[i])


class Student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__mark = {}

    def _get_name(self):
        return self.__name

    def _get_id(self):
        return self.__id

    def _get_dob(self):
        return self.__dob

    def input_mark(self, course_name, mark):
        self.__mark[course_name] = mark

    def display(self):
        print(f"Student name: {self.__name}, Student ID: {self.__id}, Student DOB: {self.__dob}")
        for course_name, mark in self.__mark.items():
            print(f"   Course name: {course_name}, Mark: {mark}")
    def Avg_gpa(self, course_list):
        marks_array = np.array([self.__mark[course._get_name()] for course in course_list])
        gpa = np.average(marks_array)
        return gpa

def Gpa_Display(student_list, course_list):
    # Calculate GPA for each student
    gpa_list = [(student.Avg_gpa(course_list), student) for student in student_list]
    # Sort students based on GPA in descending order
    sorted_students = sorted(gpa_list, key=lambda x: x[0], reverse=True)
    # Display students with GPA in descending order
    for gpa, student in sorted_students:
        print(f"{student._get_name()} - GPA: {gpa}")

student_List = []
numOfStudent = int(input("Enter number of Student: "))
for i in range(numOfStudent):
    S_Name = input(f"Enter student {i + 1} name: ")    #{i+1} idea source: NgvGiang
    S_Id = input(f"Enter student {i + 1} id: ")
    S_Dob = input(f"Enter student {i + 1} dob: ")
    student = Student(S_Name, S_Id, S_Dob)

    for course in course_List:
        mark = float(input(f"Enter mark for {S_Name} in course {course._get_name()}: "))
        student.input_mark(course._get_name(), math.floor(mark * 10) / 10)
    student_List.append(student)

for student in student_List:
    student.display()

Gpa_Display(student_List, course_List)




