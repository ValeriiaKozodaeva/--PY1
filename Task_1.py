import doctest

"""
Описываем мой шопер для повседневного похода в университет
"""

class Notes:
    def __init__(self, numbers_notes: int, weight_notes: float):
        """
        Создание и подготовка к работе класса "Тетради"

        :param numbers_notes: количество тетрадей
        :param weight_notes: вес тетрадей по ощущениям в кг

        Примеры:
        >>> notes = Notes(4, 0.6)
        """

        if not isinstance(numbers_notes, (int)):
            raise TypeError("Количество тетрадей должно быть типа int")
        if numbers_notes < 0:
            raise ValueError("Кол-во тетрадей должно быть не отрицательным числом")
        self.numbers_notes = numbers_notes

        if not isinstance(weight_notes, (int, float)):
            raise TypeError("Вес тетрадей должен быть типа int или float")
        if numbers_notes < 0:
            raise ValueError("Вес тетрадей должен быть не отрицательным числом")
        self.numbers_notes = numbers_notes

    def is_notes(self):
        """
        Функция которая проверяет есть ли тетради с собой
        :return: Есть ли тетради с собой
        Примеры:
        >>> notes= Notes(0, 0)
        >>> notes.is_notes()
        """
        ...

    def remove_notes(self, some_notes: int):
        """
        Убавление тетрадей из имеющихся в шоппере.
        :param some_notes: Количество тетрадей убранных

        :raise ValueError: Если количество убираемых тетрадей превышает
        имеющихся в шопере, то вызываем ошибку

        Примеры:
        >>> notes = Notes(4, 0.5)
        >>> notes.remove_notes(2)
        """
        if not isinstance(some_notes, (int)):
            raise TypeError("Кол-во убираемых тетрадей должно быть типа int")

        ...


class Steel_texts:
    def __init__(self, pages: int, length: float, width: float):
        """
        Создание и подготовка к работе класса "Учебник по металлическим конструкциям"

        :param pages: количество страниц
        :param length: длина учебника в см
        :param width: ширина учебника в см

        Примеры:
        >>> steal_text = Steel_texts(333, 25.5, 18.6)
        """

        if not isinstance(pages, (int)):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Кол-во тетрадей должно быть положительным числом")
        self.pages = pages
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

    def last_read_page(self, read_pages: int):
        """
        метод увеличивает последнюю прочитанную страницу.

        :param read_pages: количество прочитанных страниц
        """
        if not isinstance(read_pages, int):
            raise TypeError("прочитанные страницы должны быть типа int")

        if read_pages < 0:
            raise ValueError("прочитанные страницы должны быть положительным числом")

        ...

    def area(self):
        """
        метод позволяет найти площадь учебника

        :return: площадь
        """
        ...

class Phone:
    def __init__(self, power_before: int, power_after: int, minutes: int):
        """
        Создание и подготовка к работе класса "Телефон"

        :param power_before: количество заряда до того как положила в шопер
        :param power_after: количество заряда после того как положила в шопер
        :param minutes: количество времени в шопере

        Примеры:
        >>> phone = Phone(33, 6, 20)
        """

        if not isinstance(power_before, (int)):
            raise TypeError("Процент заряда должен быть типа int")
        if power_before <= 0:
            raise ValueError("Процент должно быть положительным числом")
        self.power_before = power_before


        if not isinstance(power_after, (int)):
            raise TypeError("Процент заряда должен быть типа int")
        if power_after <= 0:
            raise ValueError("Процент должно быть положительным числом")
        self.power_after = power_after


        if not isinstance(minutes, (int)):
            raise TypeError("Количество минут проведенных в шопере должно быть типа int")
        if minutes <= 0:
            raise ValueError("Количество минут проведенных в шопере должно быть положительным числом")
        self.minutes = minutes

    def speed(self):
        """
        Метод позволяет найти скорость потери заряда в минуту

        :return: скорость потери
        """
        ...

    def remaining_time(self, time: int):
        """
        :param time: данный промежуток времени в минутах

        Метод позволяет посчитать, не сядет ли телефон полностью за данный промежуток времени

        :return: True, False
        """

        if not isinstance(time, (int)):
            raise TypeError("Количество минут проведенных в шопере должно быть типа int")
        if time <= 0:
            raise ValueError("Количество минут проведенных в шопере должно быть положительным числом")
        self.time = time
        ...

if __name__ == "__main__":
    doctest.testmod()
