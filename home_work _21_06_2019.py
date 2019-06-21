
#------------------------
# #exercise_9(21_06_2019)
#------------------------
# list_founction = ["add", "sub", "mul", "div"]

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
# #exercise_10(21_06_2019)
#--------------------------
import random
Mirange = random.randrange(400,1000)
Marange = random.randrange(400,1000)
print (Mirange,Marange)

def getInRange (min,max):
    if

getInRange (Mirange,Marange)


#-----------------------
#exercise_10(21_06_2019)
#-----------------------

list_max_min = []

def max_min(x):
    list_max_min.append(x)

#max_min(10)
#max_min(30)
#max_min(900)

max_min( int(input('Enter Number: ')))
max_min( int(input('Enter Number: ')))
max_min( int(input('Enter Number: ')))

print (min(list_max_min))



