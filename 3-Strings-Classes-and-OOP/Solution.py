#Q2
def get_login_name(first_name, last_name, student_id):
    first_part = first_name[:3]
    last_part = last_name[:3]
    id_part = student_id[-3:]
    
    login_name = first_part + last_part + id_part
    return login_name

first_name = input("enter your first name : ")
last_name = input("enter your last name : ")
student_id = input("enter your student ID : ")
login = get_login_name(first_name, last_name, student_id)

print("generated login name ", login)

#Q4   
date = input("please enter the date dd/mm/yyyy: ")
parts = date.split("/")

print("day :", parts[0])
print("month :", parts[1])
print("year :", parts[2])

#Q7
from CellPhone import Cell_Phone

phone1 = Cell_Phone()

phone1.set_manufacturer(
    input("please enter the manufacturer of the phone : " )
)
phone1.set_model(
    input("please enter the model of the phone : " )
)
phone1.set_reatil_price(
    float(input("please enter the retail price of the phone :" ))
)

print("here is the data that you enter : ")
print("manufacturer : ", phone1.get__manufacturer())
print("model number : ", phone1.get_model_number())
print("retail price : ", phone1.get_retail_price())