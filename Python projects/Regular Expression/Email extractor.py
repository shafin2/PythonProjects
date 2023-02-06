#Following program extracts email
#You can extract email by giving your string,text file,or any web url
import requests
import re
def extract_email(str):
    patt = re.compile(r'[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+')
    matches = patt.findall(str)
    for match in matches:
        print(match)
    while(True):
        print("Do you want to save that email address in any file")
        print("Press 1 for yes or 2 for no")
        user_input = input()
        if user_input == "1":
            save_email(matches)
            break
        elif user_input == "2":
            print("Email is not save in any file")
            break
        else:
            print("Wrong input,Try again")
def save_email(emails):
    print("Enter the file path where you want to save email address")
    file_path=input()
    f=open(file_path,"a")
    for email in emails:
        f.write(f"\n{email}")
    f.close()
    print("Your email address are save in ",file_path)
if __name__ == '__main__':
    print("Hey,this program helps you to find email addresses")
    print("You can give string,file or url, and this program extract all "
          "email addresses that are in your string,file and on website")
    while (True):
        print("Press 1 for giving string,2 for giving file path,"
              "3 for giving website url and 4 for end the program")
        user_input = input()
        if user_input == "1":
            print("Note:if your string consist on two or more "
                  "lines ,it's request to save in file and "
                  "try by giving path")
            print("If not then pls enter the string")
            user_data = input()
            extract_email(user_data)
        elif user_input == "2":
            print("Please enter the File path")
            user_data = input()
            # E:\fazool\s.txt
            f = open(user_data, "r")
            file_data = f.read()
            f.close()
            extract_email(file_data)
        elif user_input == "3":
            print("Please enter the website url")
            user_data = input()
            # url="http://www.hamadrana.live/"
            url = requests.get(user_data).text
            extract_email(url)
        elif user_input == "4":
            break
        else:
            print("You entered wrong input")
            print("Try again")
            continue



