from input import Input_Course, Input_Student, Input_Mark
from output import List_course, List_student, List_Gpa
from zipfile import ZipFile, ZIP_DEFLATED

def main():
    numOfCourse = int(input("Enter number of Course: "))

    course_List = Input_Course(numOfCourse)

    course = List_course(course_List)

    numOfStudent = int(input("Enter number of Student: "))

    student_List = Input_Student(numOfStudent)

    Mark = Input_Mark(student_List ,course_List)

    student = List_student(student_List)

    List_Gpa(student_List, course_List)

    zip_path = 'AsWritten.zip'
    file_to_zip = ['./course.txt', './student.txt', './mark.txt']
    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip:
        for file in file_to_zip:
            zip.write(file)

if __name__ == "__main__":
    main()


