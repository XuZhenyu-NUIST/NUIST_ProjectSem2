import random
a = random.randint(10,20)
guess = None
while guess != a:
  guess = int(input("Please enter a number from 10 to 20: "))
  if guess == a:
    print("Congratulation")
  else:
    print("Try again")
