some_number = 3
float_number = 4.56
string_text = "hallo"
boolean = True


number_list = [2, 4, 1, 7, 8]
number_list.sort()
print(number_list)

auto_list = ["audi", "tesla", "vw", "tesla"]
print(auto_list)
auto_list.append("honda")
print(auto_list)

for item in auto_list:
    item = "bla"
    print(item)

print(auto_list)


shopping_list = {"milk": 2,
                 "bread": 5,
                 "eggs": 10,
                 "dict": {
                     "c++": 5,
                     "java": 3,
                     "python": 1,
                 },
                 "list":[1, 2, 3, 4, 5]
                 }
print(shopping_list["dict"]["python"])
