#10-1
with open("learning_python.txt") as file_object:
    content = file_object.read()
    print(content.rstrip())
    print(file_object.tell()) ##指出当前文件指针的位置
    file_object.seek(0.0)
    print(file_object.tell())
    for line in file_object:
        print(line.rstrip())

with open("learning_python.txt") as file_object:
    for line in file_object:
        print(line.rstrip())

with open("learning_python.txt") as file_object:
    list = file_object.readlines()

for eachLine in list:
    print(eachLine.rstrip())


#10-2
with open("learning_python.txt") as file_object:
    content = file_object.readlines()
for singleLine in content:
    a = singleLine.replace("Python", "C++")
    print(singleLine.rstrip())
    print(a.rstrip())

#10-3
name = input("输入用户的名字")
if name:
    with open("guest.txt", 'w') as file:
        file.write(name)


#10-4
continueFg = True
with open("guest_book.txt", "w") as fileOb:
    while continueFg:
        name = input("输入姓名 ,q终止输入")
        if name == 'q':
            continueFg = False
            continue
        else:
            name +='\n'
            fileOb.write(name)


#10-5
continueFg = True
while continueFg:
    name = input("10-5 :  ")
    if name == 'q':
        continueFg = False
        continue
    else:
        with open("guest_book.txt", "a") as fileOb:
            name +='\n'
            fileOb.write(name)


#10-6-7


def quit_check(word):
    if word == "q":
        print("溜了溜了")
        return False
    else:
        return True


while True:
    try:
        print("输入q，终止循环")
        a = input("请输入第一个数字 ")
        if quit_check(a):
            a = int(a)
        else:
            break
        b = input("请再输入第一个数字 ")
        if quit_check(b):
            b = int(b)
        else:
            break
    except ValueError:
        print("数字转换失败，请重新输入")
        continue
    else:
        print("两者的和 ", a+b)


#10-8-9

def print_list(list):
    for single in list:
        print(single.rstrip())

fileName = "cat.txt"
fileName2 = "dog.txt"
try:
    with open(fileName,encoding='UTF-8') as cat_obj:
        listCat = cat_obj.readlines()

    with open(fileName2,encoding='UTF-8') as cat_obj:
        listDog = cat_obj.readlines()

except FileNotFoundError:
    #print("没找到文件")
    pass
else:
    print_list(listCat)
    print_list(listDog)


#10-10
with open("dog.txt", encoding='UTF-8') as file_object:
    allcontent = file_object.read()
    a= allcontent.count("狗")
print("狗的个数", a)



#10-11
import json
file_name = "number.json"
favorite_number = input("输入自己喜欢的数字  ")
favorite_number = int(favorite_number)  #不转换，json里面是字符串“10”
with open(file_name, 'w') as file_obj:
    json.dump(favorite_number, file_obj)

with open(file_name) as file_load:
    a = json.load(file_load)
print("我最喜欢的数字是", a)

#10-12
import json

def enter_new_word(file_name):
    favorite_number = input("输入自己喜欢的数字  ")
    favorite_number = int(favorite_number)  # 不转换，json里面是字符串“10”
    with open(file_name, 'w') as file_obj:
        json.dump(favorite_number, file_obj)

file_name = "number.json"
try:
    with open(file_name) as file_load:
        a = json.load(file_load)
        print("我最喜欢的数字是", a)
except json.decoder.JSONDecodeError:
    print("Json文件为空")
    enter_new_word(file_name)
except FileNotFoundError:
    print("新建文件")
    enter_new_word(file_name)