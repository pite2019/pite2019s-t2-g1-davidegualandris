# CLASS to represent the students
class Student:

    # constructor
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self. surname = surname

    def filter_students(self, names):
        if (self.students):
            return True
        else:
            return False

    # print the student
    def __str__(self):
        return "Student number " + str(self.id) + ": " + str(self.name) + " " + str(self.surname)

    # when two instances equals? when they have the same 'id'
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id
        return False


# CLASS to "store" the students in a specific 'class'
class Class:

    # constructor
    def __init__(self, id, students=list()):
        self.id = id
        self.students = students

    def __len__(self):
        return len(self.students)

    def __getitem__(self, key):
        return self.students[key]

    # function to check whether a student is registered in this class
    def find_student(self, student_id):
        i = 0
        for stud in self.students:
            if student_id == stud.get('student'):
                return i
            i += 1
        return -1

    # add a new student to the class
    def add_student(self, student_id, attendances=0, grades=list()):
        # check if the student is already in the class
        if self.find_student(student_id) != -1:
                return 0

        # if not, add a new student
        new_student = {
                    'student': student_id,
                    'attendances': attendances,
                    'grades': grades
        }
        self.students.append(new_student)
        return 1

    def remove_student(self, student_id):
        # check if the student is in the class
        index = self.find_student(student_id)

        # if there is, delete him/her
        if index != -1:
            del self[index]
            return 1

        # otherwise
        return 0

    def add_attendance(self, student_id, atd=1):
        # check if the student is in the class
        index = self.find_student(student_id)

        # if there is, update him/her attendances
        if index != -1:
            self[index]["attendances"] += atd
            return 1

        # otherwise
        return 0

    def add_grade(self, student_id, grade):
        # check if the student is in the class
        index = self.find_student(student_id)

        # if there is, add the grade
        if index != -1:
            self[index]["grades"].append(grade)
            return 1

        # otherwise
        return 0

    def student_average(self, student_id):
        # check if the student is in the class
        index = self.find_student(student_id)

        # if there is, calculate
        if index != -1:
            grd = self[index]["grades"]
            return sum(grd)/len(grd)

        # otherwise
        return -1

    def student_attendance(self, student_id):
        # check if the student is in the class
        index = self.find_student(student_id)

        # if there is, calculate
        if index != -1:
            return self[index]["attendances"]

        # otherwise
        return -1

    # print the class
    def __str__(self):
        str_class = "ID of the class: " + str(self.id) + ". " + str(len(self.students)) + " students: \n"
        for stud in self.students:
            str_class += "Student ID " + str(stud.get('student')) + ". " + str(stud.get('attendances')) +\
                         " attendances. Grades: " + str(stud.get('grades')) + "\n"
        return str_class


# UTILITY FUNCTIONS

def search_id(list, id):
    c = 0
    for l in list:
        if l.id == id:
            return c
        c += 1
    return -1


def print_list(list):
    if len(list) == 0:
        print("Empty list")
    else:
        for l in list:
            print(l)
    return


# 0 to add student to a class, 1 to remove from the class
# 2 to add attendances, 3 to add grade, 4 to see the total average
def student_class_operation(choice):
    while True:  # check the id
        try:
            class_id = int(input('Class ID:'))
            cl = search_id(classes, class_id)
            if cl == -1:
                print("No class founded")
                continue
            else:
                break
        except ValueError:
            print("Insert numeric value")
            continue

    while True:
        try:
            student_id = int(input('Student ID:'))
            st = search_id(students, student_id)
            if st == -1:
                print("No student founded")
                continue
            else:
                break
        except ValueError:
            print("Insert numeric value")
            continue

    if choice == 0:
        return classes[cl].add_student(student_id)
    elif choice == 1:
        return classes[cl].remove_student(student_id)
    elif choice == 2:
        while True:
            try:
                att = int(input('Number of attendances more:'))
                if att <= 0:
                    print("The number should be more then 0")
                    continue
                break
            except ValueError:
                print("Insert numeric value")
                continue
        return classes[cl].add_attendance(student_id, att)
    elif choice == 3:
        while True:
            try:
                grd = int(input('Grade:'))
                if grd <= 0:
                    print("The grade should be more then 0")
                    continue
                break
            except ValueError:
                print("Insert numeric value")
                continue
        return classes[cl].add_grade(student_id, grd)
    elif choice == 4:
        return classes[cl].student_average(student_id)

    return

