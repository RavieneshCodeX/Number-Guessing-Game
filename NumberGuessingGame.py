import random
import time

range1 = int(input("Enter lower bound:- ")) 

range2 = int(input("Enter upper bound:- "))    

rand = random.randint(range1, range2)

attempt = int(input("How many tries do you want to attempt ? "))

for attempt in range(attempt):
    guess = int(input("Your guess: "))
    
    if guess > rand:
        print("Your guess is too high!")
        
    if guess < rand:
        print("Your guess is too low!")

    else:
        print("Congratulations! You got it right")
        break
        
time.sleep(30)        
         
