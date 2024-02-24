from itertools import cycle

alphaRus = list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
alphaEng = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

shift = 0
firstLetter = ""

while (email := input()) != "":
    address = input()

    addressWithoutEnd = address.rstrip("1234567890.")
    shift = ord(addressWithoutEnd[len(addressWithoutEnd) - 1].upper()) - ord("В")

    if shift < 0:
        shift += 26

    print("Key:", shift, "- ", end="")

    for al in email:
        if al.isalpha():
            if al.islower():
                firstLetter = "a"
            else:
                firstLetter = "A"

            print(chr((ord(al) - ord(firstLetter) - shift + 26) % 26 + ord(firstLetter)), end="")
        else:
            print(al, end="")

    print(end=" ")

    for al in address:
        if al.isalpha():
            if al.islower():
                firstLetter = "а"
            else:
                firstLetter = "А"

            print(chr((ord(al) - ord(firstLetter) - shift + 32) % 32 + ord(firstLetter)), end="")
        else:
            print(al, end="")

    print()