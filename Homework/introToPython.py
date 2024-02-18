
#if statements
x = 12
if (x != 4):
    print("hi")
else:
    print("hello")

#while loops
i = 10
while i > 0:
    print(i)
    i -= 1

#for loops
i = 10
for i in range (1,11): #inclusive, exclusive
    print(i)

#lists
myList = ['apple', 'banana', 'pineapple']
myLength = len(myList) 
fruit1 = myList[0]
fruitLast = myList[-1]
print(myList[-2:-1])
myList[0] = 'grape'
myList[1:2] = ['watermelon', 'lemon']
print(myList)
#adding to list
myList.insert(2, 'grapefruit') #adds to specific location
myList.append('orange') #adds to last
myList2 = ['mango', 'pear']
myList.extend(myList2) #adds another list to end
#removing from list
myList.remove("pear")
myList.pop(0) #removes certain index
myList.clear() #clears list

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] 
print(newlist) #["apple", "banana", "mango"]

finalList = fruits + newlist

#Dictionaries
thisdict = {"brand" : "Ford", "model" : "Mustang", "year" : 1964}
print(thisdict)
#{"brand" : "Ford", "model" : "Mustang", "year" : 1964}
#updating dictionary
thisdict.update({"year" : 2020})
#adding
thisdict["model"] = "red"
#{"brand" : "Ford", "model" : "Mustang", "year" : 2020, "color" : "red"}
#removing items
thisdict.pop("model") #removes pair




