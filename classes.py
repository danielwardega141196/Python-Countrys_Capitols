# -*- coding: utf-8 -*-

from random import randint
from function import odczyt

class Game:
    def __init__(self, countrys, capitols,imie):  ## inicjalizuje listę krajów, stolic, oraz nazwę gracza
        self.coutrys = countrys     #Initial list of countries
        self.capitols = capitols    #Initial list of capitals
        self.imie = imie            #Initial nick of the player
        self.score = 0              #Initial score of player

    @property
    def play(self):             ## Guessing the capitals
        s= randint(0,len(self.coutrys)-1)   #Drawing index list
        shoot = input("Podaj stolice państwa {0}".format((self.coutrys)[s]))
        if shoot.lower() == (self.capitols)[s].lower():
            print("Dobra odpowiedź otrzymujesz 1 punkt\n")
            self.score += 1
        else:
            print("Zła Odpowiedź\n")

    @property
    def add(self):  #Adding a new country and its capital
        new_co = str(input("Podaj Państwo jakie chcesz dodać"))
        (self.coutrys).append(new_co)
        new_ca = str(input("Podaj Stolicę tego Państwa"))
        (self.capitols).append(new_ca)

    @property
    def show_value(self):  #Showing the current result
        print("Twój aktualny wynik to {0}".format(self.score))

    @property #Showing the current content of lists
    def show_list(self):
        for i in range(len(self.coutrys)):
            print("{0}. {1} - {2} \n".format(i+1,(self.coutrys)[i],(self.capitols)[i]))

    @property
    def zapis(self): #Saving the current state of lists to given filename
        plik = str(input("Podaj nazwę pliku\n"))
        with open(plik, 'wt') as inp:
                for i in range(len(self.coutrys)):
                    inp.write('{0},{1}\n'.format((self.coutrys)[i], (self.capitols)[i]))

    @property
    def odczyt(self):   #Adding new content to lists or overwriting lists
        plik = str(input("Podaj nazwę pliku\n"))    #The new content is in the file provided by the user
        print("Czy dane chcesz dodać do aktualnej bazy czy nadpisać aktualne dane ?\n")
        print("D/d - dodać , N/n - nadpisać\n")

        choice = str(input("Podaj swój wybór\n"))

        while choice.lower() != 'd' and choice.lower() != 'n':
            print("Błędnie wprowadzona wartość\n")
            choice = print("Podaj poprawną wartość \n")

        if choice.lower() == 'n':
            del (self.coutrys)[:]   #Removing the current contents of the list
            del (self.capitols)[:]  #Removing the current contents of the list
            self.coutrys, self.capitols = odczyt(plik)  #Using function included in 'function.py'
        else:
            self.coutrys += odczyt(plik)[0] #Adding the first return value to the current countrys content
            self.capitols += odczyt(plik)[1]    #Ading the second return value to the current capitols content

    @property
    def save_score(self):
        source = open("scores.txt").readlines() #reading te file line by line
        destiny = open("scores.txt", 'w')   #Writing the changed source content to the same file
        nicks=[]   #List of different players
        for k,line in enumerate(source):
                if k == 0:  #Rewriting the headline
                    destiny.write(line)
                    size = len(line)
                    continue
                nick = ((line.split('|'))[0]).replace(" ","")
                if nick.capitalize() not in nicks:
                    nicks.append(nick)  #All existing nick in one list
                score = ((line.split('|'))[1]).replace(" ","")
                if nick.upper() == (self.imie).upper() and int(score) < self.score: #Replacing the line with the same nick, but higher score
                    destiny.write((nick.capitalize()).ljust(size//2)+'|'+(str(self.score)).rjust(size//2)+'\n')
                else:
                    destiny.write(line) #Rewriting the line
        if (self.imie).capitalize() not in nicks:
            destiny.write(((self.imie).capitalize()).ljust(size // 2) + '|' + (str(self.score)).rjust(size // 2) + '\n')    #Adding a new new nick and his score

