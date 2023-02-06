#To run following program you've needed three text files named "Details","Lended_books"and "library_file"
class library:
    def __init__(self,list_of_book,library_name):
        self.list_of_book=list_of_book
        self.library_name=library_name
    @staticmethod
    def getdate():
        import datetime
        return datetime.datetime.now()
    def display_book(self):
        # for item in list_of_book:
        #     print(item)
        print(list_of_book)
        f.close()
    @staticmethod
    def lend_book():
        print("It's suggestion to copy book name from display book and then paste\n"
              "Enter the book name :")
        lended_book=input()
        f = open("library_file", "r")
        selected_book = f.readlines()
        f.close()
        for check in selected_book:
            if check.strip("\n")==lended_book:
                w = open("library_file", "w")
                for book in selected_book:
                    if book.strip("\n") != lended_book:
                        w.write(book)
                w.close()
                # For details
                book_lend_by = open("Details", "a")
                content = "\n< " + lended_book + " > is lend by " + library_name + " at " + str(date)
                book_lend_by.write(content)
                book_lend_by.close()
                # specific detail about lended books only
                book_lend_by = open("Lended_books", "a")
                content = "\n< " + lended_book + " > is lend by " + library_name + " at " + str(date)
                book_lend_by.write(content)
                book_lend_by.close()
                print("Thanks! you've lended the book ")
                break
        else:
            print("That book is not available in library")
    @staticmethod
    def add_book():
        print("Add the book you want")
        added_book=input()
        add_book_in_file=open("library_file","a")
        book_content="\n"+added_book
        add_book_in_file.write(book_content)
        add_book_in_file.close()
        add_book_detail=open("Details","a")
        content = "\n"+ library_name + " added book < "+added_book+" > at " + str(date)
        add_book_detail.write(content)
        add_book_detail.close()
        print("Thanks! you've added ", added_book)
    @staticmethod
    def return_book():
        print("Return the book")
        returned_book= input()
        #again adding book
        add_book_in_file = open("library_file", "a")
        book_content = "\n" + returned_book
        add_book_in_file.write(book_content)
        add_book_in_file.close()
        add_book_detail = open("Details", "a")
        content = "\n" + library_name + " Retuned book < " + returned_book + " > at " + str(date)
        add_book_detail.write(content)
        add_book_detail.close()
        print("Thanks! we recieved it")
    @staticmethod
    def about_lended_books():
        lended_books=open("Lended_books","r")
        print(lended_books.read())
    @staticmethod
    def previous_log():
        detail=open("Details","r")
        print(detail.read())

print("Welcome to the Library")
print("Enter your name :")
library_name=input()
while(True):
    f = open("library_file", "r")
    list_of_book = f.read()
    lib_obj = library(list_of_book, library_name)
    date = lib_obj.getdate()
    print("\nType 1 for Display-Book ,2 for Lend-book,3 for add-book,4 for return book, \n"
          "5 for about who lended books,6 for previous log/details or for exit press any other key")
    user_input=input()
    if user_input=="1":
        lib_obj.display_book()
    elif user_input=="2":
        lib_obj.lend_book()
        # if lib_obj.lend_book()==False:
        #     print("Thanks! you've lended the book ")
        # else:
        #     print("Sorry,the book name you've entered is not in our library\n"
        #           "it's suggested that you should copy book name from display and then paste it")
    elif user_input=="3":
        lib_obj.add_book()
    elif user_input=="4":
        lib_obj.return_book()
    elif user_input=="5":
        lib_obj.about_lended_books()
    elif user_input=="6":
        lib_obj.previous_log()
    else:
        break