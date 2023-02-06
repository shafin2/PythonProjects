class employee():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.address="gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    #when property decorator is used then you have no need to "()" to run functon
    def email(self):
        return f"{self.fname}.{self.lname}@{self.address}"

    #setter property is used when you have to set something
    # now emmail is setting
    @email.setter
    def email(self,string):
        #first of split string in two part one is befor @ and other is after @
        #intialize any var name and select [0] mean first part before @
        domaim=string.split("@")[0]
        self.address=string.split("@")[1]
        #then split this part in two parts with .
        self.fname=domaim.split(".")[0]
        self.lname=domaim.split(".")[1]
        #now retun as return in email() above
        return f"{self.fname}.{self.lname}@{self.address}"




zayan=employee("zayan","maqsood")
print(zayan.explain())
print(zayan.email)
zayan.fname="urwa"
print(zayan.email)
zayan.email="shafin.zaman@hotmail.com"
print(zayan.email)