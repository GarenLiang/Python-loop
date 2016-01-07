# Python-loop
def remove_duplicates(alist):
    hold = []
    for item in alist:
        if item not in hold:
            hold.append(item)
    return hold
