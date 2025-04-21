import random 
n = random.randint(1,100)
a=0
guess = None
while(guess != n):
    guess=int(input("guess the number:"))
    a=a+1
    if guess>n:
        print("lower number plese")
    elif guess<n:
        print("higher number please")
    else:
        print("you have guessed the number")
print(f"and you guessed it in {a} attemptes")
    
