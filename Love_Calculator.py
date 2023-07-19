# Love Calculator

print("Welcome to the LOVE CALCULATOR ❤️")
name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")

name = name1 + name2
lower_case_name = name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
score = int(love_score)

#score = int( str(true) + str(love) )

if score <10 or score >90 :
  print(f"Your score is {score} , You go together like coke and mentos .")
elif score>=40 and score <=50:
  print(f"Your score is {score} , you are alright together .")
else :
  print(f"Your score is {score} .")
