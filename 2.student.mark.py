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


student_List = []
numOfStudent = int(input("Enter number of Student: "))
for i in range(numOfStudent):
    S_Name = input(f"Enter student {i + 1} name: ")    #{i+1} idea source: NgvGiang
    S_Id = input(f"Enter student {i + 1} id: ")
    S_Dob = input(f"Enter student {i + 1} dob: ")
    student = Student(S_Name, S_Id, S_Dob)

    for course in course_List:
        mark = float(input(f"Enter mark for {S_Name} in course {course._get_name()}: "))
        student.input_mark(course._get_name(), mark)
    student_List.append(student)

for student in student_List:
    student.display()



