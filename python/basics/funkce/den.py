import random

def dobrySpatnyDen():
    den = ["dobrý", "špatný", "napycu"]
    return random.choice(den)

print(f"Mám {dobrySpatnyDen()} den.")
