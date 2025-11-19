class Teacher:
    def __init__(self, fname, lname, nick, age, status, grade):
        self.fname = fname
        self.lname = lname
        self.nick = nick
        self.age = age
        self.status = status
        self.grade = grade


    def getInfo(self):
        return self.fname + " " + self.lname + ", " +  str(self.grade)

sbor = {
    "herman": Teacher("Petr", "Heřmanský", "Berta", 60, "angry", 2),
    "cyril": Teacher("Cyril", "Kochrda", "Walter White", 45, "aktivní", 3),
    "kozina": Teacher("Petr", "Kozák", "kozy", 52, "married", 1)
}

print(sbor["herman"].getInfo())

for x in sbor.values():
    print(x.getInfo())