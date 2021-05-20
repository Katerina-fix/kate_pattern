from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
    #Интерфейс Компонента объявляет метод accept,
    #который в качестве аргумента может получать любой объект,
    #реализующий интерфейс посетителя.


    @abstractmethod
    def visitn(self, v:Notebooks) -> str:
        pass

    @abstractmethod
    def visits(self, v:Stationary) -> str:
        pass


class Calculator(Visitor):

    #Каждый Конкретный Компонент должен реализовать метод accept таким образом,
    # чтобы он вызывал метод посетителя, соответствующий классу компонента.

    def __init__(self, cost:int = 0):
        self.cost = cost

    def visitn(self, v:Notebooks):
        self.cost = self.cost + v.GetPrice()

    def visits(self, v:Stationary):
        self.cost = self.cost + v.GetPrice()

    def GetCost(self) -> int:
        return self.cost


class Visitable(ABC):

    # Интерфейс помещаемого объекта

    @abstractmethod
    def accept(self, v:Visitor):
        pass


class Notebooks(Visitable):

    def __init__(self, price: int):
        self.price = price

    def accept(self, v: Visitor):
        v.visitn(self)

    def GetPrice(self):
        return self.price



class Stationary(Visitable):

    def __init__(self, price: int):
        self.price = price

    def accept(self, v: Visitor):
        v.visits(self)

    def GetPrice(self):
        return self.price

#Список покупок для школы:
class TestVisitorSchool:

    def __init__(self):
        self.shopping_list = [Notebooks(150), Stationary(567)]
        self.calc = Calculator()

    def setProduct(self):
        for i in self.shopping_list:
            i.accept(self.calc)

    def GetCost(self) -> int:
        return self.calc.GetCost()

#Список покупок для института:
class TestVisitorUniversity:

    def __init__(self):
        self.shopping_list = [Notebooks(175), Stationary(30)]
        self.calc = Calculator()

    def setProduct(self):
        for i in self.shopping_list:
            i.accept(self.calc)

    def GetCost(self) -> int:
        return self.calc.GetCost()


if __name__ == "__main__":

    s = TestVisitorSchool()

    s.setProduct()

    print(f"Всего к оплате за покупки к школе: {s.GetCost()}")

    u = TestVisitorUniversity()

    u.setProduct()

    print(f"Всего к оплате за покупки к институту: {u.GetCost()}")