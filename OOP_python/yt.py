# class employee:
#     incremen=1.7
#     @classmethod
#     def incr(cls, e):
#         cls.incremen = e
#     def __init__(self,name,age):
#         self.a=name
#         self.b=age
#     def inc(self):
#         self.b=self.b*employee.incremen
#
# emp1=employee("name1",10)
# emp2=employee("name2",35)
# print(emp1.b)
# emp1.inc()
# print(emp1.b)
# employee.incr(5)
# emp1.inc()
# print(emp1.b)



#
# class employee:
#     def __init__(self,name,email,salary):
#         self.n=name
#         self.e=email
#         self.s=salary
#     def salary_increase(self,increment):
#         self.s=self.s * self.increment
# shafin=employee("shafin","shag@gmail.com",5000)
# aniq=employee("Aniq","saniag@gmail.com",3000)
#
# print(shafin.s)
# shafin.salary_increase(2)
# print(shafin.s)
# print(aniq.s)






# Starting Again




class employee:
    increment = 1.5
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def increase(self):
        self.salary=int(self.salary * self.increment)
    @classmethod
    def change_increment(cls,incr):
        cls.increment=incr
    @classmethod
    def From_str(cls,emp_str):
        name,age,salary=emp_str.split("-")
        return cls(name, age, salary)
    @staticmethod
    def is_open(day):
        if day=="sunday":
            return False
        else:
            return True
    #Dunders/Magic methods
    def __add__(self, other):
        return self.salary+other.salary
    def __repr__(self):
        return "Employee ({},{},{})".format(self.name,self.age,self.salary)
    def __str__(self):
        return self.name


#Inheritance
class programmer(employee):
    def __init__(self,name,age,salary,lang,ex):
        super().__init__(name,age,salary)
        self.lang=lang
        self.ex=ex
    def increase(self):
        self.salary=int(self.salary * self.increment) + 2000





aneeq=employee("Aneeq",16,50000)
shafin=programmer("shafin",18,60000,"python",5)
# print("shafin",shafin.salary)
# shafin.increase()
# print(shafin.salary)
# print("Aneeq",aneeq.salary)
# aneeq.increase()
# print(aneeq.salary)
#
# print(shafin.ex)




#
# day=input()
# print(employee.is_open(day))
# urwa=employee.From_str("Urwa-9-8000")
# aneeq=employee("Aneeq",16,20000)
# zayan=employee("zayan",13,10000)
#
# print(urwa.salary)
# urwa.increase()
# print(urwa.salary)
# urwa.change_increment(2)
# urwa.increase()
# print(urwa.salary)





print(repr(shafin))
print(str(shafin))

































