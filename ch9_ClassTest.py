
#9-1-2-4
class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_server = 0

    def describe_restaurant(self):
        print(f"Name is {self.restaurant_name}")
        print(f"Type is {self.cuisine_type.title()}")
        print(f"Served people  is {self.number_server}")

    def open_restaurant(self):
        print("营业中")

    def update_restaurant_served(self, number):
        self.number_server += number


smallRestaurant = Restaurant("KFC", "fried chicken")
smallRestaurant.describe_restaurant()
smallRestaurant.open_restaurant()

smallRestaurantA = Restaurant("McDonald", "fried chicken")
smallRestaurantA.describe_restaurant()

smallRestaurantB = Restaurant("PizzaHut", "Pizza")
smallRestaurantB.describe_restaurant()
smallRestaurantB.update_restaurant_served(10)
smallRestaurantB.describe_restaurant()
smallRestaurantB.update_restaurant_served(11)
smallRestaurantB.describe_restaurant()


#9-3-5
class User :
    def __init__(self, first_name, last_name, age, occupation):
        self.firstName = first_name
        self.lastName = last_name
        self.age = int(age)
        self.occupation = occupation
        self.login_attempt = 0

    def greet_user(self):
        print("你的名字是？")
        print(f"LastName -- {self.lastName.title()}  , FirstName -- {self.firstName.title()} ")
        print("你的年龄是？")
        print(self.age)
        print("你的职业是？")
        print(self.occupation)

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0

    def show_login_attempts(self):
        print(f"已经登陆了 {self.login_attempt} 次")
myInformation = User("Liang", "Huo", "28", "programmer")
myInformation.greet_user()

myInformationA = User("Liang11", "Huo11", "29", "programmer")
myInformationA.greet_user()
myInformationA.increment_login_attempts()
myInformationA.increment_login_attempts()
myInformationA.increment_login_attempts()
myInformationA.show_login_attempts()
myInformationA.increment_login_attempts()
myInformationA.show_login_attempts()
myInformationA.reset_login_attempts()
myInformationA.show_login_attempts()


#9-6
class Restaurant6:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_server = 0

    def describe_restaurant(self):
        print(f"Name is {self.restaurant_name}")
        print(f"Type is {self.cuisine_type.title()}")
        print(f"Served people  is {self.number_server}")

    def open_restaurant(self):
        print("营业中")

    def update_restaurant_served(self, number):
        self.number_server += number


class IceCreamStand(Restaurant6):
    def __init__(self, name, type, flavors):
        super().__init__(name, type) #!!!!!
        self.flavors = flavors

    def show_flavor(self):
        print("菜单 : ", end='')
        for flavor in self.flavors:
            print(flavor, "  ", end='')


flavors = ["杨枝甘露", "奶茶", "芒果沙冰"]
myIce = IceCreamStand("七分甜", "冰淇淋店", flavors)
myIce.describe_restaurant()
myIce.update_restaurant_served(2)
myIce.describe_restaurant()
myIce.show_flavor()


#9-7
class UserA :
    def __init__(self, first_name, last_name, age, occupation):
        self.firstName = first_name
        self.lastName = last_name
        self.age = int(age)
        self.occupation = occupation
        self.login_attempt = 0

    def greet_user(self):
        print("你的名字是？")
        print(f"LastName -- {self.lastName.title()}  , FirstName -- {self.firstName.title()} ")
        print("你的年龄是？")
        print(self.age)
        print("你的职业是？")
        print(self.occupation)

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0

    def show_login_attempts(self):
        print(f"已经登陆了 {self.login_attempt} 次")


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privilege is :")
        for p in self.privileges:
            print(p)


class Admin(UserA):
    def __init__(self, first_name, last_name, age, occupation):
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = ["Acan add post", "can delete post", "can ban user"]
        self.privileges2 = Privileges()


admin = Admin("L", "H", "28", "soldier")
print(admin.privileges)
print(admin.privileges2.show_privileges())


class Battery:
    def __init__(self):
        self.batter_size = 75
        self.range = 0

    def check_range(self):
        if self.batter_size == 100:
            self.range = 260
        else:
            self.range = 360

    def show_range(self):
        print("当前里程数", self.range)

    def update_battery(self):
        if self.batter_size != 100:
            self.batter_size = 100


test = Battery()
test.check_range()
test.show_range()
test.update_battery()
test.check_range()
test.show_range()

from random import randint,choice


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return randint(1,self.sides)

    def update_die(self, side):
        self.sides = side
        print(f"更新骰子面为{self.sides}")

singleDie = Die()
a = singleDie.roll_die
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())
singleDie.update_die(20)
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())
print(singleDie.roll_die())

#9-14 15
from random import randint, choice
import operator

originList = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
#originList = [1,2,3,4]
finalList = []
while len(finalList) < 4:
    finalList.append(choice(originList))

print(f"This is lucky number {finalList}")

tryList = []
i = 0
while operator.eq(tryList,finalList) == False:
    tryList = []
    while len(tryList) < 4:
        tryList.append(choice(originList))
    print("i=",i)
    print(tryList)
    i+=1

print(f"tryList is {tryList}")
print("i = ",i)