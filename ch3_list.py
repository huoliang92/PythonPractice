print("3-1")
nameList = ["Huo Liang", "liang zai", "xiao huo"]
print(nameList[0])
print(nameList[1].title())
print(nameList[2].upper())

print("3-2")
name0 = f"{nameList[0].title()}, 你好呀"
print(name0)
print(f"{nameList[1].title()},你好呀")
print(nameList[2].title(), "你好呀")

print("3-3")
motorcycle = ["honda", "yamaha", "suzuki"]
print("I would like to own a", motorcycle[0].title(), "motorcycle")  # , 之间的两个变量 自己带空格
print("I would like to own a", f"{motorcycle[1].title()} motorcycle")
cycle3 = motorcycle[2].title()
print("I would like to own a", cycle3, "motorcycle")

print("3-4569")
guestList = ["Mother", "Father", "Wife"]
print("I want this people to have dinner with me.")
print(guestList)
print("It is regrettable that", guestList[2], "can not come right now")
guestList[2] = "Tang Yan"
print("Now the new List is", guestList[0], ",", guestList[1], "and", guestList[2])
print("找到了更大的餐桌， 可以再加3个人")
guestList.insert(0, "卡卡西")
guestList.insert(2, "鸣人")
guestList.append("佐助")
print(guestList)
print("餐桌没来，只能装2个人了")
print("现在有", len(guestList), "待邀请嘉宾")
people1 = guestList.pop()
print(people1, "你来不了了")
people1 = guestList.pop()
print(people1, "你来不了了")
people1 = guestList.pop()
print(people1, "你来不了了")
people1 = guestList.pop()
print(people1, "你来不了了")

print("现在有", guestList[0], "和", guestList[1])
# 删除一个元素后，队列就会重排，下标就不准了
del guestList[1]
del guestList[0]
print("现在列表中的嘉宾", guestList)

print("3-8")

location = ["Xia Men", "Qing Dao", "Jia Mu Si", "S Tuo Li Ni"]
print(location)
print(sorted(location))
print(location)
print(sorted(location, reverse=True))
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)

print("3-10")
listAll = [1, 2+4, 3, 4, "aaa", 5]
print("listAll[-2]=", listAll[-2])
listAll.insert(2, 2.5)
print(listAll)
listAll.remove("aaa")
print(listAll)
listAll.pop(-1)
print(listAll)
del listAll[4]
print("删除第五个", listAll)
