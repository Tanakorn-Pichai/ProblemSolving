def sequential_Search(alist, item):
    pos = 0
    found = False
    while pos<len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0] 
print(sequential_Search (testlist, 3))
print(sequential_Search (testlist, 13))