# Write a program count number of occurrences of vowels in a given string

def vowel_count(word):
    vowels = "aeiou"
    
    d = {}
    
    for ch in word:
        if ch in vowels:
            d[ch] = d[ch] + 1
    return d
print(vowel_count("ambitious"))
