#apple news api
#https://newsapi.org/v2/everything?q=apple&from=2022-01-27&to=2022-01-27&sortBy=popularity&apiKey=aa59059d8c4f4cdea01d4053242f1d70
import requests
import json
from win32com.client import Dispatch
def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)
url="https://newsapi.org/v2/everything?q=apple&from=2022-01-27&to=2022-01-27&sortBy=popularity&apiKey=aa59059d8c4f4cdea01d4053242f1d70"
news=requests.get(url).text
news_dict=json.loads(news)
articles=news_dict["articles"]
print("Welcome to news center. Today's news are")
speak("Welcome to news center. Today's news are")
for article in articles:
    print("Title of news : ",article["title"])
    speak("Title of news is ")
    speak(article["title"])
    print("Description : ", article["description"])
    speak("Description is ")
    speak(article["description"])
    print("For more detail go to",article["url"])
    speak("For more detail go to that link")
    print("\nNext news is\n")
    speak("Next news is")






















# import requests
# import json
# import time
# from win32com.client import Dispatch
#
# def speak(s):
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(s)
#
# data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=aa59059d8c4f4cdea01d4053242f1d70")
#
# result = data.json()
# print(result['status'])
# # print(result)
#
# news = result['articles']
#
# speak("Welcome to the News Channel")
# speak("Here are the top ten news")
# speak("So our first news is ")
# for i  in range(0,10):
#     print(i)
#     print(news[i]['description'])
#     speak(news[i]['description'])
#     if i>=9:
#         break
#     time.sleep(2)
#     if i == 8:
#         speak("So our last news for today is ")
#     else:
#         speak("Moving To Our next news")
#
#
# speak("Thanks for listening ! Have a nice day")
# speak("Keep coding")