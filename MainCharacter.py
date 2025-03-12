class MainCharacter:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.age = age
        self.height = height
        print(f"You've created a character named {name}, who is {age} years old and {height} cm in height.")

    def jump(self):
        return 'You jumped!'

    def attack(self):
        return "You've dealt some damage!"