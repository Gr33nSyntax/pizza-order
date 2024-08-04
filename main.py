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
"""Pick Up Function - submits information, moves onto Number of Pizzas window."""
def pu_submit_function():
    name_ent = pu_name_ent.get()
    name_check = name_ent.isspace()
    if len(name_ent) != 0 and name_check == False:
        global name 
        name = pu_name_ent.get()
        pick_up_window.destroy()
        number_pizzas_function()

"""Pick Up Function - cancels order, goes back to order type page"""
def pu_cancel_order_function():
    pick_up_window.destroy()
    order_type_function()

"""Pick Up Function - creates Pick Up window"""
def pick_up_function():
    global pick_up_window
    pick_up_window = tk.Tk()
    pick_up_window.title("Dream Pizzas - Pick Up")
    pick_up_window.geometry("500x300")
    pick_up_window.minsize(500, 300)
    pick_up_lbl = tk.Label(master=pick_up_window,  
                            text="Pick Up",
                            font=("Zain", 32))
    pu_name_lbl = tk.Label(master=pick_up_window, 
                            text="Name:",
                            font=("Zain", 24))
    global pu_name_ent
    pu_name_ent = tk.Entry(master=pick_up_window,
                             font=("Zain", 18))
    pu_submit_btn = tk.Button(master=pick_up_window,
                              text="Submit",
                              font=("Zain", 24),
                              command=pu_submit_function)
    pu_cancel_order_btn = tk.Button(master=pick_up_window,
                                 text="Cancel Order",
                                 font=("Zain", 12),
                                 command=pu_cancel_order_function)
    pick_up_lbl.pack(anchor="n")
    pu_name_lbl.pack(anchor="center", expand=True)
    pu_name_ent.pack(anchor="center", expand=True)
    pu_submit_btn.pack(anchor="center", expand=True)
    pu_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    pick_up_window.mainloop()

# Delivery Window Functions
"""Delivery Function - submits information, moves onto Number of Pizzas window."""
def d_submit_function():
    name_ent = d_name_ent.get()
    address_ent = d_address_ent.get()
    phone_ent = d_phone_ent.get()
    name_ent_check = name_ent.isspace()
    address_ent_check = address_ent.isspace()
    phone_ent_check = phone_ent.isspace()
    if (len(name_ent) !=0 and name_ent_check == False 
        and len(address_ent) !=0 and address_ent_check == False 
        and len(phone_ent) !=0 and phone_ent_check == False):
        global name
        name = d_name_ent.get()
        global address
        address = d_address_ent.get()
        global phone_number
        phone_number = d_phone_ent.get()
        delivery_window.destroy()
        number_pizzas_function()


"""Delivery Function - cancels order, goes back to order type page"""
def d_cancel_order_function():
    delivery_window.destroy()
    order_type_function()

"""Delivery Function - creates delivery window"""
def delivery_function():
    global delivery_window
    delivery_window = tk.Tk()
    delivery_window.title("Dream Pizzas - Delivery")
    delivery_window.geometry("800x400")
    delivery_window.minsize(800, 400)
    delivery_lbl = tk.Label(master=delivery_window,  
                            text="Delivery",
                            font=("Zain", 32))
    d_disclaimer_lbl = tk.Label(master=delivery_window,
                                text="*$5 delivery fee applies",
                                font=("Zain", 12))
    d_name_frm = tk.Frame(master=delivery_window)
    d_name_lbl = tk.Label(master=d_name_frm,
                          text="Name:",
                          font=("Zain", 24))
    global d_name_ent
    d_name_ent = tk.Entry(master=d_name_frm,
                          font=("Zain", 18))
    d_address_frm = tk.Frame(master=delivery_window)
    d_address_lbl = tk.Label(master=d_address_frm,
                             text="Address:",
                             font=("Zain", 24))
    global d_address_ent
    d_address_ent = tk.Entry(master=d_address_frm,
                             font=("Zain", 18))
    d_phone_frm = tk.Frame(master=delivery_window)
    d_phone_lbl = tk.Label(master=d_phone_frm,
                           text="Phone:",
                           font=("Zain", 24))
    global d_phone_ent
    d_phone_ent = tk.Entry(master=d_phone_frm,
                            font=("Zain", 18))
    d_submit_btn = tk.Button(master=delivery_window,
                             text="Submit",
                             font=("Zain", 24),
                             command=d_submit_function)
    d_cancel_order_btn = tk.Button(master=delivery_window,
                                  text="Cancel Order",
                                  font=("Zain", 12),
                                  command=d_cancel_order_function)
    delivery_lbl.pack(anchor="n")
    d_disclaimer_lbl.pack(anchor="n")
    d_name_frm.pack(anchor="center", expand=True, pady=10)
    d_name_lbl.pack(expand=True, side="left")
    d_name_ent.pack(expand=True, side="left")
    d_address_frm.pack(anchor="center", expand=True, pady=10)
    d_address_lbl.pack(expand=True, side="left")
    d_address_ent.pack(expand=True, side="left")
    d_phone_frm.pack(anchor="center", expand=True, pady=10)
    d_phone_lbl.pack(expand=True, side="left")
    d_phone_ent.pack(expand=True, side="left")
    d_submit_btn.pack(anchor="center", expand=True)
    d_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    delivery_window.mainloop()

# Number of Pizzas Window Functions
"""Number of Pizzas Function - creates Number of Pizzas window"""
def number_pizzas_function():
    print("Number of Pizzas window")

order_type_function()