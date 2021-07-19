'''We often need to convert the information in a "string" to a list = []
this be be related to the who's paying exercise '''
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_choice = random.randint(0, len(names) -1)
bill_payer = names[random_choice]


print(f"{bill_payer} is going to buy the meal today")

