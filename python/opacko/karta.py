def karta(**person):
    print("*" * 30)
    print("* First Name:", person["fname"])
    print("* Last Name:", person["lname"])
    print("*" * 30)
    print("* Last Name:", person["job"])
    print("*" * 30)


karta(fname = "Petr", lname = "Pelc", job = "Gooner")
karta(fname = "Sam", lname = "Pelc", job = "Stripter")
