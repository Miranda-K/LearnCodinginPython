import random
number = random.randint(1, 10)
guess = int(input("Guess the number! "))
while True:
  if guess < number:
    print("The number is too low!")
    guess = int(input("Guess again! "))
  elif guess > number:
    print("The number is too high!")
    guess = int(input("Guess again! "))
  elif guess == number:
    print ("Congratulations, you have guessed the number!")
    break