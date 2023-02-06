# That program open directory you enter then it capitalize first letter of all text files
#that are in that directory and numberig the jpg files
# E:\PycharmProjects\Python projects\Prettify the folder
import os
def jpg_function(files_are):
    i=1
    for file in files_are:
        jpg_file = file.split(".")
        if jpg_file[1] == "jpg":
            new_jpg = str(i) + file
            os.rename(file,new_jpg)
            i = i + 1
def txt_files(files_are,dont_change_file):
    for file in files_are:
        txt_file = file.split(".")
        if txt_file[1] == "txt":
            if file != dont_change_file:
                os.rename(file, file.capitalize())

if __name__ == '__main__':
    while(True):
        print("Enter the directory do you want to set")
        dir_name = input()
        check_dir = os.path.isdir(dir_name)
        if check_dir == True:
            os.chdir(dir_name)
            files_are = os.listdir(dir_name)
            print("Enter the file name that you dont want to change")
            dont_change_file = input()
            check_file = os.path.isfile(dont_change_file)

            if check_file == True:
                jpg_function(files_are)
                txt_files(files_are, dont_change_file)
                break
            else:
                print("That file does'nt exist")
                continue
        else:
            print("This directory does not exist")
            continue






