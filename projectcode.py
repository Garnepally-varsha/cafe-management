menu ={
    "coffee":300,
    "tea":250,
    "biscuit":100,
    "cake":200,
    "shakes":300,
    "sandwich":250,
}
order={}

def show_menu():
    print(menu)

def take_order():
    anything="start"
    while(anything!="stop"):
        item=input("order please:")
        if item in menu:
            quantity=int(input("enter quantity:"))
            order.update({item:quantity})
           
        else:
            print("item is not in menu")
        anything=input("want to add item enter 'start' if not 'stop' :")

def calculate_total():
    total=0
    for item in order:
        item_total=menu[item]*order[item]
        total+=item_total
    print(total)

import datetime
def generate_bill():
    print("\n****** v cafe ******")
    print("\n ")
    print(datetime.datetime.now())
    print("\n")
    for item in order:
        print(menu[item],end="*")
        print(order[item],end="=")
        print(menu[item]*order[item])
    print("the total amount is ",end="")
    calculate_total()
    order.clear()

print("********* welcome to v cafe **********")
while True:
    print("\n1.Show Menu \n2.Take Order \n3.Generate Bill \n4.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        show_menu()
       
    elif choice==2:
        take_order()
      
    elif choice==3:
        generate_bill()
        
    elif choice==4:
        exit(0)
    else:
        print("wrong choice")


