class students:
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
    def display(self):
        print(f"Name:{self.name}\nMarks:{self.marks}\n Age:{self.age}")

student1= students("Punee",100,19)
student2=students("Chethan",98,20)
student3=students("shalini",99,18)
student1.display() 
student2.display()
student3.display()
