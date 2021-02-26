#input a num
#generate num
#check for num with if and else
#loop while the answer is right 


import random
answer = random.randrange(1,21)
user = 0
while (user != answer):
  user = int(input("Enter a number between 1 - 20: "))
  if (user > answer):
    print("too high")
  elif (user < answer):
    print("too low")

print("You got it")

