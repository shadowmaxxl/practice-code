class Human:

 def __init__(self, name: str, age: int) -> None:
  self.name = name 
  self.age = age
  self.num_arms= 2

 def wave(self):
    print(f"{self.name} is waving.")
name = input("what is your name? ")
age = int(input("how old are you?"))

  