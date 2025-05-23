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
    load_menu()
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
import json
        
def save_menu():
    with open("menu.json", "w") as f:
            json.dump(menu, f)
        
def load_menu():
    global menu
    try:
        with open("menu.json", "r") as f:
            menu = json.load(f)
    except FileNotFoundError:
            pass  # Use default menu if file doesn't exist
        
        # At the start of your script, call load_menu()

def add_new_item():
    new_item=input("enter item name:")
    new_item_price=int(input("enter item price:"))
    menu.update({new_item:new_item_price})
    save_menu()
    

def remove_item():
    del_item=input("enter delete item:")
    if del_item in menu:
        del menu[ del_item]   
        save_menu()  
        
    else:
        print("item is not in menu")

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
    print("\n1.Show Menu \n2.Take Order \n3.Generate Bill \n4.Add New Item \n5.Remove Item \n6.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        show_menu()
       
    elif choice==2:
        take_order()
      
    elif choice==3:
        generate_bill()
    elif choice==4:
        
        add_new_item()
    elif choice==5:
        remove_item()
        
    elif choice==6:
        exit(0)
    else:
        print("wrong choice")


