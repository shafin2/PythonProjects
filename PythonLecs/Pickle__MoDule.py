#as we store veges to make pickle same pickle module save objects
#it is not recommmended to use you can use database which is better
import pickle

# # Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# # wb means binary file/it creates it
# fileobj = open(file, 'wb')
# # pickele.dump save cars in fileobj
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
fileobj.close()
print(mycar)
print(type(mycar))




