#Write a program reverse the given input list

def rev_list():
    list1 = [0,1,2,3,4,5,6,7,8,9]
    x = []
    for ele in list1[::-1]:
        x.append(ele)
    return x
print(rev_list())
