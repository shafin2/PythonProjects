import random
def wrong_table(num):
    wrong_list=[]
    a=random.randint(3, 8)
    for i in range(1, 11):
        if i == a:
            wrong_list.append(num * i + 1)
        else:
            wrong_list.append(num * i)
    return wrong_list
def iscorrect(num,wrong_outputs):
    i=0
    for wrong_output in wrong_outputs:
        i=i+1
        if num * i == wrong_output:
            pass
        else:
            print(f"There is mistake in {num} * {i} = {wrong_output} "
                  f"\ncorrect form is {num} * {i} = {num*i} ")


if __name__ == '__main__':
    num = int(input("Enter the number : \n"))
    wrong_outputs=wrong_table(num)
    b=0
    print("Table is : ")
    for output in wrong_outputs:
        b=b+1
        print(f"{num} x {b} = {output}" )
    print("No! it's scam \n Alert!")
    iscorrect(num,wrong_outputs)
