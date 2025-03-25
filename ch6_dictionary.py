print("6-1")
peopleInformation = {
    'firstName': "Liang",
    'LastName': "Huo",
    'Age': 28,
    'city': "佳木斯",
}

print(peopleInformation.items())

print("6-2")
peopleForLovingNumber = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
}
for key in peopleForLovingNumber.keys():
    print(f"Hello {key}.", f"Your choice number is {peopleForLovingNumber[key]}")

aNum = peopleForLovingNumber["C"]
print(aNum)
aNum = peopleForLovingNumber.get('A', "????")
print(aNum)
aNum = peopleForLovingNumber.get('Z', "????")
print(aNum)



print("6-3")
vo = {
    'c': "111",
    'c++': "222",
    'java': "333",
    'python': "444",
    'rust': "555",
}
keyList = vo.keys()
print(keyList)
for singleKey in keyList:
    print(f"{singleKey} :", f"{vo[singleKey]}")

print("6-4")
vo = {
    'c': "111",
    'c++': "222",
    'java': "333",
    'python': "444",
    'rust': "555",
}

for singleKey, singleValue in vo.items():
    print("First dictionary", f"{singleKey} :", singleValue)

vo["go"] = "666"
vo["php"] = "777"
for singleKey, singleValue in vo.items():
    print("Second dictionary", f"{singleKey} :", singleValue)

print("6-5")

vo = {
    '黑龙江省': "松花江",
    '江苏省': "长江",
    '河南省': "黄河",
}

for singleKey, singleValue in vo.items():
    print(f"{singleKey} ", "流淌着", singleValue)

for singleValue in vo.values():
    print("流淌着", singleValue)

for singleKey in vo.keys():
    print(singleKey)


print("6-6")
vo = {
    'c': "111",
    'c++': "222",
    'java': "333",
    'python': "444",
    'rust': "555",
}

nameList = ['python', 'c++']

for singleKey, singleValue in vo.items():
    print({singleKey}, "---", singleValue)
    if singleKey in nameList:
        print("[1]我正在学", singleValue)
        print("[2]我正在学", vo[singleKey])
    else:
        print(f"{singleKey}", "我不会啊")


for a in range(5):
    print(a) # 从0开始
    print("11") # 循环5次


print("6-7 8")
people1 = {
    'firstName': "Liang",
    'LastName': "Huo",
    'Age': 28,
    'city': "佳木斯",
}

people2 = {
    'firstName': "Liang",
    'LastName': "Hou",
    'Age': 27,
    'city': "杭州",
}

people3 = {
    'firstName': "Liang",
    'LastName': "Hu",
    'Age': 26,
    'city': "八五九",
}

allPeople = [people1, people2, people3]

for person in allPeople:
    print(person)

for person in allPeople:
    print(person['city'])


print("6-9/10")

favorite_place = {
    "p1": ["11", "12", "13"],
    "p2": ["21", "22", "23"],
    "p3": ["31", "32", "33"],
}

for key,values in favorite_place.items():
    print(key,"'s favorite place have ", end="")
    for value in values:
        print(value, "  ", end="")
    for value in values:
        if (value == "11") or (value == "22") or (value == "33"):
            print(f"But {key} best place is ", value)
    print()


print("6-11")
cites = {
    'HarBin': {
          "country":"China",
          "population":500,
           "language":"东北话",
            },
    'NanJing': {
        "country": "China",
        "population": 800,
        "language": "南京话",
    },
}
a = cites.keys()
print(a)
for key, values in cites.items():
    print(key, ":")
    for k1 in values.keys():
        print(k1, " :", values[k1])
