fclass Sword:

    def __init__(self, name, material, blade_length, grip):
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        print(f'Новый меч {name} выкован!')
    
    def slashing_blow(self):
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')

    def piercing_strike(self):
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.')

# Создаём экземпляр класса Sword.
first_sword = Sword('Тренировочный',
                    'Кора железного дуба',
                    1.2, 'хват одной рукой')

print('Перед вами манекен, опробуйте удары на нём.')
# Вызвать метод рубящего удара.
print(first_sword.slashing_blow())
# Вызвать метод пронзающего удара.




class Sword:
    # Объявляем конструктор класса и указываем все необходимые параметры: 
    # обязательный параметр self, название меча, материал клинка, 
    # длину клинка, тип рукояти.
    def __init__(self, name, material, blade_length, grip):
        # Объявляем свойства класса и передаём в них необходимые значения.
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        # Когда объект будет создан, выведется сообщение.
        print(f'Новый меч {name} выкован!')

    # Объявляем собственные методы,
    # в которых используются значения свойств класса Sword.
    # Метод «Нанести рубящий удар».
    def slashing_blow(self):
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')
    
    # Метод «Выполнить укол».
    def piercing_strike(self):
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    # Метод «Заточить клинок».
    def sharpen(self):
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.') 



                self.start_time = None
        self.end_time = None