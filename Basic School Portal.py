class Person():

    def __int__(self,name="boş",lastname="boş",age=0):
        self.name = name
        self.lastname = lastname
        self.age = age

    def showinfo(self):
        print("Person's information...")
        print("Name: {} \nLastname: {} \nAge: {}".format(self.name,self.lastname,self.age))


class Student(Person):

    def __init__(self,name,lastname,age,studentid,paycheck):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.studentid = studentid
        self.paycheck = paycheck

    def showinfo(self):
        print("Student's information...")
        print("Name: {} \nLastname: {} \nAge: {} \nStudent Id: {} \nPaycheck: {}".format(self.name,self.lastname,self.age,self.studentid,self.paycheck))

    def changename(self,newname):
        self.name = newname
        print("Name has been changed")

    def changelastname(self,newlastname):
        self.lastname = newlastname
        print("Lastname has been changed")

    def changeage(self,newage):
        self.age = newage
        print("Age has been changed")

    def changestudentid(self,newid):
        self.studentid = newid
        print("Student's Id has been changed")

    def changepaycheck(self,newstatu):
        self.paycheck = newstatu
        print("Student's Paycheck statu has been changed")

class Teacher(Person):

    def __init__(self,name,lastname,age,teacherid,salary):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.teacherid = teacherid
        self.salary = salary

    def changename(self,newname):
        self.name = newname
        print("Name has been changed")

    def changelastname(self,newlastname):
        self.lastname = newlastname
        print("Lastname has been changed")

    def changeage(self,newage):
        self.age = newage
        print("Age has been changed")

    def showinfo(self):
        print("Teacher's information...")
        print("Name: {} \nLastname: {} \nAge: {} \nTeacher Id: {} \nSalary: {} tl".format(self.name,self.lastname,self.age,self.teacherid,self.salary))

    def changeteacherid(self,newid):
        self.teacherid = newid
        print("Teacher Id has been changed")


    def changesalary(self,newsalary):
        self.salary = newsalary
        print("Teacher's salary has been changed")

while True:
    print("""*******************************************
    
    Welcome to Yakut University Portal...
    
    *******************************************
    
    Please choose your operation...
    
    Press 1 for Registeration of Student
    Press 2 for Change Information of Student
    Press 3 for Registeration of Teacher
    Press 4 for Change Information of Teacher
    Press anything else for QUIT...
    
    *******************************************
    
    """)
    x = int(input("Your Operation is: "))

    if x==1:
        student_name = input("Student's name: ")
        student_lastname = input("Student's lastname: ")
        student_age = int(input("Student's age: "))
        student_id = int(input("Student's id: "))
        student_paycheck = input("Student's paycheck (If you paid please write Yes, otherwise write No): ")
        student1 = Student(student_name,student_lastname,student_age,student_id,student_paycheck)

    elif x==2:
        while True:
            print("""*******************************************

            Please choose the Object that you wanted to change...
            
            Press 1 for Display Student's Information
            Press 2 for Change Student's Name
            Press 3 for Change Student's Lastame
            Press 4 for Change Student's Age
            Press 5 for Change Student's Student Id
            Press 6 for Change Student's Paycheck
            Press anything else for QUIT...
            
            *******************************************
            
            """)
            y = int(input("Choose your operation: "))
            if y==1:
                student1.showinfo()
            elif y==2:
                newname1 = input("Please write student's name again: ")
                student1.changename(newname1)
            elif y==3:
                newlastname1 = input("Please write students's lastname again: ")
                student1.changelastname(newlastname1)
            elif y==4:
                newage1 = int(input("Please write student's age again: "))
                student1.changeage(newage1)
            elif y==5:
                newid1 = int(input("Please write student's id again: "))
                student1.changestudentid(newid1)
            elif y==6:
                newstatu1 = input("Please write student's paycheck statu again: ")
                student1.changepaycheck(newstatu1)
            else:
                print("Quiting from the portal...")
                break
    elif x==3:
        teacher_name = input("Teacher's name: ")
        teacher_lastname = input("Teacher's lastname: ")
        teacher_age = int(input("Teacher's age: "))
        teacher_id = int(input("Teacher's id: "))
        teacher_salary = int(input("Teacher's Salary:  "))
        teacher1 = Teacher(teacher_name, teacher_lastname, teacher_age, teacher_id, teacher_salary)
    elif x==4:
        while True:
            print("""*******************************************

            Please choose the Object that you wanted to change...

            Press 1 for Display Teacher's Information
            Press 2 for Change Teacher's Name
            Press 3 for Change Teacher's Lastame
            Press 4 for Change Teacher's Age
            Press 5 for Change Teacher's Teacher Id
            Press 6 for Change Teacher's Salary
            Press anything else for QUIT...
            
            *******************************************
            
            """)
            y = int(input("Choose your operation: "))
            if y == 1:
                teacher1.showinfo()
            elif y == 2:
                newname1 = input("Please write teacher's name again: ")
                teacher1.changename(newname1)
            elif y == 3:
                newlastname1 = input("Please write teacher's lastname again: ")
                teacher1.changelastname(newlastname1)
            elif y == 4:
                newage1 = int(input("Please write teacher's age again: "))
                teacher1.changeage(newage1)
            elif y == 5:
                newid1 = int(input("Please write teacher's id again: "))
                teacher1.changeteacherid(newid1)
            elif y == 6:
                newsalary1 = int(input("Please write teacher's salary again: "))
                teacher1.changesalary(newsalary1)
            else:
                print("Quiting from the portal...")
                break
    else:
        print("Quiting from portal...")
        break








