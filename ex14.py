#Write a program print longest length string from given input list of strings. 

def longest_str(str_list):
    str_len = []
    for ch in str_list:
        str_len.append((len(ch), ch))
    str_len.sort()
    return str_len[-1][1]

num = int(input("enter list range:"))
str_list = []
for i in range(num):
    i = input("enter a string: ")
    str_list.append(i)
    

print(longest_str(str_list))
