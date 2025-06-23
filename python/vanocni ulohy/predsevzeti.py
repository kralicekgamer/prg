def predsevzeti():
    pocet_predsevzeti = 3
    predsevzeti_list = []

    for i in range(pocet_predsevzeti):
        predsevzeti = input("Zadej předsevzetí: ")
        predsevzeti_list.append(predsevzeti)

    print("\nV roce 2025 chci dosáhnout těchto cílů:")
    for i in range(pocet_predsevzeti):
        print(f"{i + 1}. {predsevzeti_list[i]}")

predsevzeti()
