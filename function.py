# -*- coding: utf-8 -*-

def menu1 ():   #Menu showing options of loading the lists of countrys and capitols
    print("Proszę wybrać któromś z opcji. Wielkość liter nie ma znaczenia\n\n")
    print("Podaj A - aby czytać domyślną listę państw\n")
    print("Podaj B - aby wczytać własne listy do gry\n")
    print("Podaj C - aby wczytać listę z pliku z poprzedniej gry\n")

def menu ():    #Menu showing action of definition contained in 'Game Class'
    print("Podaj 1 - aby zagrać \n")
    print("Podaj 2 - aby dodaj państwo i stolice \n")
    print("Podaj 3 - wyświetl aktualny wynik \n")
    print("Podaj 4 - aby zapisać państwa i stolice do odpowiedniego pliku\n")
    print("Podaj 5 - aby odczytać państwa i stolica z pliku\n")
    print("Podaj 6 - aby pokazać aktualną zawartość list\n")
    print("Podaj 7 - aby zakończyć i zapisać wartośc do pliku  \n")

def odczyt(filename):
    co=[]   #Adding countrys included in the file
    ca=[]   #Adding capitols included in the file
    with open(filename, 'rt') as out:
    #List of countrys and their capitols has format:
    #Country,Capitol
        for line in out:
            co.append((line[:-1].split(','))[0])
            ca.append((line[:-1].split(','))[1])
    return co,ca

def wczytywanie():

    i = 1
    co = []
    ca = []
    print("Proszę podawać wartości, podanie Q\q kończy wczytywanie\n")
    while True:
        #Ading a new country and their capitol
        country = str(input("Podaj Państwo numer {0}".format(i)))
        if country.lower() == 'q':
            break
        capitol = str(input("Podaj stolicę tego Państwa".format(i)))
        co.append(country)
        ca.append(capitol)
        i+=1
    return co,ca


