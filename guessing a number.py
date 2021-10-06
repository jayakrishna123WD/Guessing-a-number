#Import random module for generating random numbers
import random

#created a variable for random number 
random_number = random.randint(1,10) 

#initiated a count variable for repeat process of while loop
count = 0         

#number of limits to guess the numbe is 5
while count < 5:
    number = int(input("Enter the number to guess : "))
    if random_number > number:
        print(number,"is small, guess again...")
    elif random_number < number:
        print(number,"is high, guess again.....")
    elif random_number == number:
        print(f"you guessed the number correctly in {count} tries")
    count += 1
if count == 5:
    print("You crossed the guess limit")