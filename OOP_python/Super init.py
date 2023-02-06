class alpha:
    vd="I am in alpha"
    def __init__(self):
        self.vd="I am in alpha's constructor"
class beta(alpha):
    def __init__(self):
        super().__init__()
        self.vd2="I am in beta"
a=alpha()
b=beta()
print(b.vd)