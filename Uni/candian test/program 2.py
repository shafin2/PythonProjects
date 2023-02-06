import random



def randomNo():
  rn = round(random.uniform(1,500),2)
  return rn

def createarray():
    rows, cols = (5, 8)
    arr = []
    for i in range(rows):
        col = []
    for j in range(cols):
        col.append(randomNo())
        arr.append(col)
    return arr


arr1=createarray()
arr2=createarray()
print(arr1)
print(arr2)