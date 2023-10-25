import math

def PpKuli(r):
      return 4*math.pi*r**2

while True:
      inp = input()
      if inp =="a":
            data = float(input())
            print(PpKuli(data))
      elif inp == "b":
            break
      else:
            print("Nie ma takiej komendy")      