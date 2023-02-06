#function caching
#function caching means if any function take 10 seconds to do a task
#when the function call so if the same function is call again
#it will take again 10 seconds
#to save that time we use function  caching
#
from functools import lru_cache
import time
a=input()
@lru_cache(maxsize=int(a))
#We use lru_cache decorator and maxsize mean it will save last 10 function calls
def sleep_fun():
    #Let this function take 10 seconds to do a task
    time.sleep(10)


print("hello")
sleep_fun()
print("hello again")
sleep_fun()
print("Calling the same function so it will not take time")

#
#
#



#coroutines


# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# print("search started")
# next(search)
# print("Next method run")
# search.send("harry")
#
# search.close()
# search.send("harry")
# # input("press any key")
# # search.send("harry and")
# # input("press any key")
# # search.send("thi si")
# # input("press any key")
# # search.send("joker")
# # input("press any key")
# # search.send("like this video")







