from input import Input_Course
from output import List_course
from input import Input_Student
from output import List_student
from input import Input_Mark
from output import List_Gpa

def main():
    numOfCourse = int(input("Enter number of Course: "))

    course_List = Input_Course(numOfCourse)

    course = List_course(course_List)

    numOfStudent = int(input("Enter number of Student: "))
    
    student_List = Input_Student(numOfStudent)
    
    Mark = Input_Mark(student_List ,course_List)

    student = List_student(student_List)
    
    List_Gpa(student_List, course_List)

if __name__ == "__main__":
    main()


