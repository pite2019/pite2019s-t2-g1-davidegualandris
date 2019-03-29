# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class ScoolGrades:

    #defining static variables
	
    
    #Defining the constructor
    
    def __init__(self, students_names, students_grades, students_attendance):
        self.students_names = students_names
        self.students_grades = students_grades
        self.students_attendance = students_attendance

    def get_average_score(self):
        sum = 0
        count = 0
        for grades in self.students_grades:
            for grade in grades:
                count += 1
                sum += grade
        return sum/count

    def get_students(self):
        return self.students_names

    def get_total_attendance(self):
        count = 0
        for attendance in self.students_attendance:
            count += attendance
        return count

    def get_student_average_score(self, student):
        sum = 0
        count = 0
        for grade in self.students_grades[self.students_names.index(student)]:
            count += 1
            sum += grade
        return sum/count

if __name__ == '__main__':
    scool1 = ScoolGrades(["a green", "b red", "c white"], [[3,4,5], [1,4,8], [5,8,9]], [5, 8, 9])
    print(scool1.get_average_score())
    print(scool1.get_students())
    print(scool1.get_total_attendance())
    print(scool1.get_student_average_score("a green"))
