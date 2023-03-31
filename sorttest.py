import random
import sortmodule

looping = True
listnummers = []

for tnum in range(5):
    tslumptal = random.randint(0, 100)
    listnummers.append(tslumptal)
    print(tslumptal)

while looping:

    val = sortmodule.create_menu()

    if (val == "1"):
        print("\n Skriver ut lista med sumpade tal ----")


        sortmodule.print_list_numbers(listnummers)
        nysorterad_listnumbers = sortmodule.bubble_sort(listnummers)
        print("SORTERAR")
        sortmodule.print_list_numbers(nysorterad_listnumbers)
        forsatt = input("\nVill du fortsätta? j/n ")
        if(forsatt == "n"):
            break

    elif (val == "2"):
        print("\n-Skriver listnumbers med slumpade tal---------")
        listnummers2 = listnummers
        sortmodule.print_list_numbers(listnummers)
        print("\n-sorterar med pyhton sort-------")
        listnummers2.sort()
        sortmodule.print_list_numbers(listnummers2)
        listnummers2.sort()
        
        if(forsatt == "n"):
            break

        print("val 2")
    else:
        break
