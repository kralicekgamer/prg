class Nuts:
    kg = 0 

    def __init__(self, order):
        self.order = order
        Nuts.kg = Nuts.kg + self.order

    def __del__(self):
        Nuts.kg = Nuts.kg - self.order


order_1 = Nuts(20)
order_2 = Nuts(20)

print(Nuts.kg)

del order_1

print(Nuts.kg)