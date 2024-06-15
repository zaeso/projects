class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.email = email
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет. Мой никнейм - {self.nickname}, мой email - {self.email}.")


gamer1 = Gamer("Иван", 14, "John", "john@gmail.com")


gamer1.add_game("Minecraft")
gamer1.add_game("Dota 2")


gamer1.introduce()


print(f"{gamer1.name} любит игры: {', '.join(gamer1.games)}")

