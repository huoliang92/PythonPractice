print("5-1")
car = "subaru"
if car == "subaru":
    print("Car is subaru")
else:
    print("Car is not subaru")

print("car == audi ?", car == "audi")


print("5-2")
word1 = "aaa"
word11 = "aaa"
word2 = "aab"
word3 = "AAA"

print("比较 word1 和 word11")
if word1 == word11:
    print("word1 == word11")
print("比较 word1 和 word2")
if word1 == word2:
    print("word1 == word2")
else:
    print("word1 != word2")

if word1 == word3:
    print("word1 == word3")
elif word1 == word3.lower():
    print("word1 == word3.lower()")

numListA = [1, 2, 3, 4, 5, 6, 7]
numListA.reverse()
numListB = numListA[:]
numListA.reverse()

if numListA[0] == numListB[-1]:
    print("numListA[0] = ", numListA[0])
if numListA[3] > numListB[5]:
    print("numListA[3] = ", numListA[3])
    print("numListB[5] = ", numListB[5])

number = 1
if (number == numListA[0]) and (number == numListB[6]):
    print("number ", number)

number = 5
if (number == numListA[0]) or (number == numListB[2]):
    print("number ", number)

number = 6
if number in numListA:
    print("number ", number, "in numListA");

number = 60
if number not in numListA:
    print("number ", number, "not in numListA");


print("5-3 4 5")
alien_color = "yellow"
if alien_color == "green":
    print("Got Green ,point 5")
elif alien_color == "yellow":
    print(f"Got Wrong Color {alien_color}", end="")
elif alien_color == "red":
    print(f"Got Wrong Color {alien_color}", end="")

print("5-6")
age = 64
if age <= 2:
    print("1you age is ", age)
elif age <= 4:
    print("2you age is ", age)
elif age <= 13:
    print("3you age is ", age)
elif age <= 20:
    print("4you age is ", age)
elif age < 65:
    print("5you age is ", age)
elif age >= 65:
    print("6you age is ", age)

print("5-7")

fruitList = ["A", "bb", "ccc"]
if "A" in fruitList:
    print("A in List")

temp = "BB"
if temp.lower() in fruitList:
    print("BB lower in List")

temp = "77"
if temp.lower() not in fruitList:
    print(f"{temp}  not in List")



print("5-8")
nameList = ["hl", "admin", "qqq"]
name = "hl"
if name in nameList and name == "admin":
    print(f"Hello {name}, you are good")
else:
    print(f"{name}, you are bad")


print("5-9")
nameList = ["hl", "admin", "qqq"]
if "hl" in nameList:
    print("remove hl")
    nameList.remove("hl")
if "admin" in nameList:
    print("remove admin")
    nameList.remove("admin")
if "qqq" in nameList:
    print("remove qqq")
    nameList.remove("qqq")

if nameList:
    print("你不对劲")
else:
    print("Null List ,need add")


print("5-10")
currentUserList = ["hl", "admin", "qqq", "aaa", "qwe", "A"]
newUserList = ["qQq", "aaa", "a", "B", "C"]

currentUserListForLow = []

for temp in currentUserList:
    currentUserListForLow.append(temp.lower())

print(currentUserListForLow)

for newUser in newUserList :
    if newUser.lower() in currentUserListForLow:
        print(newUser, "has bee used ")
    else:
        print(newUser, "not used ")


print("5-11")

numberList = list(range(1, 10))
print(numberList)
for temp in numberList:
    if temp == 1:
        print("1st")
    elif temp == 2:
        print("2rd")
    elif temp == 3:
        print("3rd")
    elif temp == 4:
        print("4th")
    elif temp == 5:
        print("5th")
    elif temp == 6:
        print("6th")
    elif temp == 7:
        print("7th")
    elif temp == 8:
        print("8th")
    elif temp == 9:
        print("9th")

