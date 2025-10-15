class Pet:
    def __init__(self,
                 name: str,
                 number_of_legs: int,
                 color: str):
        self.name = name
        self.number_of_legs = number_of_legs
        self.color = color

    def __str__(self):
        return f'{self.name} ({self.color})'

    def make_sound(self) -> str:
        return "Pet sound"


class Cat(Pet):
    def __init__(self,
                 name: str,
                 number_of_legs: int,
                 color: str,
                 loves_boxes: bool = True):
        super().__init__(name, number_of_legs, color)
        self.loves_boxes = loves_boxes

    def make_sound(self) -> str:
        return "Meow!"


class Dog(Pet):
    def __init__(self,
                 name: str,
                 number_of_legs: int,
                 color: str,
                 is_good_boy: bool = True):
        super().__init__(name, number_of_legs, color)
        self.is_good_boy = is_good_boy

    def make_sound(self) -> str:
        return "Woof!"


# Testiranje
cat = Cat('Kitty', 4, 'gray')
dog = Dog('Rex', 4, 'brown')

print(cat)
print(f'The cat has {cat.number_of_legs} legs and says: {cat.make_sound()}')

print()
print(dog)
print(f'The dog has {dog.number_of_legs} legs and says: {dog.make_sound()}')