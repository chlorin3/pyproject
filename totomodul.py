import os
#-----------------PROGRAM - FUNKCJE--------------------
import random

def ustawienia():
  '''Funkcja pobiera ilość losowanych liczb, maksymalną wartość oraz ilość prób.
  Pozwala określić stopień trudności gry.'''
  nick = input("Wprowadź nick: ")
  nazwapliku = nick + ".ini"
  gracz = czytaj_ust(nazwapliku)

  while True:
    try:
      ileliczb = int(input("Wprowadź ilość typowanych liczb: "))
      maksliczba = int(input("Wprowadź maksymalną losowaną liczbę: "))
      if ileliczb > maksliczba:
        print("Błędne dane! Ilość liczb typowanych musi być mniejsza od wartości maksymalnej liczby.")
        continue #przerywa działanie pętli i przechodzi do jej początku
      ileprob = int(input("Ile prób: "))
      return (nick, ileliczb, maksliczba, ileprob)
    except ValueError:
      print("Błędne dane")
      continue

def losujliczby(ileliczb, maksliczba):
  '''Funkcja losuje maksliczba liczb'''
  liczby = list()
  
  i = 0
  while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
      liczby.append(liczba)
      i = i + 1
  print(liczby)
  return liczby

def pobierztypy(ileliczb, maksliczba):
  '''Funkcja pobiera wytypowane liczby przez użytkownika'''
  typy = set()
  i = 0
  while i < ileliczb:
    try:
      typ = int(input("Wprowadz %s liczbę: " % (i + 1)))
    except ValueError:
      print("Błędne dane!")
      continue
    
    if 0 < typ <= maksliczba and typ not in typy:
      typy.add(typ)
      i = i + 1
  return typy

def wyniki(liczby, typy):
  '''Funkcja porównuje wylosowane i wytypowane liczby, zwraca ilość trafień'''
  trafione = set(liczby) & typy

  if trafione:
    print("\nIlość trafień: %s" % len(trafione))
    trafione = ", ".join(map(str, trafione))
    print("\nTrafione liczby: %s" % trafione)
  else:
    print("Brak trafień")
      
  print("\n" + "=" * 40 + "\n")

  return len(trafione)

def czytaj_ust(nazwapliku):
  if os.path.isfile(nazwapliku):
    plik = open(nazwapliku, "r")
    linia = plik.readline()
    plik.close()
    if linia:
      return linia.split(";")
    return False
    
def zapisz_ust(nazwapliku, gracz):
  plik = open(nazwapliku, "w")
  plik.write("; ".join(gracz))
  plik.close()