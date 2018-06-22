#Write a program convert all the vowels to uppercase
#for the given input string.

def vowels_upper():
    str1 = input("enter a string: ")
    x = '' 
    for ele in str1:
        if ele in 'aeiou':
            x = x + ele.upper()
        else:
            x = x + ele
            
    return x
print(vowels_upper())

