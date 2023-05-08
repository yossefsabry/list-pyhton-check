print('first way'.center(40,'#'))
list_1 = [10,30,50,-80,-20]
list_positive = []
list_nagitave = []

for x in list_1:
    if x > 0 :
        # print(x)
        list_positive.append(x)        
# print(list_positive)
sum_positive = sum(list_positive)
print('the total sum of positive numbers is :' ,sum_positive)

for t in list_1:
    if t < 0 :
        # print(t)
        list_nagitave.append(t)        
# print(list_nagitave)
sum_nagive = sum(list_nagitave)
print('the total sum of nagitive numbers is :',sum_nagive)

print('second way'.center(40,'#'))

list1 =  [10,30,50,-80,-20]
sum_positive = 0 # number of positive
sum_negative = 0 # number of negative
for n in list1:
    if n > 0:
        sum_positive += n
    elif n < 0:
        sum_negative += n
print("Sum of positive numbers is:", sum_positive)
print("Sum of negative numbers is:", sum_negative)

print('third way'.center(40,'#'))

nums =  [10,30,50,-80,-20]
positives = [num for num in nums if num >= 0]
negatives = [num for num in nums if num < 0]
print("Sum of positive numbers is:", positives)
print("Sum of positive numbers is:", sum(positives))
print("Sum of negative numbers is:", sum(negatives))


print('four way'.center(40,'#'))

nums =  [10,30,50,-80,-20]
positives = []
nagative = []
for num in nums:
    if num>= 0:
        positives.append(num)
    else:
        nagative.append(num)
print("Sum of positive numbers is:", sum(positives))
print("Sum of negative numbers is:", sum(nagative))
