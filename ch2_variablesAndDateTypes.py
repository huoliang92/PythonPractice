
# 2-1 2-2
oneSingleWords = 'Be happy'
print(oneSingleWords)
oneSingleWords = "Be more happier!"
print(oneSingleWords)

# 2-3 2-4
name = 'eric bob'
print(f"Hello {name}, would you like to learn some Python today")
print(f"Hello {name.lower()}, would you like to learn some Python today?")
print(f"Hello {name.upper()}, would you like to learn some Python today?")
print(f"Hello {name.title()}, would you like to learn some Python today?")

#2-5 2-6 2-7
print('亮仔说： "穿越逆旅，抵达繁星"')
name = '亮仔'
oneSingleWords = '"穿越逆旅，抵达繁星"'
namePlusWords = f'{name}说： {oneSingleWords}'
print(namePlusWords)

name = "   亮仔   "
print(name.rstrip())
print(name.lstrip())
print(name.strip())

print(f"{name.strip()}说： \n\t{oneSingleWords}")


#2-8
print("5+3=", 5+3)
print("9-1=", 9-1)
print("4*2=", 4*2)
print("16/2=", 16/2)

#2-9 2-10
#下面的代码，打印出的了我最喜欢的数字
oneNumber = 73
print(f"我喜欢的数字是{oneNumber}，因为它是我的生日")

#2-11
import this