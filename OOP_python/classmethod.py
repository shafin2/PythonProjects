class student:
    no_of_leave= 8
    def __init__(self,name,grade,rollno):
        self.name=name
        self.grade=grade
        self.roll=rollno
    @classmethod
    def increase_leave(cls,leave):
        cls.no_of_leave=leave

Aneeq=student("Aneq",9,"23")
Aneeq.increase_leave(45)
print(Aneeq.no_of_leave)