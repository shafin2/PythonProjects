import requests
import pickle
data=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text
file_name="data_fromserver.iu"
fileobj=open(file_name,'wb')
pickle.dump(data,fileobj)
fileobj.close()

fileobj2=open(file_name,'rb')
pickled_data=pickle.load(fileobj2)
fileobj2.close()
print(pickled_data)

