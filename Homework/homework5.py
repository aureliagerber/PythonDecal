import numpy as np

# Part 1
print('Part 1: \n')
def equalArr(arr):
    equalArr = []
    for i in arr:
        num = i[0]
        allEqual = True
        for j in i:
            if j != num:
                allEqual = False
        if allEqual:
            equalArr.append(list(i))
    return equalArr

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
print(equalArr(arr))
    
# Part 2
print('\nPart 2: \n')
arr2 = np.zeros((8, 8), dtype = int)
arr2[0::2, 0::2] = 1 # for every even row... Row: start at 0, every 2 rows  Column: starts at 0, every 2 columns
arr2[1::2, 1::2] = 1 # for odd even row... Row: start at 1, every 2 rows  Column: starts at 1, every 2 columns
print(arr2)
#[start:end:step]

# Part 3
print('\nPart 3: \n')
myarr = np.array(['python', 'is', 'cool!'])
def spaceBetween(arr): #need to make new numpy array with different dimensions
    newArr = []
    for i in arr:
        newWord = ''
        for j in i:
            if i.index(j) < len(i) - 1:
                newWord += j + ' '
            else:
                newWord += j
        newArr.append(newWord)
    return np.array(newArr)

print(spaceBetween(myarr))

# Part 4
print('\nPart 4: \n')
np.random.seed(12345)
a = np.random.randint(1, 50, (4, 5))

def sorting(arr):
    rows = arr.shape[0] # # of rows
    columns = arr.shape[1] # # of columns
    # first create arrays of column numbers
    col = 0
    for col in range(columns):
        row = 0
        index = 0
        colArr = np.zeros(rows)
        for row in range(rows):
            colArr[index] = arr[row][col]
            row += 1
            index += 1
        colArr.sort()
        
        row2 = 0
        for row2 in range(rows):
            arr[row2][col] = colArr[row2]
            row2 += 1
        col += 1
    return arr

print(sorting(a))
##arr3 = np.array([3, 2, 7, 1], [4, 5, 2, 1])
#print(sorting(arr3))
