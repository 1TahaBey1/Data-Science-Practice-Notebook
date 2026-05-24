#Q1
import rectangle
import circle

def display_menu():
    print("1- Area of the circle")
    print("2- Circumference of a circle")
    print("3- Area of a rectangle")
    print("4- Perimeter of a rectangle")
    print("5- Quit")

donme = True
while donme == True:  
    display_menu()  
    selection = input("please enter what u want to do ")
    if selection == "1":
        radius = float(input("Please enter the radius : "))
        circle.circle_area(radius) 
        donme = True
    elif selection == "2": 
        radius = float(input("Please enter the radius : "))
        circle.circle_circumference(radius)  
        donme = True
    elif selection == "3": 
        length = float(input("please enter the length : "))
        width =  float(input("please enter the width : "))
        rectangle.area_rectangle(length,width)
        donme = True
    elif selection == "4": 
        length = float(input("please enter the length : "))
        width =  float(input("please enter the width : "))
        rectangle.perimeter_rectangle(length,width)     
        donme = True
    elif selection == "5":
        print("u quit the menü ")      
        donme = False
    else: 
        print("İnvalid input ")   
        donme = False 
          
#Q2

project_number = int(input("please enter the number of the videos in the project"))

file = open("Q2_video_time.txt","w")

for i in range(1,project_number+1):
    running_time = float(input("please enter the running time"))
    file.write(str(running_time)+ "\n")
file.close()        
print("the times saved to Q2_video_time")
 
#Q3
total = 0
count = 0
file = open("Q2_video_time.txt","r")
for line in file:
    running_time = float(line)
    count += 1
    print("video " + str(count) + " " +str(running_time))
    total += running_time
file.close()
print("The total running time is " + str(total) + " seconds.")

#Q4
file = open ("sales.txt","w")
for day in range(1,4):
    sales = float(input("enter the sales for the day # " + str(day)))
    file.write(str(sales) + "\n")

file.close()    
print("Data written to sales.txt")

#Q4_2
try: 
    file = open("sales.txt","r")
    total = 0 

    for line in file:
        sale = float(line)
        total += sale
    
    file.close()
    print("total sales " + str(total ))

except IOError  : 
    print("IO error occured")

except ValueError as error: 
    print(error)
    
finally : 
    if file !=None: 
        file.close()    
        
#Q5

file = None 
try: 
    file = open("sales.txt","r")
    total = 0 

    for line in file:
        sale = float(line)
        total += sale
    
    file.close()
    print("total sales " + str(total ))

except Exception : 
    print("error occured ")
    
finally : 
    if file !=None: 
        file.close()        

#Q6
items = [] 
items.append("pizza")
items.append("burgers")
items.append("chips")

print("here is the items in the food list" )
print(items )
will_change = input("which item should I change")
for i in range(len(items)) : 
    if items[i] == will_change :
        changed_item = input("please enter the new item ")
        items[i] = changed_item

print("here is the revised list ")
print(items)  

#Q7
employees =["John","Wayne","Cris","Jack","Paul","Moris"]

hourly_pay = 12.75
hours = []

for i in range(len(employees)):
    work_hour = float(input("please enter the hour for the " + employees[i] ))
    hours.append(work_hour)
    
for i in range(len(hours)):
    gross_pay = hours[i]*hourly_pay
    print("gross pay for" + employees[i] + "is" + str(gross_pay))    
    
#Q8
import random 
values = [
    [0,0,0,0]
    [0,0,0,0]
    [0,0,0,0]
] 
for row in range(3):
    for col in range(4): 
        values [row][col] = random.randint(1,100)

for row in values:
    print(row)      

#Q9-1
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[3:6])
#Q9-2
my_tuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(my_tuple[1][1])
#Q9-3
tuple = (50,)
print(tuple)
#Q9-4
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
for student in students:
    if student[1] >= 90:
        print(student) 
          
