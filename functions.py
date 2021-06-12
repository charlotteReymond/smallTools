# current functions

def nbrsolution(n): # return the number of phytagorean possiblites
   liste.clear()
   carré=int(n/2)
   for a in range(1,carré+1):
      for b in range(1,carré+1):
         for c in range(1,carré+1):
            if a**2+b**2==c**2:
               if a+b+c==n:
                  nbr=a*c*b
                  liste.add(nbr)
   return(len(liste))

def pandigital(n,x): # return True if n is a pandigital number of x
   a=0
   string=str(n)
   for i in range(1,10):
      string2=str(i)
      if string2 in string:
         a+=1
   if a == x:
      return(True)
   else:
      return(False)

def isPrime(n): # return True if n is prime
   m = int(n)
   if m==1 or m == 0:
      return(False)
   for i in range(2, m):
      if m%i==0 :
         return(False)
         break
   return(True)

def rotate(strg, n): # rotate strg of n chars
    return strg[n:] + strg[:n]

def factorial(nbr): #return the factorial of nbr
   fact = 1
   i=1
   while (i<=nbr):
      fact=fact*i
      i+=1
   return(fact)

def sommeDiviseurs(n):#return the sum of divisors of n
   somme=0
   for i in range(1,n):
      nbr=int(n)
      if nbr%i == 0 :
         somme += i
   return(somme)

def average(a,b) :#return the arithmetic average of a and b
   return(a + b) / 2

def squareRoot(num=9,low=2,high=5) :#return the square root 
   average(low,high)
   for i in range(20) :
      guess = average(low,high)
      if guess**2 == num :
         print(guess)
      elif guess**2 >  num : 
         high = guess
      else :
         low=guess
   return(guess)




