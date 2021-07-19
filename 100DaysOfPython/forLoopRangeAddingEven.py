total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total = total + number #long hand for below
print(total)

total1 = 0
for number in range(2, 101, 2):#if you start form 1 yoyour first number would be 3
    total1 += number
print(total1)