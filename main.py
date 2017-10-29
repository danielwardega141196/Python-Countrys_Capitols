# -*- coding: utf-8 -*-

from function import menu,menu1,wczytywanie,odczyt
from classes import Game


gra = True

while gra:  #Repeat the game until the player wouldn't want to quit

    menu1() #Using defnition included in 'function.py'

    list_choice = str(input("Podaj swój wybór\n"))
    while (list_choice.lower() != 'a' and list_choice.lower() !='b' and list_choice.lower() != 'c'):
        list_choice=str(input("Podaj popraną wartość"))

    if list_choice.lower() == 'a':
        panstwa = ["Poland","Germany","France","Holland"]
        stolice = ["Warsaw","Berlin","Paris","Amsterdam"]

    if list_choice.lower() == 'b':
        print("Wypełnij listy państw oraz stolic")
        panstwa ,stolice = wczytywanie()    #Using definition included in 'function.py'

    if list_choice.lower() == 'c':
        filename = str(input("Podaj nazwe pliku z jakiego chcesz odczytać listy"))
        panstwa, stolice = odczyt(filename) #Using definition included in 'function.py'

    imie = input("Podaj nazwę użytkownika")

    gra = Game(panstwa,stolice,imie)    #Class initialization

    menu()  #Using definition included in 'function.py'

    while True:

        choice = str(input("Podaj twój wybór\n"))
        #The player will choose what he want to do in particular moment
        while (choice not in ['1','2','3','4','5','6','7']):
            choice = str(input("Wprowadź poprawną wartość"))

        if choice == '1':
            gra.play

        elif choice == '2':
            gra.add

        elif choice == '3':
            gra.show_value

        elif choice == '4':
            gra.zapis

        elif choice == '5':
            gra.odczyt

        elif choice == '6':
            gra.show_list

        elif choice == '7':
            print("Nick gracza: ",gra.imie,". Wynik: ",gra.score,".")
            print("Wyniki znajdują się w pliku \"scores.txt\"\n")
            gra.save_score
            break


    again = str(input("Czy chcesz zagrać jeszcze raz ?\nNaciśnj T-t,aby rozpocząć nową grę bądź N-n.\n"))
    #Player have to decided: Play or Quit
    while again.upper() != 'T' and again.upper() != 'N':
        again = str(input("Podaj poprawną wartość T/t lub N/n"))

    if again.upper()=='N':  #Ends the program
        gra=False

print("Dziękuję za Uwagę\n")




