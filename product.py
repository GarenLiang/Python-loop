# Python-loop
def product(integers):
    length = len(integers)
    multiplier = 1
    for i in range(length):
        multiplier = multiplier * integers[i]
    return multiplier

print product([1, 2])
print product([2, 3, 5, 7, 11])
