#Write a program find a maximum number in the given input integer list.

def max_num(list1):
    myMax = list1[0]
    for num in list1:
        if myMax < num:
            myMax = num
    return myMax

list1 = []
num = int(input("range of list: "))
for i in range(num):
    i = int(input("enter new number:"))
    list1.append(i)
print (max_num (list1))
