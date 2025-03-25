print("7-1")
carName = input("Which car do you want to rent? ")
print("Let mee see if I can fing you a", f"{carName}")


print("7-2")
peopleNum = input("How many people in resturant ? ")
peopleNum = int(peopleNum)  # 字符串转换为int类型
if peopleNum >= 8 :
    print("Current people is ", peopleNum, " not have spare sit")
else:
    print("Current people is ", peopleNum,  "you can in !")



print("7-3")
num = input("Input one number ")
num = int(num)
if num % 10 == 0 :
    print("good one")
else:
    print("bad one")


print("7-4")

activeFg = True
while activeFg:
    ingredients = input("Input one ingredient ")
    if ingredients != 'quit':
        print("We will add ", f"{ingredients}", "in pizza~")
    else:
        activeFg = False

print("7-5")

while True:
    age = input("Input your age ")
    age = int(age)
    if age < 3:
        print("Free to watch movie")
    elif age <=  12:
        print("$10 to watch movie")
    elif age > 15:
        print("$15 to watch movie")

    result = input("If want to continue query (yes/no)")
    if result.upper() == 'YES':
        continue
    else:
        print("END!!")
        break


print("7-8")

sandwich_order = ["aa", "bb", "cc", "特制披萨"]
finish_sandwich_order = []
while sandwich_order:
    temp = sandwich_order.pop()
    print(f"I make your {temp} sandwich")
    finish_sandwich_order.append(temp)

print("finish_sandwich_order is ", finish_sandwich_order)
print("sandwich_order is ", sandwich_order)




print("7-8")

sandwich_order = ["aa", "特制披萨" , "bb", "cc", "特制披萨" ,"dd", "ee"]
finish_sandwich_order = []
i = 0
while "特制披萨" in sandwich_order:
    temp = sandwich_order.pop()  ## 每pop一次，列表的长度减少1个
    print(f"I make your {temp} sandwich")
    finish_sandwich_order.append(temp)


print("特制披萨 卖完了")
print("我做了哪些 ", finish_sandwich_order)
print("还剩下 ", sandwich_order)

print("7-10")
allPlaces = []
while True:
    temp = input("If you could visit one place in the world ,where would you go ")
    if temp == "quit":
        break
    allPlaces.append(temp)
i = 1
for place in allPlaces:
    print(i, "--", place)
    i += 1

print("使用用户输入填充字典")

dictionary = {}
activeFg = True
while activeFg:
    key = input("Enter a key: ")

    if key == "quit" :
        print("Wrong key")
        activeFg =False
        continue

    value = input("Enter a value: ")
    value = int(value)
    dictionary[key] = value

for key, value in dictionary.items():
    print(f"{key} maping to",value)
