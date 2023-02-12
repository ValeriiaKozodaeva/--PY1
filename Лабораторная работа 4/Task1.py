import doctest

class Song:
    """ Базовый класс - песни. Дочерний класс - рок песня """
    def __init__(self, name: str, vocalist: str, duration: float):
        self.name = name
        self.vocalist = vocalist
        self.duration = duration

    def __str__(self):
        return f"Песня {self.name}. Исполнитель {self.vocalist}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, vocalist={self.vocalist!r}, duration={self.duration})"

    def sec(self) -> float:
        """Перевод длительности песни из минут в секунды"""
        return self.duration * 60

    def instruments(self, number_of_instr: int) -> int:
        """Количество участвующих инструментов и зарплата музыкантам каждому по 60к
        Пример:
        >>> song = Song("Белые розы", "Шатунов", 3.45)
        >>> song.instruments(6)
        """
        return number_of_instr * 60000


class Rocksong(Song):
    def __init__(self, name: str, vocalist: str, duration: float, language: str):
        super().__init__(name, vocalist, duration)
        self.language = language

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, vocalist={self.vocalist!r}, duration={self.duration!r}, language={self.language!r})"

    def __str__(self):
        return f"Песня {self.name}. Исполнитель {self.vocalist}. Продолжительность {self.duration}. Язык {self.language}"

    def instruments(self, number_of_instr: int) -> int:
        """Количество участвующих инструментов и зарплата музыкантам каждому по 60к + аренда каждого инструмента по 7к"""
        total_coast = number_of_instr * 7000 + number_of_instr * 60000
        return total_coast

if __name__ == "__main__":
    doctest.testmod()
