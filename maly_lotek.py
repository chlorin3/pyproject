import random

liczba = random.randint(1, 10)
#print("Wylosowana liczba to: ", liczba, "\n")

for i in range(3):
  print("Próba ", i+1)
  odpowiedz = input("Jaką liczbę od 1 do 10 mam na myśli? ")
  #print("Twoja odpowiedź ", odpowiedz)
  
  if liczba == int(odpowiedz):
    print("Brawo! Zgadłaś! Wygrywasz nic :)")
    break
  elif i == 2:
    print("Źle. Mam na myśli liczbę ", liczba)
  else:
    print("Nie zgadłaś. Spróbuj jeszcze raz... \n")