import random
import sortmodule

looping = True
listnummers = []

for tnum in range(5):
    tslumptal = random.randint(0, 100)
    print(tslumptal)

while looping:

    val = sortmodule.create_menu()

    if (val == "1"):
        print("val 1")

    elif (val == "2"):
        print("val 2")
    else:
        break
