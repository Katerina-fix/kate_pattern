from abc import ABC, abstractmethod


class Education(ABC):

    # Абстрактный Класс определяет шаблонный метод, содержащий скелет некоторого алгоритма,
    # состоящего из вызовов (обычно) абстрактных примитивных операций.
    # Конкретные подклассы должны реализовать эти операции, но оставить сам шаблонный метод
    # без изменений.

    @abstractmethod
    def ShowBegining(self) -> str:
        pass

    @abstractmethod
    def ShowPassed(self) -> str:
        pass

    # Эти операции должны быть реализованы в подклассах.
    def runAll(self):
        # print(self.ShowBegining)
        # print(self.ShowPassed)
        return "\n ".join([self.ShowBegining, self.ShowPassed])


class School(Education):
    """
    Конкретные классы должны реализовать все абстрактные операции базового
    класса. Они также могут переопределить некоторые операции с реализацией по
    умолчанию.
    """

    # Эти операции уже имеют реализации.
    @property
    def ShowBegining(self) -> str:
        return "в первый класс принято 90 человек"

    @property
    def ShowPassed(self) -> str:
        return "в первом классе не приняли 12 человек"


class University(Education):

    @property
    def ShowBegining(self) -> str:
        return "в ВУЗ на бюджет зачислено 534 человека"

    @property
    def ShowPassed(self) -> str:
        return "в ВУЗ на бюджет не прошли 175 человек"


if __name__ == "__main__":
    school = School()
    school.runAll()

    university = University()
    university.runAll()