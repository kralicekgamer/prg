from abc import ABC, abstractmethod

class Operation(ABC):
    
    @abstractmethod
    def calculate(self, *args):
        pass
    
# Vytvoř třídy Sum a Multiply jako potomky rozhraní Operation.
# Přepiš abstraktní metodu calculate tak, aby ve třídě Sum
# sečetla libovolný počet vstupních hodnot a vrátila výsledek
# a ve třídě Multiply mezi sebou vynásobila libovolný počet
# vstupních hodnot a vrátila výsledek.

        
# Vytvoř objekt sum třídy Sum, zavolej metodu caluculate(1, 3, 5 0.1) a vypiš výsledek.
# Vytvoř objekt mul třídy Multiply a zavolej metodu caluculate(1, 3, 5 0.1) a vypiš výsledek.


class Sum(Operation):
    def calculate(self, *args):
        total = 0
        for arg in args:
            total += arg
        return total

class Multiply(Operation):
    def calculate(self, *args):
        total = 1
        for arg in args:
            total *= arg 
        return total

s = Sum()
print(s.calculate(1, 3, 5, 0.1))

m = Multiply()
print(m.calculate(1, 3, 5, 0.1))