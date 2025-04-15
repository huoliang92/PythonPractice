
def display_message():
    """文档字符串 """
    print("8-1 函数测试")
# display_message()


def favorite_book(title):
    print("8-2")
    print(f"my favorite book is {title}")

# favorite_book("三国演义")


def t_shirt_description(size, word):
    print("8-3")
    size = int(size)
    print(f"I want Size:{size},and type is \"{word}\"")


# t_shirt_description(15, "Dog Type")
# t_shirt_description(word="Dog Type", size=15)


def make_shirt(size="Big", word="I love Python"):
    print("8-4")
    print(f"I want Size:{size},and type is \"{word}\"")

# make_shirt()
# make_shirt("Medium")
# make_shirt(size="Medium")
# make_shirt("Small", "找工作好难啊")


def describe_city(city="北京", country="中国"):
    print("8-5")
    print(f"{city} is in {country}")


# describe_city()
# describe_city(city="台湾")
# describe_city("伦敦", "英国")

def city_country(city, country):
    print("8-6")
    index = f"{city.title()}, {country.title()}"
    return index

rlt = city_country("london", "uS")
print(rlt)
rlt =city_country("dc", "USA")
print(rlt)
rlt = city_country("beijing", "China")
print(rlt)



def make_album(singer, album_name, music_number=None):
    """None 表示可选参数"""
    print("8-7")
    album_dictionary = {}
    if music_number:
        album_dictionary['singer'] = singer
        album_dictionary['album_name'] = album_name
        album_dictionary['music_number'] = music_number
    else:
        album_dictionary['singer'] = singer
        album_dictionary['album_name'] = album_name
    return album_dictionary


check_a = make_album("周杰伦", "七里香", 1)

check_b = make_album("林俊杰", "江南", 1)

check_c = make_album("SHE", "河滨公园")

listA = [check_a, check_b, check_c]


for a in listA:
    print(a)



def check_if_quit(word):
    if word == 'q':
        print("终止输入")
        return True

print("8-8 专辑录入 随意选项输入 q 结束本次")
listA = []
while True:
    name = input("请输入歌手名")

    if check_if_quit(name):
        break
    album = input("请输入专辑名")

    if check_if_quit(name):
        break

    check_a = make_album(name, album)
    listA.append(check_a)
for a in listA:
    print(a)


# 8-9 10
def show_messages(list_to_print):
    for single in list_to_print:
        print(single)


def send_messages(send_message_list, list_all):
    while send_message_list:
        temp = send_message_list.pop()
        list_all.append(temp)
    list_all.reverse()


listA = ["A", "B", "C", "D"]
list_all = []
print(listA)
print(list_all)
send_messages(listA, list_all)
print(listA)
print(list_all)


# 8-11
def send_no_change_ori(send_message_list,list_all):
    while send_message_list:
        temp = send_message_list.pop()
        list_all.append(temp)
    list_all.reverse()


listA = ["A", "B", "C", "D"]
list_all = []
print(listA)
print(list_all)
send_no_change_ori(listA[:], list_all)
print(listA)
print(list_all)



# 8-12
def multiple_para(*mul):
    for temp in mul:
        print(temp)


multiple_para("1","2","3")


# 8-13 14

# 










#  **kwargs 任意数量的关键字参数
#  字典
def user_profile(first_name, last_name, **dic):
    dic["first_name"]= first_name
    dic["last_name"] = last_name
    print(222)
    return dic



dic_out = user_profile("11", "22", middle_name="33", 中文="试试")
for key, value in dic_out.items():
    print(f"{key}---{value}")


if __name__=='__main__':
    print("1111")
    print("1111")


