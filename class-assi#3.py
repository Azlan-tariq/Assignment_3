

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = {}

    def enroll_course(self, course):
        self.courses[course.course_code] = {"course": course, "grades": {}}

    def submit_grade(self, course_code, grade):
        if course_code in self.courses:
            self.courses[course_code]["grades"] = grade
        else:
            print(f"Student {self.name} is not enrolled in the course with code {course_code}.")

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0

        for course_info in self.courses.values():
            course = course_info["course"]
            grades = course_info["grades"]
            credits = course.credits

            if grades:
                total_credits += credits
                total_points += grades * credits

        if total_credits > 0:
            return total_points / total_credits
        else:
            return 0.0


class Professor(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def grade_student(self, student, course_code, grade):
        if course_code in student.courses:
            student.submit_grade(course_code, grade)
        else:
            print(f"Student {student.name} is not enrolled in the course with code {course_code}.")


class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits


# objects are given below:

# Creating instances of classes
student1 = Student("Azlan Tariq", 20, "S001")
professor1 = Professor("Alyan", 45, "P001")
course1 = Course("C001", "Software construction and development", 3)

# Enrolling student in a course
student1.enroll_course(course1)

# Professor grading a student
professor1.grade_student(student1, "C001", 90)

# Calculating GPA for the student
gpa = student1.calculate_gpa()

# Displaying information
student1.display_info()
professor1.display_info()
print(f"Student's GPA: {gpa}")
