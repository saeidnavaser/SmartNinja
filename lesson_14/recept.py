class Animal():
    count = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count.append(name)
def get_number_animals(self):
    return len(self.count)
#animals = [Animal("bello", 23), Animal("", )]
a = Animal ("bello", 23)
b = Animal ("Goldi", 4)

print(a.get_number_animals())