# Python-loop
def censor(text,word):
    text=text.split()
    for i in range(0,len(text)):
         if text[i]==word:
            text[i]= "*" * len(word)
    newtext= " ".join(text)
    return newtext
text=raw_input("Enter Text")
word=raw_input("Enter word")
print censor(text,word)
