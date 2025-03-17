import random
a = random.randint(10,20)
guess = int(input("Please enter a number from 10 to 20:" ))
while True:
  if guess==a:
    print("Congratulation")
    break
