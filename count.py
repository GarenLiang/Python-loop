# Python-loop
def count(sequence, item):
    found = 0
    seq_list = []
    for i in sequence:
        print i
        if i == item:
            found += 1
    print found
    return found

count('I am I am am', 'am')
