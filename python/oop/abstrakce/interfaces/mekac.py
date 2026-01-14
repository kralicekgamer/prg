from abc import ABC, abstractmethod

class FastFood(ABC):
    
    @abstractmethod
    def accept_order(self, what, deliver_number):
        pass

    @abstractmethod
    def cook(self, what, deliver_number):
        pass
    
    @abstractmethod
    def pack(self, deliver_number):
        pass
    
    @abstractmethod
    def deliver(self, deliver_number):
        pass
    

class KFC(FastFood):
    def accept_order(self, what, deliver_number):
        pass

    def cook(self, what, deliver_number):
        pass
    
    def pack(self, deliver_number):
        pass
    
    def deliver(self, deliver_number):
        pass


class McDonald(FastFood):
    def accept_order(self, what, deliver_number):
        pass

    def cook(self, what, deliver_number):
        pass
    
    def pack(self, deliver_number):
        pass
    
    def deliver(self, deliver_number):
        pass


class BurgerKing(FastFood):
    def accept_order(self, what, deliver_number):
        pass

    def cook(self, what, deliver_number):
        pass
    
    def pack(self, deliver_number):
        pass
    
    def deliver(self, deliver_number):
        pass


b = BurgerKing()
b.accept_order("dadasd", 1)
b.cook("dasd", 1)
b.deliver(1)
b.pack(1)