#you make generator by yield
#print(type(a))
def awein(n):
    for i in range(n):
        yield i

a=awein(50000)

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

