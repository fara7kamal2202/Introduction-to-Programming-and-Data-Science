# ================================
# Exercise: Student Class
# ================================

# Task 1: Write a class called Student with the attributes name (str) and studyProgram (str)

class Student:
    def __init__(self, name:str, age:int, gender:str, study_program:str):
        self.name = name
        self.age = age
        self.gender = gender
        self.study_program = study_program

    def print_info(self):
        print(self.name, self.age, self.gender, self.study_program)


# ================================
# Task 2: Create three instances. One for yourself, one for your left neighbor and one for our right neighbor.
# ================================

farah = Student("Farah", 27, "Female", "Programming")
right_student = Student("right_student", 27, "Female", "Programming")
left_student = Student("left_student", 27, "Female", "Programming")


# ================================
# Task 3: Add a method printInfo that prints the name and studyProgram of a Student. Test your method on the objects!
# ================================

farah.print_info()
right_student.print_info()
left_student.print_info()


# ================================
# Task 4: Modify the code and add age and gender to the attributes. Modify your printing methods respectively too.
# ================================


