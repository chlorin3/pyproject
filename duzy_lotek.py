import random

try:
  ileliczb = int(input("Ile liczb chcesz odgadnąć? "))
  maksliczba = int(input("Wpisz maksymalną losowaną liczbę: "))
  #print("Wytypuj", ileliczb, "z", maksliczba, "liczb:")
  if ileliczb > maksliczba:
    print("Błędne dane! Maksymalna liczba musi być mniejsza od ilości odgadywanych liczb!")
    exit()
except ValueError:
  print("Błędne dane!")
  exit()
  
#------------LOSOWANIE LICZB---------------
liczby = []
#print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
'''
for i in range(ileliczb):
  liczby.append(random.randint(1, maksliczba))
'''
i = 0
while i < ileliczb:
  liczba = random.randint(1, maksliczba)
  if liczby.count(liczba) == 0: #sprawdzenie czy liczba jeszcze się nie pojawiła w liście
    liczby.append(liczba)
    i = i + 1

print("Wylosowane liczby to:", liczby)

#-----------ZGADYWANIE LICZB-------------
print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))

for i in range(3):
  typy = set()
  i = 0
  while i < ileliczb:
    try:
      typ = int(input("Podaj %s. liczbę: " % (i + 1)))
      if typ not in typy:
        typy.add(typ)
        i = i + 1
    except ValueError:
      print("Błędne dane!")
      
  #--------SPRAWDZENIE TRAFIONYCH LICZB----------
  trafienia = set(liczby) & typy
  if len(trafienia) == ileliczb:
    print("Gratulacje! Wytypowałaś prawidłowe liczby :)")
    break
  elif trafienia:
    print("Trafienia %s z %s" % (len(trafienia), ileliczb))
    print("Trafione liczby: ", trafienia)
  else:
    print("Ojjj, brak trafień. Spróbuj jeszcze raz! :)")
  #print("\nxxxxxxxxxxxxxxxxxxxxxxxxx\n")
  print("\n" + "=" * 40 + "\n")
  
print("Wylosowane liczby: ", liczby)