#ClASS
class student:
    no_of_leave= 8
    def __init__(self,name,grade,rollno):
        self.name=name
        self.grade=grade
        self.roll=rollno
    #Dunder method(for what do if + is used)
    #If + used then i want to add thier roll no
    def __add__(self, other):
        return self.roll+other.roll
    #for more you can search "mapping operator in function"
    #link for that also "https://docs.python.org/3/library/operator.html"

    #some more dunders for practice
    def __gt__(self, other):
        return self.roll > other.roll



    #Repr and str method
    def __repr__(self):
        return f"Student('{self.name}', {self.grade}, '{self.roll}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.grade} and role is {self.roll}"

#OBJECTS
Aneeq=student("Aneq",9,23)
zayan=student("Zyaan",10,56)




#DUNDER OUTPUT
print(Aneeq+zayan)
print(Aneeq<zayan)



#Repr and str
# str is by default
print(Aneeq)
print(repr(Aneeq))