class Pozemek:
    total_area = 0
    total_build = 0
    total_agri = 0 

    def __init__(self, idd, area, kind):
        if kind not in ("zem", "stav", "mix"):
            raise ValueError(f"Neplatný druh pozemku: {kind}")

        self.idd = idd
        self.area = area
        self.kind = kind

        if self.kind == "zem":
            Pozemek.total_agri += self.area
            Pozemek.total_area += self.area
        
        elif self.kind == "stav":
            Pozemek.total_build += self.area
            Pozemek.total_area += self.area

        elif self.kind == "mix":
            Pozemek.total_area += self.area

    def change_kind(self, new_kind):
        if new_kind not in ("zem", "stav", "mix"):
            raise ValueError(f"Neplatný druh pozemku: {new_kind}")

        self.new_kind = new_kind

        if self.kind == "zem":
            Pozemek.total_agri -= self.area
        
        elif self.kind == "stav":
            Pozemek.total_build += self.area


        if self.new_kind == "zem":
            Pozemek.total_agri += self.area
        
        elif self.new_kind == "stav":
            Pozemek.total_build += self.area
        

    def summary():
        print(f"Total area: {Pozemek.total_area}, Total agri: {Pozemek.total_agri}, Total build: {Pozemek.total_build}")


    def __del__(self):
        if self.kind == "zem":
            Pozemek.total_agri -= self.area
            Pozemek.total_area -= self.area
        
        elif self.kind == "stav":
            Pozemek.total_build -= self.area
            Pozemek.total_area -= self.area

        elif self.kind == "mix":
            Pozemek.total_area -= self.area


p1 = Pozemek(1, 100, "zem")
p2 = Pozemek(2, 200, "zem")
p3 = Pozemek(3, 100, "stav")
p4 = Pozemek(4, 100, "mix")
print(Pozemek.total_area)
del p4
print(Pozemek.total_area)
p3.change_kind("zem")

Pozemek.summary()