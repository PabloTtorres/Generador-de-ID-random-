from random import random, randint
import string 
def user_id_gen_by_user():
  inp1 = int(input("Ingresa un numero"))
  inp2 = int(input("Numero de ID's")) 
  p = list(string.ascii_letters)
  x = ""
  k = inp2
  while k>0:
    lst = []
    for i in range(inp1):

      d = randint(1,2)
      if d == 1:
          l = randint(0,9)
          x+= str(l)

      else:
          b = randint(0,50)
          x+= str(p[b])
    print(x)
    k-=1
    x = ""

user_id_gen_by_user()

