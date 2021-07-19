'''repeating something over and over and over again
for loop goes thorugh each item in a list and performs an action on each item
 1st time it runs fruit is equal to apple
 2nd time it runs fruit is equal to Peach etc ....
 inside a for loop (indentation) will get carried our as many times as the
 for loop needs to repeat
outside the the for loop will print after the for loop has done
 '''

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)