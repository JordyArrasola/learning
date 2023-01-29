#recap our primitives
#int, boolean, float, string

variable = "jordy"
num = 0

#if statements

import random
num = random.randint(0, 100)
print("num is: " + str(num))

# #if statements need a boolean expression
# #if-else branch - note that you don't have to have an else
if (num < 50):
    print("num is below 50")
else:
    print("number is above 50")


num = random.randint(0, 75)
print("num is: " + str(num))

if num < 20:
    print("num is less than 20")
elif num < 40:
    print("num is less than 40")
elif num < 60:
    print("num is less than 60")
else:
    print("num is 60 or greater")




num = random.randint(0, 60)
print("num is: " + str(num))

#you can chain multiple boolean expressions in one if statement
#use keywords --> 'and' and 'or'
if num < 10:
    print("num is less than 10")
elif num > 10 and num < 20:
    print("num is between 10 and 20")
elif num > 30 and num < 40:
    print("num is between 30 and 40")
elif num > 40:
    print("num is more than 40")




#data structures - things that you hold data in
#primitives - integers, boolean, float, and strings
#lists are data structures that hold data

items = []
items.append(0)
items.append(10)
items.append(5)
items.append(34)

items.append("brett")
items.append("lucas")
items.append("jordy")
items.append("tyler")

#items.sort(reverse=True)
print(items)



items = []
items.append(4)
items.append(90)
items.append(6)
items.append(45)
items.append("jordy")
print(items)

first = items[0]
second = items[1]
third = items[2]

#while loop
#reads while [boolean expression] -> do this code

#looping over a data structure BY INDEXING
index = 0
length_of_list = len(items)
while(index < length_of_list):
    print("index is: " + str(index))
    print(items[index])
    index = index + 1

#for loop -> otherwise known as a for-each loop
#looping over a data structure BY ELEMENT
for item in items:
    print(item)



















