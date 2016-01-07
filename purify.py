# Python-loop
def purify(uInput):
    even = []
    for i in uInput:
        if (i % 2 == 0):
            even.append(i)
    return even
    
print purify([1,2,3])
