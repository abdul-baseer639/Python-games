import random
n= random.randint(1,100)
a=-1
guesss=1
while(a != n):
  a=int(input("Enter a number: "))
  if(a<n):
    print("guessed lower number ")
    guesss+=1
  else:
    print("guessed higher number")
    guesss+=1
print(f"you guessed the correct number in {guesss} attempts")      
