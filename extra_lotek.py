from totomodul import ustawienia, losujliczby, pobierztypy, wyniki

#------------PROGRAM GŁÓWNY------------------
def main(args):
  # ustawienia gry
  nick, ileliczb, maksliczba, ileprob = ustawienia()

  # losowanie liczb
  liczby = losujliczby(ileliczb, maksliczba)

  # wytypowanie liczb
  for i in range(ileprob):
    typy = pobierztypy(ileliczb, maksliczba)
    iletraf = wyniki(set(liczby), typy)

  return 0

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))