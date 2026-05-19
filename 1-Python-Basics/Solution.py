#q1
print("what is your name ? ")
name = input(str);
print("What is your age ")
age = input(int )
print ("What is your income ")
income = input(int )
print ("Here is the data you entered" )
print("Name " + name )
print("Age " + age )
print("Income  " + income )

#q2
f = 10000
n = 10
r = float(input("Please enter the rate "))
p = f/((1+r)**n)
print ("if you want to have 10k after 10 years ")
print(str(p) + "u need to invest now")

#q3
grade = int(input("please enter your grade"))
letter_grade = str
if grade > 90 : letter_grade = 'A'
elif 90 > grade >= 80 : letter_grade = 'B'
elif 80 > grade >= 70 : letter_grade = 'C'
elif 70> grade >= 60  : letter_grade = 'D'
else : letter_grade = 'F'
print("here is that your letter grade " + letter_grade)

#q4
name1 = "Mary"
name2 = "Mark"
if name1 >name2: print("Mary is greater than mark ")
else: print ("Mary is not greater tan mark") 

#q5
print("KPH \t MPH")
for kph in range(60, 131, 10):
    mph = kph * 0.6214

    print(kph, "\t", format(mph, ".1f"))

#q6
fname = input("please enter your first name ")
lname = input("please enter your last name ") 
fullname = fname+lname 
print (fullname[::-1])   

#q7
import random
yesno = "y"
while yesno == "y":
    print("Do you want to roll the dice y/n ?")
    yesno = input().lower()

    if yesno == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("Dice 1:", dice1)
        print("Dice 2:", dice2)
    else : yesno == "n"      
    
#q8
import math
radius = float(input("Please enter te radius of te circle "))
area = math.pi*radius**2
circumference = 2*math.pi*radius    
print("Area: " + str(area) + " Circumference : "+ str(circumference))