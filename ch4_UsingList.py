"""
"""

print("4-1")
pizza_List = ["A PIZZA", "B PIZZA", "C PIZZA"]
for singlePizza in pizza_List:
    print(singlePizza)
    print(f"I like {singlePizza.lower().title()}")
print("I like pizza very much")

print("4-2")
animal_List = ["pig", "dog", "cat"]
for singleAnimal in animal_List:
    print("A", singleAnimal, "wouled make a great pet")
print("I like these animal")

print("4-3")
for number20 in range(1, 21):
    print(number20)

print("4-4,5")
number_List = []
number_List = list(range(1, 11)) #list 和 range 都是函数
for singelNumber in number_List:
    print(singelNumber)
print(f"最小的值是--{min(number_List)}")
max = max(number_List)
print(f"最大的值是--{max}")
print(f"1-10 总和是--{sum(number_List)}")

print("4-6")
oddNumberList = []
oddNumberList = list(range(1, 20, 2))
for oddNumber in oddNumberList:
    print(oddNumber)


print("4-7")
threNumberList = []
threNumberList = list(range(3, 31, 3))
for threeNumber in threNumberList:
    print(threeNumber)

print("4-8")

number_List = list(range(1, 10))
print("原始数据")
print(number_List)
tripleNumber_List = []
for temp in number_List:
    tripleNumber_List.append(temp**3)
print("立方放大后")
print(tripleNumber_List)


print("4-9")
number_List = list(range(1, 10))
tripleNumber_List = [temp**3 for temp in number_List]
print(tripleNumber_List)


print("4-10")
number_List = list(range(1, 11))
print(f"Current list is {number_List}")
print("前3个数是")
print(number_List[:3])
print("中间3个数是")
for middle in number_List[4:7]:
    print(middle)
print("最后3个数是", number_List[-3:])

print("4-11 12")
pizza_ListA = ["A PIZZA", "B PIZZA", "C PIZZA"]
pizza_ListB = pizza_ListA[:]  # 复制列表
pizza_ListA.append("D PIZZA")
temp = "E PIZZA"
pizza_ListB.append(temp)
print("pizza_ListA")
for temp in pizza_ListA:
    print(temp)
print("pizza_ListB")
for temp in pizza_ListB:
    print(temp)

print("4-13")

menu = ('a', 'b', 'c', 'd', 'e')
for temp in menu:
    print(temp)

menu = ('a', 'bb', 'cc', 'd', 'e')
for temp in menu:
    print(temp)