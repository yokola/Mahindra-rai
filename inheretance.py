student = shaym ghallay
age = 108
cid number = 122344566

teacher = Mahindra rai
age = 120
cid number = 11808002710

class person:
    def__init__(self,name,age;cid number):
    self.name = name
    self.age = age
    self.cid number = cid number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")  

    def eat(self):
        print(f"{self.name} is eating.")  

    def sleep(self):
        print(f"{self.name} is sleeping.")  

class student(person):
    def__init__(self,name,age,cid number):
    super().__init__(name,age,cid number): 
    self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."


class Teacher(Person):
    def __init__(self, name, age, cid_number, employee_id):
        super().__init__(name, age, cid_number)
        self.employee_id = employee_id

    def teach(self):
        return f"{self.name} is teaching."

print(student.walk()) 
print(student.eat())   
print(student.sleep())
print(student.study()) 

print(teacher.walk())  
print(teacher.talk())  
print(teacher.sleep()) 



   