def reverse_method_1(lst):
    #build function method
    #making list copy
    a=lst[:]
    a.reverse()
    print("Reversed list no 1" ,a)
def reverse_method_2(lst):
    #slicing
    print("Reversed list no 2",lst[::-1])
def reverse_method_3(lst):
    b=lst
    #swapping
    for i in  range(len(b)//2):
        b[i],b[len(b)-i-1]=b[len(b)-i-1],b[i],
    print("Reversed list no 3",b)
if __name__ == '__main__':
    print("how many items are there in your list?")
    no_of_items = input()
    lst = []
    for i in range(1, int(no_of_items) + 1):
        print(f"Enter your item no {i}")
        list_items = input()
        lst.append(list_items)
    print("Your list", lst)
    reverse_method_1(lst)
    reverse_method_2(lst)
    reverse_method_3(lst)
