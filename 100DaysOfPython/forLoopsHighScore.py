
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]


#Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The Highest score in the class is: {highest_score}")