import random 
number = random.randint(1,100)

guessesTaken = 0

print("I'm thinking of a number between 1 and 100, can you guess what it is?")

while guessesTaken < 6 :
  guess = int(input("Take a guess: "))

  guessesTaken +=1

  if guess < number :
    print("Too Low! : ")

  if guess > number : 
      print("Too high! : ")

  if guess == number :
     break

if guess == number :
  guessesTaken = str(guessesTaken)
  print("Congratulations! You guessed my number in " +  guessesTaken + " guesses!") 

else:
  print("Sorry, you didn't guess my number within 6 attempts! The number I was thinking of was "  + str(number))