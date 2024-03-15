from domains.Course import Course
from domains.Student import Student
import math

def Input_Course(numOfCourse):
    course_List = []
    course_File = open("course.txt", "w")
    for i in range(numOfCourse):
        C_Name = input(f"Enter course {i + 1} name: ")    #{i+1} idea source: NgvGiang
        C_Id = input(f"Enter course {i + 1} id: ")
        course_List.append(Course(C_Name, C_Id))
        course_File.write(f"Course name: {C_Name}, Course ID: {C_Id}\n")
    course_File.close()
    return course_List


def Input_Student(numOfStudent):
    student_List = []
    student_File = open("student.txt", "w")
    for i in range(numOfStudent):
        S_Name = input(f"Enter student {i + 1} name: ")    #{i+1} idea source: NgvGiang
        S_Id = input(f"Enter student {i + 1} id: ")
        S_Dob = input(f"Enter student {i + 1} dob: ")
        student = Student(S_Name, S_Id, S_Dob)
        student_List.append(student)
        student_File.write(f"Student name: {S_Name}, Student ID: {S_Id}, Student DOB: {S_Dob}\n")
    student_File.close()
    return student_List


def Input_Mark(student_List, course_List):
    mark_File = open("mark.txt", "w")
    for student in student_List:
        for course in course_List:
            mark = float(input(f"Enter mark for {student._get_name()} in course {course._get_name()}: "))
            student.input_mark(course._get_name(), math.floor(mark * 10) / 10)
            mark_File.write(f"Student {student._get_name()} in Course {course._get_name()}, Mark: {mark}\n")
    mark_File.close()
