# 2.1
myList = []
i = 0
while i <= 50:
    myList.append(i)
    i += 1

# 2.2
def squareList(lis):
    i = 0
    while i < len(lis):
        lis[i] = lis[i] * lis[i]
        i += 1
    return lis

print(squareList(myList))

# 2.3
def oddList(list1, list2):
    oddList = []
    for i in list1:
       if i % 2 != 0:
          oddList.append(i)
    for i in list2:
       if i % 2 != 0:
          oddList.append(i)
    return oddList

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [20,21,22,23,24,25,26,27,28,29,30]
print(oddList(list1,list2))

# 3.1
list2d = []
i = 0 
j = 0
value = 1
while i < 5:
    list2d.append([])
    while j < 5:
        list2d[i].append(value)
        value += 1
        j += 1
    i += 1
    j = 0
print(list2d)

# 3.2
i = 0
j = 0
while i < 5:
    while j < 5:
        if list2d[i][j] % 3 == 0:
            list2d[i][j] = '?'
        j += 1
    j = 0 
    i += 1 # Error - forgot to update i --> infinite loop 
print(list2d)

# 4
def removeDuplicates(lis):
    newList = []
    for i in lis:
        duplicate = False
        for j in newList:
            if i == j:
                duplicate = True
        if duplicate == False:
            newList.append(i)
    return newList

myList = [1,1,2,2,2,3,4,5,5,6,7,7,7]
print(removeDuplicates(myList))
