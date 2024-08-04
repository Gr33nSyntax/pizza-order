"""A program that will a phone operator to input an order for a customer."""
import tkinter as tk
from tkinter import font

# Global Variables
global saved_orders
saved_orders = {"order_demo": ["Name", 
                               "Address", 
                               "Phone", 
                               ["Chosen pizza(s) list"], 
                               "Total price"]}
global PIZZAS
PIZZAS = {"Classic Margherita": 10.50, 
          "Pepperoni Delight": 10.50, 
          "Veggie Supreme": 10.50, 
          "BBQ Chicken": 10.50, 
          "Hawaiian Paradise": 10.50,
          "Four Cheese Extravaganza": 10.50,
          "Meat Lover’s Feast": 10.50,
          "Truffle Mushroom Bliss": 15.50,
          "Prosciutto & Arugula Delight": 15.50,
          "Fig & Goat Cheese Fantasy": 15.50,
          "Lobster & Lemon Zest": 15.50,
          "Pesto & Sun-Dried Tomato Medley": 15.50}

# General Functions
"""General Function - terminates program"""
def terminate_program_function():
    with open("saved_orders.txt", "a") as output:
        for key, value in saved_orders.items():
            output.write(f"{key}: {value}\n")
    exit()

# Order Type Functions
"""Order Type Function - submits information, moves onto Pickup window"""
def ot_pu_function():
    global address
    address = "N/A"
    global phone_number
    phone_number = "N/A"
    order_type_window.destroy()
    pick_up_function()

    
"""Order Type Function - moves onto Delivery window"""
def ot_d_function():
    order_type_window.destroy()
    delivery_function()

# Order Type Window
def order_type_function():
    global order_type_window
    order_type_window = tk.Tk()
    global current_window
    current_window = order_type_window
    order_type_window.title("Dream Pizzas - Order Type")
    order_type_window.geometry("500x300")
    order_type_window.minsize(500, 300)
    order_type_lbl = tk.Label(master=order_type_window,  
                            text="Order Type",
                            font=("Zain", 32))
    ot_pickup_btn = tk.Button(master=order_type_window, 
                            text="Pickup",
                            font=("Zain", 24),
                            width=10,
                            command=ot_pu_function)
    ot_delivery_btn = tk.Button(master=order_type_window, 
                                text="Delivery",
                                font=("Zain", 24),
                                width=10,
                                command=ot_d_function)
    ot_exit_btn = tk.Button(master=order_type_window, 
                            text="Exit",
                            font=("Zain", 12),
                            command=terminate_program_function)
    order_type_lbl.pack(anchor="n")
    ot_pickup_btn.pack(anchor="center", expand=True)
    ot_delivery_btn.pack(anchor="center", expand=True)
    ot_exit_btn.pack(anchor="se", padx=10, pady=10)
    order_type_window.mainloop()

#Pick Up Window Functions
"""Pick Up Function - creates Pick Up window"""
def pick_up_function():
    print('Pick Up Window')

# Delivery Window Functions
"""Delivery Function - creates delivery window"""
def delivery_function():
    print('Delivery Window')
    
order_type_function()