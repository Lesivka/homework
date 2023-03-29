class Hearthstone:
    def __init__(self, hero, healthpoints, pack, move):
        self.hero = hero
        self.healhpoints = healthpoints
        self.__pack = pack
        self.move = move

    def tier(self):
        if self.healhpoints > 40:
            return 'Уровень персонажа равен 1'
        else:
            return 'Уровень персонажа равен 2'

    def money(self):
        if self.move <= 8:
            return f'На {self.move} ходу дается {self.move + 2} монет'
        else:
            return f'На {self.move} ходу дается 10 монет'

    def slogan(self):
        return 'Никому не говори, но я болею за тебя!'

    def get_pack(self):
        return f'Основным классом были выбраны {self.__pack}'

    def set_pack(self, new_pack):
        self.__pack = new_pack
        return f'Вектор изменён, теперь основной класс - {self.__pack}'


hero1 = Hearthstone('Captain Udora', 45, 'Beasts', 5)
hero2 = Hearthstone('Rafaam', 40, 'Undeads', 13)
print(hero1.get_pack())
print(hero2.tier())
