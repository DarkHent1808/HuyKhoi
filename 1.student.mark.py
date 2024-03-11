def input_course_info():
    course_name = input("Enter course name: ")
    course_id = int(input("Enter course id: "))
    return {'Course Name': course_name, 'Course Id': course_id}

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(course['Course Name'])

def input_student_info():
    name = input("Enter student name: ")
    student_id = input("Enter student id: ")
    dob = input("Enter student dob (YYYY-MM-DD): ")
    return {'Name': name, 'Id': student_id, 'DOB': dob}

def list_students(students):
    print("List of Students:")
    for student in students:
        print(student['Name'])

def input_marks(courses, students):
    course_id = int(input("Enter course id: ")) - 1
    course = courses[course_id]
    print(f"Enter marks for course {course['Course Name']}:")
    for i, student in enumerate(students):
        mark = float(input(f"Enter mark for student {student['Name']}: "))
        course['Student Mark'][i] = mark

def list_marks(courses):
    print("List of Marks:")
    for course in courses:
        print(course['Course Name'] + ": " + str(course['Student Mark']))


numberOfStudents = int(input("Enter the number of students: "))
students = [input_student_info() for _ in range(numberOfStudents)]

numberOfCourses = int(input("Enter the number of courses: "))
courses = [{'Course Name': '', 'Course Id': i + 1, 'Student Mark': [0] * numberOfStudents} for i in range(numberOfCourses)]
for course in courses:
    course.update(input_course_info())

list_students(students)
list_courses(courses)

input_marks(courses, students)
list_marks(courses)

input_marks(courses, students)
list_marks(courses)
