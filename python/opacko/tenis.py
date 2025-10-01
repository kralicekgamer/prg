def playerCard(*person_prize, **person):
    print(sum(person_prize))
    print("First name:", person["fname"])
    print("Last name:", person["lname"])
    print("Ranking:", person["rank"])


playerCard(500, 2000, 7000, fname="Janik", lname="Siner", rank=1)
