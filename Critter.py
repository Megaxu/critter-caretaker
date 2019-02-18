# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property

    def mood(self):                     # отражает настроение питомца
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = None):         # выбор обильности обеда
        print\
            ("""
            Выберите, как сильно хотите покормить питомца:
            1 - Чуть-чуть перекусить
            2 - Перекусить
            3 - Плотно покушать
            4 - ПокушОть от души
            """
        )
        feed = None
        while feed != "1" and feed != "2" and feed != "3" and feed != "4":
            feed = input("Ваш выбор: ")
            if feed == "1":
                food = 2
                print("Покушал... а вроде и нет. Может еще покушаем?")
            elif feed == "2":
                food = 3
                print("Ну... перекусили, теперь можно и поспать..")
            elif feed == "3":
                food = 4
                print("Наконец-то я сыт!")
            elif feed == "4":
                food = 5
                print("Ух, хорошо покушОл, можно и отдохнуть")
            else:
                print("Извините, но в меню нет пункта", feed)

        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = None, do = None):      # позволяет выбрать интенсивность игры
        print\
            ("""
            Выберите как долго играть с питомцем:
            1 - Сыграть совсем чуть-чуть
            2 - Сыграть пару раз
            3 - Устроить полноценную игру-тренировку
            4 - Устроить мегагалактическую тренировку вселенских масштабов и веселья!"""
             )
        do = input("Ваш выбор: ")
        if do == "1":
            fun = 2
            self.hunger += 1
            print("Поиграли хорошо, но как-то мало.. Может еще разок?)")
        elif do == "2":
            fun = 3
            self.hunger += 2
            print("Ух, я даже немного устал.")
        elif do == "3":
            fun = 4
            self.hunger += 3
            print("Уиии! Это было круто, правда я проголодался.")
        elif do == "4":
            fun == 5
            self.hunger += 4
            print("Фух, вот это было тяжело, но очень весело, правда я очень голодный.")
        else:
            print("Извините, но в меню нет пункта", do)

        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Введите имя зверушки: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print\
            ("""
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствии
            2 - Покормить зверушку
            3 - Поиграть со зверушкой
            """)
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        # кормление
        elif choice == "2":
            crit.eat()
        # играть
        elif choice == "3":
            crit.play()
        # непонятный ввод пользователя
        else:
            print("Извините, но в меню нет пункта", choice)

main()
input("\n\nPress Enter")