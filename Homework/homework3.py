#1
def power(x,y):
    num = x
    while y > 1:
        num = num * x
        y -= 1
    return num

#2
def minMax(numbers):
    min = numbers[0]
    max = numbers[0]
    for i in numbers:
        if i < min:
            min = i 
    for i in numbers:
        if i > max:
            max = i
    myTuple = (min,max)
    return myTuple

#3
def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

#4
def bmi(weight, height):
    return weight/(height**2)

#5
def rotate(num):
    lastNum = num % 10
    baseNum = num // 10
    return str(lastNum) + str(baseNum)

#6
def minFor(numbers):
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    return min

def minWhile(numbers):
    i = len(numbers) - 1
    min = numbers[0]
    while i >= 0:
        if numbers[i] < min:
            min = numbers[i]
        i -= 1
    return min

def maxFor(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max

def maxWhile(numbers):
    i = len(numbers) - 1
    max = numbers[0]
    while i >= 0:
        if numbers[i] > max:
            max = numbers[i]
        i -= 1
    return max

#7
def vowel(word):
    word = word.lower()
    vowelCount = 0
    vowelList = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        for j in vowelList:
            if i == j:
                vowelCount += 1
    return vowelCount

#8
def digiRoot(number):
    total = 0
    for i in str(number):
        total += int(i)
    return total



