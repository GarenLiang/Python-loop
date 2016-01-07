# Python-loop
def reverse(text):
    TextReverse = ""
    Letter = len(text)
    while Letter > 0:
        TextReverse += text[Letter-1]
        Letter -= 1
    return TextReverse
