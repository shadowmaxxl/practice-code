# Keyword `class` followed by class name, starting with a capital letter
class Human:
    # This is your constructor method
    # It is how you make an object. You pass in a set of parameters to make an object, and it sets up the properties of the object.
    def __init__(self, name: str, age: int) -> None:
        # The attribute `name` is set to the value of the parameter `name` that was passed in.
        self.name = name # atttributes of the object.
        self.age = age
        self.num_legs = 2

    # This is a method
    # It uses your object, and then does sth. Here, we say the guy is walking. I'm walking here!
    def walk(self):
        print(f"{self.name} is walking.")

    # Not all functions within a class are methods.
    # Methods start with the `self` keyword, like you see in `walk` and `__init__`
    # These "methods" do not need an object, hence they are static methods.
    @staticmethod
    def talk():
        print("I am talking.")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self) -> str:
        return f"Human(name='{self.name}', age={self.age})"

peep1 = Human("John", 30)
peep1.walk()
Human.talk()

# This is how you access the attributes of an object.
print(peep1.name)
print(peep1.age)

# __str__ is useful when you want sth to show up when you print the object.
print(peep1)

# I used repr to make another object that is the same as peep1.
peep2 = eval(repr(peep1))

print(peep2)

# __repr__ is useful when you want to see the object in a more detailed way.
# Some peeps like to use it to make a string that can be used to recreate the object.
# print(repr(peep1))

# You can do what a class does using dictionaries and functions that act on the dictionary.
def human_maker(name: str, age: int) -> dict:
    return {
        "name": name,
        "age": age,
        "num_legs": 2
    }

def walk(person: dict) -> None:
    print(f"{person['name']} is walking.")

peep2 = human_maker("Jane", 25)

print(peep2["name"])
print(peep2["age"])
walk(peep2)

        