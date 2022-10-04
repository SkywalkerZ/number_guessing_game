import random as rd
from art import logo

userChoice =[5,10]

def numGen():
  number = rd.randint(1,101)
  return number
  
def welcome(value):
  print("Welcome to the Number Guessing Game")
  print("I am thinking of a number between 1 and 100")
  # print(f"The number is {value}") #Uncomment this line to view the random number

#Function to check user's guess against actual answer.
def compare(number, answer):
  if number > answer:
    print("\nToo Low\nGuess again\n")
    return 0
  elif number < answer:
    print("\nToo High\nGuess again\n")
    return 0
  elif number == answer:
    print("You guessed the correct number")
    return 1

print(logo)
randNum = numGen()
welcome(randNum)
choice = input("Choose a difficulty. Type 'easy' for easy-mode or 'hard' for hard-mode: ").lower()

#Steps to set difficulty.
if choice == 'easy':
  guessCounter = userChoice[1]
elif choice == 'hard':
  guessCounter = userChoice[0]
  
print(f"\nYou have {guessCounter} attempts remaining to guess the number")

for guess in range(1,guessCounter+1):
  
  userAnswer = int(input("\nMake a guess: "))
  solution = compare(randNum,userAnswer)
  popupCounter = guessCounter - guess

  if solution == 1:
    break
  elif solution == 0:
    print(f"You have {popupCounter} attempts remaining to guess the number")

  if guess == guessCounter:
    print("\nYou are out of attempts")
