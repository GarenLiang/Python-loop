# Python-loop
def anti_vowel(text):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res=[]
    for i in text:
        if i not in vowel:
            res.append(i)
    return ''.join(res)
print(anti_vowel('Hey You!'))
