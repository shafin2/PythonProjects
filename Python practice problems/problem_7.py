import time
from datetime import datetime
def searching(search_word):
    lst = ["Python is awesome", "Python is not snake", "good or bad","web www.w3schools.com"]
    search_word.lower()
    result_found=0
    search_result=[]
    a= datetime.now()
    for item in lst:
        words = item.split(" ")
        for word in words:
            if search_word==word.lower():
                result_found = result_found + 1
                search_result.append(item)
                time.sleep(0.5)
        b=datetime.now()

    print(f"{result_found} results found in {b-a} time")
    for result in search_result:
        print(result)

if __name__ == '__main__':
    print("Search here ....")
    search_word = input()
    searching(search_word)






