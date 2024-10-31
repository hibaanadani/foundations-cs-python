class Course:
    def __init__(self,code,name,numbCred,courseType):
        self.code=code
        self.name=name
        self.numbCred=numbCred
        self.courseType= courseType
class Student():
    def __init__(self, name, ID):
        self.name=name
        self.ID=ID
        self.courses={}

    def enroll(self,course):
        if course.code not in courses_catalog:
            print(f"Error: Course {course.code} not found in catalog")
            return
        if course.code in self.courses:
            print(f"Course {course.name} already exists")
            return
        self.courses[course.code]=course
        print(f"{course.code} added to the courses list.")

    def drop(self,course):
        if course in self.courses:
            del self.courses[course]
        else:
            print(f"{course} not enrolled")

    def listcourses(self):
        return list(self.courses.values())

courses_catalog = {}
def add_course(code,name,numbCred,courseType):
    courses_catalog[code]= Course(code,name,numbCred,courseType)
    print(f"Course {name} ({code}) added successfully!")

def save(filename):
    with open(filename,'w') as file:
        for course in courses_catalog.values():
            file.write(f"{course.code},{course.name},{course.numbCred},{course.courseType}\n")
    print(f"Course catalog saved to {filename}")

def load_courses(filename):
    with open(filename, 'r') as file:
        for i in file:
            code, name, numbCred, courseType = i.strip().split(',')
            if code not in courses_catalog:
                courses_catalog[code] = Course(code, name, int(numbCred), courseType)
            else:
                print(f"Course {code} already exists in the catalog and was not added.")
    print("Loaded courses:")
    for course in courses_catalog.values():
        print(f"{course.code} - {course.name} ({course.numbCred} credit hours, {course.courseType})")


def main():
    students = {}
    while True:
        print("\nMenu:")
        print("1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Drop Course for Student")
        print("4. List Student Courses")
        print("5. Save Course Catalog")
        print("6. Load Course Catalog")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            code = input("Enter course code: ")
            name = input("Enter course name: ")
            credit_hours = int(input("Enter credit hours: "))
            course_type = input("Enter course type (core/elective): ")
            add_course(code, name, credit_hours, course_type)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            if student_id not in students:
                student_name = input("Enter student name: ")
                students[student_id] = Student(student_name, student_id)
            course_code = input("Enter course code to enroll in: ")
            if course_code in courses_catalog:
                students[student_id].enroll(courses_catalog[course_code])
            else:
                print(f"Error: Course {course_code} not found in catalog")
        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code to drop: ")
            students[student_id].drop(course_code)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            courses = students[student_id].listcourses()
            for course in courses:
                print(f"{course.code} - {course.name}")
        elif choice == '5':
            filename = input("Enter filename to save course catalog: ")
            save(filename)
        elif choice == '6':
            filename = input("Enter filename to load course catalog: ")
            load_courses(filename)
            print(f"Course catalog loaded from {filename}")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
