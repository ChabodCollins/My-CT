# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:09:59 2024

@author: Felix
"""

'''
    Add Product
    Sell Product
    Delete Product
    View Product
    
    
    products = {
            "name": ['Yam', 'Beans', 'Rice'],
            "Price": [2000, 3000, 5000],
            "Quantity": [20, 30, 35]
        }
    
    products["name"][1]

'''

def prompt():
    print ("\n\tMini Point of sale")
    print ("\t1->Add Product")
    print ("\t2->Sell Product")
    print ("\t3->Delete Product")
    print ("\t4->View Product")
    print ("\t5->Exit")
    
    value = int (input("Enter your Option: "))
    return value

products = {
    "name": [],
    "price": [],
    "quantity": []
    }

running = True
while running:
    action = prompt()
    print (action)
    
    if action == 1:
        name = input("Enter Product Name: ")
        if name in products["name"]:
            print ("Prduct already in stock.")
        
        else:
            price = int(input("Enter Product Price: "))
            quantity = int (input("Enter Product Quantity: "))
            products["name"].append(name)
            products["price"].append(price)
            products["quantity"].append(quantity)
            print ("\nProduct added Successfully")
    
    elif action == 2:
        name = input ("Enter Product Name: ")
        if name in products["name"]:
            quantity = int(input("Enter Quantity: "))
            index = products["name"].index(name)
            if quantity <= products["quantity"][index]:
                products["quantity"][index] -= quantity
                amount = quantity * products["price"][index]
                print (f"Succesfully bought {name} and you paid {amount}")
            else:
                print ("Product out of stock")
        else:
            print ("Product not Availabe.")
    
    elif action == 3:
        name = input ("Enter Product Name: ")
        if name in products["name"]:
            index = products["name"].index(name)
            del products["name"][index]
            del products["price"][index]
            del products["quantity"][index]
            print (f"Succesfully deletec {name} from store")
        
        else:
            print ("Product not available")
    
    elif action == 4:
        print ("Name\tPrice\tQuantity")
        for i, name in enumerate(products["name"]):
            price = products["price"][i]
            quantity = products["quantity"][i]
            print (f"{name}\t\t{price}\t{quantity}")
    
    elif action == 5:
        running = False
        print ("\nCode Exiting!!!")
    
    else:
        print ("\nWrong Input Try again !!!")

print ("Bye Bye!!!")