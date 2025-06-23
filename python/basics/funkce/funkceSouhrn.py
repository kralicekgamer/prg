def slepText(t1, t2):
    return t1 + " " + t2


def slepText2(slova):
    slepenec = ""

    for slovo in slova:
        slepenec = slepenec + slovo + " "
    return slepenec


def slepText3(slova):
    return " ".join(slova)


def slepText4(*argv):
    return " ".join(argv)

