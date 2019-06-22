#------------------------
# #exercise_8(21_06_2019)
#------------------------

def CircleScope (R):
    calculate = 2*3.14*R
    print(calculate)
CircleScope(int(input('Enter Number_1: ')))

#------------------------
# #exercise_9(21_06_2019)
#------------------------
 list_founction = ["add", "sub", "mul", "div"]

for Type_founction in list_founction:

    def Type_founction (x=0,y=0):
        print(" ")
        add =x+y
        sub =x-y
        mul = x*y
        div = x/y
        print(f'add:{add}, sub:{sub}, mul:{mul}, div:{div}')

    Type_founction (int(input('Enter Number_1: ')),int(input('Enter Number_2: ')))
    break

#-------------------------
# #exercise_10(21_06_2019) *****8
#--------------------------
import random

num_1 = random.randrange(150)
num_2 = random.randrange(150)

def getInRange (min,max):
    a = min >= 10 and min <=100
    b = max >=10 and max <=100

    if a and b:
        print ("Yes:",num_1,num_2)
    else:
        print("No: ",num_1,num_2)

getInRange (num_1,num_2)

#-----------------------
#exercise_10(21_06_2019)
#-----------------------

list_max_min = []

for row in range(3):

    Number = int(input('Enter Number: '))

    def max_min(x):
        list_max_min.append(x)

    max_min(Number)

print ("min:",min(list_max_min))
print ("min:",max(list_max_min))




