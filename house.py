name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron" | "Ginny" | "Kaske":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

