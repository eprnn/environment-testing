from libraries.testlib import *

kirja = Book("hyvä kirja", "matti meikäläinen", 5)

kirjasto = Shelf()

kirjasto.additem(Book("Testikirja"))
kirjasto.additem(Game("Testipeli"))

for tavara in kirjasto.contents:

    if tavara.type == "Book":
        print(f"Kirjan nimi on {tavara.name}")
        continue

    if tavara.type == "Game":
        print(f"Pelin nimi on {tavara.name}")
        continue

    else:
        print("Wat?")