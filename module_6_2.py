class Vehicle():
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
    __COlOR_VARIANT = ['blue', 'red', 'green', 'black', 'white']


    def get_model(self):
        return f'Модель: {self.__model}'


    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'



    def get_color(self):
        return f"Цвет: {self.__color}"


    def print_info(self):
        print(f'{Vehicle.get_model(self)}, {Vehicle.get_horsepower(self)}, {Vehicle.get_color(self)}, Владелец: {self.owner}')


    def set_color(self, new_color):
        self.new_color = new_color
        for i in self.__COlOR_VARIANT:
            if i.lower() == self.new_color.lower():
                self.__color = new_color
                break
        else:
            print(f"Нельзя сменить цвет на {self.new_color}")

class Sedan(Vehicle):
    __PASSANGERES_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()