# 0 to get student total average, 1 to get student total attendances
def student_statistic(choice, student_id = -1):
    if student_id == -1:
        while True:
            try:
                student_id = int(input('Student ID:'))
                st = search_id(students, student_id)
                if st == -1:
                    print("No student founded")
                    continue
                else:
                    break
            except ValueError:
                print("Insert numeric value")
                continue

    att = 0
    sm = 0
    grd = 0
    for cl in classes:
        index = cl.find_student(student_id)
        if index != -1:
            att += cl[index]["attendances"]
            sm += sum(cl[index]["grades"])
            grd += len(cl[index]["grades"])

    if choice == 0:
        if grd == 0:
            return -1
        return sm/grd
    elif choice == 1:
        return att


def filter_attendances(std):
    if student_statistic(1, std.id) >= 10:
        return True
    else:
        return False


# MAIN PROGRAM
if __name__ == '__main__':
    import json

    students = list()
    classes = list()

    # load the data
    with open('school.json') as json_file:
        try:
            data = json.load(json_file)
            for s in data['students']:
                students.append(Student(s["id"], s["name"], s["surname"]))
            for c in data['classes']:
                classes.append(Class(c["id"], c["students"]))
            print("Data loaded")
        except ValueError:
            print("Nothing to load")

    # start the program
    while True:
        print("Select which operation you want to perform")
        print("1 to create a student")
        print("2 to see the students")
        print("3 to create a class")
        print("4 to see the classes")
        print("5 to add student to a class")
        print("6 to remove student from a class")
        print("7 to add student's attendances to a class")
        print("8 to add student's grade to a class")
        print("9 to see a student's total average score")
        print("10 to see a student's total attendances")
        print("11 to see a student's average score in a class")
        print("12 to see students with more then 10 total attendances")
        print("Everything else to exit the program")

        try:
            # make your choice
            option = int(input('Insert choice \n'))
            if option == 1:
                while True:  # check the id
                    try:
                        tmp_id = int(input('Student ID:'))
                        if search_id(students, tmp_id) == -1:
                            break
                        else:
                            print("ID already used")
                    except ValueError:
                        print("Insert numeric value")
                        continue
                tmp_name = input('Student name:')
                tmp_surname = input('Student surname:')
                students.append(Student(tmp_id, tmp_name, tmp_surname))
                print('Student added')
            elif option == 2:
                print_list(students)
            elif option == 3:
                while True:  # check the id
                    try:
                        tmp_id = int(input('Class ID:'))
                        if search_id(classes, tmp_id) == -1:
                            classes.append(Class(tmp_id))
                            break
                        else:
                            print("ID already used")
                    except ValueError:
                        print("Insert numeric value")
                        continue
                print('Class added')
            elif option == 4:
                print_list(classes)
            elif option == 5:
                res = student_class_operation(0)
                if res == 1:
                    print('Student added')
                else:
                    print('Student already in the class')
            elif option == 6:
                res = student_class_operation(1)
                if res == 1:
                    print('Student removed')
                else:
                    print('Student not in the class')
            elif option == 7:
                res = student_class_operation(2)
                if res == 1:
                    print('Attendances updated')
                else:
                    print('Student already in the class')
            elif option == 8:
                res = student_class_operation(3)
                if res == 1:
                    print('Grade added')
                else:
                    print('Student not in the class')
            elif option == 9:
                res = student_statistic(0)
                if res == -1:
                    print("No grades available")
                else:
                    print("Avarage: " + str(res))
            elif option == 10:
                res = student_statistic(1)
                print("Total attendances: " + str(res))
            elif option == 11:
                avg = student_class_operation(4)
                if avg == -1:
                    print("Student doesn't found in the class")
                else:
                    print("Average: " + str(avg))
            elif option == 12:  # use 'filter
                filtered = filter(filter_attendances, students)
                print('The students are:')
                for s in filtered:
                    print(s)
            else:
                break
        except ValueError:
            # wrong input == exit
            break

    # save the data
    data = dict()
    data['students'] = []
    for stud in students:
        data['students'].append({
            'id': stud.id,
            'name': stud.name,
            'surname': stud.surname
        })

    data['classes'] = []
    for cls in classes:
        data['classes'].append({
            'id': cls.id,
            'students': cls.students
        })

    with open('school.json', 'w') as outfile:
        json.dump(data, outfile)
        print("Data saved")
