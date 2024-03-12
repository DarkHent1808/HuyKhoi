import numpy as np
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