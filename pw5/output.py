from domains.Student import Student 
def List_course(course_List):
    for Course in course_List:
        Course.display()
    
def List_student(student_List):
    for student in student_List:
        student.display()

def List_Gpa(student_List, course_List):
    gpa_list = [(student.Avg_gpa(course_List), student) for student in student_List]
    sorted_students = sorted(gpa_list, key=lambda x: x[0], reverse=True)
    for gpa, student in sorted_students:
        print(f"{student._get_name()} - GPA: {gpa}")