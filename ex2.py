#2.Write a program reverse a given input string

def rev_str():
    str1 = input("enter a string: ")
    x = ''
    for ele in str1[::-1]:
        x = x + ele
    return x
print(rev_str())
