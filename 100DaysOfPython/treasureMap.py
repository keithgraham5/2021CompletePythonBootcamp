# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
if position == "11":
    map[0][0] = "X"
if position == '12':
    map[1][0] = "X"
if position == '13':
    map[2][0] = "X"
if position == '21':
    map[0][1] = "X"
if position == '22':
    map[1][1] = "X"
if position == '23':
    map[2][1] = "X"
if position == '31':
    map[0][2] = "X"
if position == '32':
    map[1][2] = "X"
if position == '33':
    map[2][2] = "X"
else:
    print("Sorry that location is not on the island ")







#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")