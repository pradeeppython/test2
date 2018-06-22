#Write a program count duplicated elements in the list



def count_dupes(list1):

    d = {}
    
    for ele in list1:
        if ele in d:
            d[ele] = d[ele]+1
        else:
            d[ele] = 1
    return d    

list1 = ["pradeep","ram","rakesh","ram","pradeep","ram"]

print(count_dupes(list1))
