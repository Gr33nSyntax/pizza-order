"""A program that will a phone operator to input an order for a customer."""
import tkinter as tk
from tkinter import ttk
import os

# VARIABLES, LISTS, AND DICTIONARIES
global saved_orders
saved_orders = {"order_demo": ["Name",
                               "Address",
                               "Phone",
                               ["Chosen pizza(s) list"],
                               "Total price"]}
global order
order = 0
global total_price
total_price = 0
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

# GENERAL FUNCTIONS


def terminate_program_function():
    """General Function - terminates program"""
    # Opens saved_orders.txt file
    os.startfile("saved_orders.txt")
    # Terminates the program
    exit()


# ORDER TYPE FUNCTIONS


def ot_pu_function():
    """Order Type Function - submits information, moves onto Pickup window"""
    # Declares address variable, and sets to "N/A" as it is not needed
    global address
    address = "N/A"
    # Declares phone_number variable, and sets to "N/A" as it is not
    # needed
    global phone_number
    phone_number = "N/A"
    # Destroys Order Type window
    order_type_window.destroy()
    # Calls Pick Up window function
    pick_up_function()


def ot_d_function():
    """Order Type Function - moves onto Delivery window"""
    # Destroys Order Type window
    order_type_window.destroy()
    # Calls Delivery window function
    delivery_function()


# ORDER TYPE WINDOW


def order_type_function():
    """Order Type Function - creates the Order Type window"""
    # Creates window and defines window properties
    # Makes order_type_window a global variable so it can be accessed
    # elsewhere
    global order_type_window
    order_type_window = tk.Tk()
    global current_window
    current_window = order_type_window
    order_type_window.title("Dream Pizzas - Order Type")
    order_type_window.geometry("500x300")
    order_type_window.minsize(500, 300)
    # Creates widgets and defines widget properties
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
    # Packs widgets and defines widget placement
    order_type_lbl.pack(anchor="n")
    ot_pickup_btn.pack(anchor="center", expand=True)
    ot_delivery_btn.pack(anchor="center", expand=True)
    ot_exit_btn.pack(anchor="se", padx=10, pady=10)
    # Runs the window
    order_type_window.mainloop()


# PICK UP WINDOW FUNCTIONS


def pu_submit_function():
    """Pick Up Function - submits information, moves onto Number of Pizzas
    window."""
    # Declares total_price variable, and sets to 0 as no delivery fee
    global total_price
    total_price = 0
    # Retrieves value in pu_name_ent entry widget
    name_ent = pu_name_ent.get()
    # Checks if name_ent is only whitespace
    name_check = name_ent.isspace()
    # Checks if name_ent is not empty and name_check is False
    if len(name_ent) != 0 and name_check is False:
        # If conditions are met, sets name variable to pu_name_ent
        # value
        global name
        name = pu_name_ent.get()
        # Destroys Pick Up window
        pick_up_window.destroy()
        # Calls Number of Pizzas window function
        number_pizzas_function()


def pu_cancel_order_function():
    """Pick Up Function - cancels order, goes back to order type page"""
    # Destroys Pick Up window
    pick_up_window.destroy()
    # Calls Order Type window function
    order_type_function()


def pick_up_function():
    """Pick Up Function - creates Pick Up window"""
    # Creates window and defines window properties
    # Makes pick_up_window a global variable so it can be accessed elsewhere
    global pick_up_window
    pick_up_window = tk.Tk()
    pick_up_window.title("Dream Pizzas - Pick Up")
    pick_up_window.geometry("500x300")
    pick_up_window.minsize(500, 300)
    # Creates widgets and defines widget properties
    pick_up_lbl = tk.Label(master=pick_up_window,
                           text="Pick Up",
                           font=("Zain", 32))
    pu_name_lbl = tk.Label(master=pick_up_window,
                           text="Name:",
                           font=("Zain", 24))
    # Makes pu_name_ent a global variable so it can be accessed
    # elsewhere
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
    # Packs widgets and defines widget placement
    pick_up_lbl.pack(anchor="n")
    pu_name_lbl.pack(anchor="center", expand=True)
    pu_name_ent.pack(anchor="center", expand=True)
    pu_submit_btn.pack(anchor="center", expand=True)
    pu_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    # Runs the window
    pick_up_window.mainloop()

# Delivery Window Functions


def d_submit_function():
    """Delivery Function - submits information, moves onto Number of Pizzas
    window"""
    # Adds 3 to total_price as there is a $3 delivery fee
    # Makes total_price a global variable so it can be accessed elsewhere
    global total_price
    total_price += 3
    # Retrieves values in d_name_ent, d_address_ent, and d_phone_ent entry
    name_ent = d_name_ent.get()
    address_ent = d_address_ent.get()
    phone_ent = d_phone_ent.get()
    # Checks if name_ent, address_ent, and phone_ent are only whitespace
    name_ent_check = name_ent.isspace()
    address_ent_check = address_ent.isspace()
    phone_ent_check = phone_ent.isspace()
    # Checks if name_ent, address_ent, and phone_ent are not empty and
    # name_ent_check, address_ent_check, and phone_ent_check are False
    if (len(name_ent) != 0 and name_ent_check is False
            and len(address_ent) != 0 and address_ent_check is False
            and len(phone_ent) != 0 and phone_ent_check is False):
        # If conditions are met, sets name, address, and phone_number variables
        # to d_name_ent, d_address_ent, and d_phone_ent values.
        # Makes name, address, and phone_number global variables so they can be
        # accessed elsewhere
        global name
        name = d_name_ent.get()
        global address
        address = d_address_ent.get()
        global phone_number
        phone_number = d_phone_ent.get()
        # Destroys Delivery window
        delivery_window.destroy()
        # Calls Number of Pizzas window function
        number_pizzas_function()


def d_cancel_order_function():
    """Delivery Function - cancels order, goes back to order type page"""
    # Destroys Delivery window
    delivery_window.destroy()
    # Calls Order Type window function
    order_type_function()


def delivery_function():
    """Delivery Function - creates delivery window"""
    # Creates window and defines window properties
    # Makes delivery_window a global variable so it can be accessed elsewhere
    global delivery_window
    delivery_window = tk.Tk()
    delivery_window.title("Dream Pizzas - Delivery")
    delivery_window.geometry("800x400")
    delivery_window.minsize(800, 400)
    # Creates widgets and defines widget properties
    delivery_lbl = tk.Label(master=delivery_window,
                            text="Delivery",
                            font=("Zain", 32))
    d_disclaimer_lbl = tk.Label(master=delivery_window,
                                text="*$3 delivery fee applies",
                                font=("Zain", 12))
    d_name_frm = tk.Frame(master=delivery_window)
    d_name_lbl = tk.Label(master=d_name_frm,
                          text="Name:",
                          font=("Zain", 24))
    # Makes d_name_ent a global variable so it can be accessed elsewhere
    global d_name_ent
    d_name_ent = tk.Entry(master=d_name_frm,
                          font=("Zain", 18))
    d_address_frm = tk.Frame(master=delivery_window)
    d_address_lbl = tk.Label(master=d_address_frm,
                             text="Address:",
                             font=("Zain", 24))
    # Makes d_address_ent a global variable so it can be accessed elsewhere
    global d_address_ent
    d_address_ent = tk.Entry(master=d_address_frm,
                             font=("Zain", 18))
    d_phone_frm = tk.Frame(master=delivery_window)
    d_phone_lbl = tk.Label(master=d_phone_frm,
                           text="Phone:",
                           font=("Zain", 24))
    # Makes d_phone_ent a global variable so it can be accessed elsewhere
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
    # Packs widgets and defines widget placement
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
    # Runs the window
    delivery_window.mainloop()

# Number of Pizzas Window Functions


def np_increase_function():
    """Number of Pizzas Function - adds 1 to the quantity of pizzas wanted"""
    # Retrieves value in np_number_ent entry widget
    number = int(np_number_ent.get())
    # Checks if number is greater than or equal to 1 and less than 5
    if number >= 1 and number < 5:
        # If conditions are met, sets np_number_ent value to number + 1
        np_number_ent.config(state="normal")
        np_number_ent.delete(0, tk.END)
        number += 1
        np_number_ent.insert(0, number)
        np_number_ent.config(state="disabled")


def np_decrease_function():
    """Number of Pizzas Function - subtracts 1 from the quantity of pizzas
    wanted"""
    # Retrieves value in np_number_ent entry widget
    number = int(np_number_ent.get())
    # Checks if number is greater than 1 and less than or equal to 5
    if number > 1 and number <= 5:
        # If conditions are met, sets np_number_ent value to number - 1
        np_number_ent.config(state="normal")
        np_number_ent.delete(0, tk.END)
        number -= 1
        np_number_ent.insert(0, number)
        np_number_ent.config(state="disabled")


def np_submit_function():
    """Number of Pizzas Function - submits information, moves onto Pizzas
    window"""
    # Makes number_pizzas a global variable so it can be accessed elsewhere
    global number_pizzas
    # Retrieves value in np_number_ent entry widget and assigns it to
    # number_pizzas variable
    number_pizzas = int(np_number_ent.get())
    # Destroys Number of Pizzas window
    number_pizzas_window.destroy()
    # Calls Pizzas window function
    pizzas_function()


def np_cancel_order_function():
    """Number of Pizzas Function - cancels order, goes back to order type
    page"""
    # Destroys Number of Pizzas window
    number_pizzas_window.destroy()
    # Calls Order Type window function
    order_type_function()


def number_pizzas_function():
    """Number of Pizzas Function - creates Number of Pizzas window"""
    # Creates window and defines window properties
    # Makes number_pizzas_window a global variable so it can be accessed
    global number_pizzas_window
    number_pizzas_window = tk.Tk()
    number_pizzas_window.title("Dream Pizzas - Number of Pizzas")
    number_pizzas_window.geometry("800x400")
    number_pizzas_window.minsize(800, 400)
    # Creates widgets and defines widget properties
    number_pizzas_lbl = tk.Label(master=number_pizzas_window,
                                 text="Number of Pizzas",
                                 font=("Zain", 32))
    np_how_many_lbl = tk.Label(master=number_pizzas_window,
                               text="How many pizzas?",
                               font=("Zain", 24))
    np_frm = tk.Frame(master=number_pizzas_window)
    np_decrease_btn = tk.Button(master=np_frm,
                                text="-",
                                font=("Zain"),
                                command=np_decrease_function,
                                width=2)
    # Makes np_number_ent a global variable so it can be accessed elsewhere
    global np_number_ent
    np_number_ent = tk.Entry(master=np_frm,
                             font=("Zain"),
                             width=4,
                             justify="center")
    # Sets np_number_ent to 1 and disables the entry widget - ensures that
    # the user can only input a number between 1 and 5 (or whatever is
    # specified in the np_decrease_function and np_increase_function if
    # changed at a later date to accomodate for more or less pizzas)
    np_number_ent.insert(0, 1)
    np_number_ent.config(state="disabled")
    np_increase_btn = tk.Button(master=np_frm,
                                text="+",
                                font=("Zain"),
                                command=np_increase_function,
                                width=2)
    np_submit_btn = tk.Button(master=number_pizzas_window,
                              text="Submit",
                              font=("Zain", 24),
                              command=np_submit_function)
    np_cancel_order_btn = tk.Button(master=number_pizzas_window,
                                    text="Cancel Order",
                                    font=("Zain", 12),
                                    command=np_cancel_order_function)
    # Packs widgets and defines widget placement
    number_pizzas_lbl.pack(anchor="n")
    np_how_many_lbl.pack(anchor="center", expand=True)
    np_frm.pack(anchor="center", expand=True)
    np_decrease_btn.pack(side="left", padx=5)
    np_number_ent.pack(side="left", padx=5)
    np_increase_btn.pack(side="left", padx=5)
    np_submit_btn.pack(anchor="center", expand=True)
    np_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    # Runs the window
    number_pizzas_window.mainloop()


# Pizzas Window Functions


def p_submit_function():
    """Pizzas Function - submits information, moves onto Summary window"""
    global chosen_pizzas
    chosen_pizzas = []
    for dropdown_choice in dropboxes:
        chosen_pizzas.append(dropdown_choice.get())
    global price_list
    price_list = []
    global total_price
    for pizza in chosen_pizzas:
        price_list.append(PIZZAS[pizza])
        total_price += PIZZAS[pizza]
    print(chosen_pizzas)
    print(price_list)
    print(total_price)
    pizzas_window.destroy()
    summary_function()


def p_cancel_order_function():
    """Pizzas Function - cancels order, goes back to order type page"""
    pizzas_window.destroy()
    order_type_function()


def pizzas_function():
    """Pizzas Function - displays pizza choices and adds choices to the
    order"""
    # Creates window and defines window properties
    # Makes pizzas_window a global variable so it can be accessed elsewhere
    global pizzas_window
    pizzas_window = tk.Tk()
    pizzas_window.title("Dream Pizzas - Pizzas")
    pizzas_window.geometry("1200x600")
    pizzas_window.minsize(1200, 600)
    # Creates pizzas_lbl widget, defines properties, and packs widget
    pizzas_lbl = tk.Label(master=pizzas_window,
                          text="Pizzas",
                          font=("Zain", 32))
    pizzas_lbl.pack(anchor="n")
    # Creates p_menu_count variable and sets to 0, allows for the menu to
    # have numbers next to each pizza name.
    p_menu_count = 0
    for pizza, price in PIZZAS.items():
        # Adds 1 to p_menu_count
        p_menu_count += 1
        # Creates p_menu_frm, p_menu_number_lbl, p_menu_pizza_lbl, and
        # p_menu_price_lbl widgets and defines properties
        p_menu_frm = tk.Frame(master=pizzas_window)
        p_menu_number_lbl = tk.Label(master=p_menu_frm,
                                     text=f"{p_menu_count}.",
                                     font=("Zain", 10))
        p_menu_pizza_lbl = tk.Label(master=p_menu_frm,
                                    text=f"{pizza}",
                                    font=("Zain", 10))
        p_menu_price_lbl = tk.Label(master=p_menu_frm,
                                    text=f"(${price})",
                                    font=("Zain", 10))
        # Packs widgets and defines widget placement
        p_menu_frm.pack(anchor="center", expand=True)
        p_menu_number_lbl.pack(side="left", padx=5)
        p_menu_pizza_lbl.pack(side="left", padx=5)
        p_menu_price_lbl.pack(side="left", padx=5)
    # Creates dropboxes list, makes it a global variable so it can be
    # accessed elsewhere
    global dropboxes
    dropboxes = []
    # Loops through to meet the number of pizzas the user wants to order
    # and create a dropdown for each pizza to be chosen.
    for number in range(1, number_pizzas + 1):
        # Creates dropdown_frm, dropdown_pizza_number_lbl, and dropdown_choice
        # widgets and defines properties
        dropdown_frm = tk.Frame(master=pizzas_window)
        dropdown_pizza_number_lbl = tk.Label(master=dropdown_frm,
                                             text=f"Pizza {number}:",
                                             font=("Zain", 18))
        dropdown_choice = ttk.Combobox(dropdown_frm,
                                       values=list(PIZZAS.keys()),
                                       state="readonly",
                                       width=35)
        dropdown_choice.set(list(PIZZAS.keys())[0])
        dropboxes.append(dropdown_choice)
        dropdown_frm.pack(anchor="center", expand=True)
        dropdown_pizza_number_lbl.pack(side="left", padx=5)
        dropdown_choice.pack(side="left", padx=5)
    p_submit_btn = tk.Button(master=pizzas_window,
                             text="Submit",
                             font=("Zain", 24),
                             command=p_submit_function)
    p_cancel_order_btn = tk.Button(master=pizzas_window,
                                   text="Cancel Order",
                                   font=("Zain", 12),
                                   command=p_cancel_order_function)
    p_submit_btn.pack(anchor="center", expand=True)
    p_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    pizzas_window.mainloop()

# Summary Window Functions


def s_cancel_order_function():
    """Summary Function - cancels order, goes back to Order Type window"""
    summary_window.destroy()
    order_type_function()


def s_confirm_order_function():
    """Summary Function - confirms order, restarts order by opening
    Order Type window"""
    global order
    order += 1
    saved_orders[f"order_{order}"] = [name,
                                      address,
                                      phone_number,
                                      chosen_pizzas,
                                      total_price]
    with open("saved_orders.txt", "a", encoding="utf-8") as output:
        for key, value in saved_orders.items():
            output.write(f"{key}: {value}\n")
    summary_window.destroy()
    order_type_function()


def summary_function():
    """Summary Function - creates Summary window"""
    # Creates window and defines window properties
    # Makes summary_window a global variable so it can be accessed elsewhere
    global summary_window
    summary_window = tk.Tk()
    summary_window.title("Dream Pizzas - Summary")
    summary_window.geometry("400x600")
    summary_window.minsize(800, 400)
    # Creates summary_lbl, s_name_lbl, s_name_data_lbl, and s_pizzas_lbl
    # and defines widget propoerties
    summary_lbl = tk.Label(master=summary_window,
                           text="Summary",
                           font=("Zain", 32))
    s_name_lbl = tk.Label(master=summary_window,
                          text="Name:",
                          font=("Zain", 24))
    s_name_data_lbl = tk.Label(master=summary_window,
                               text=f"{name}",
                               font=("Zain", 18))
    s_pizzas_lbl = tk.Label(master=summary_window,
                            text="Pizzas:",
                            font=("Zain", 24))
    # Packs summary_lbl, s_name_lbl, and s_name_data_lbl, s_pizzas_lbl
    # widgets and defines widget placement
    summary_lbl.pack(anchor="n")
    s_name_lbl.pack(anchor="center", expand=True)
    s_name_data_lbl.pack(anchor="center", expand=True)
    s_pizzas_lbl.pack(anchor="center", expand=True)
    for pizza in chosen_pizzas:
        # Loops through chosen_pizzas list and creates s_pizzas_frm,
        # s_pizzas_data_lbl, and s_pizza_price_data_lbl widgets for
        # each pizza in the list and defines widget properties
        s_pizzas_frm = tk.Frame(master=summary_window)
        s_pizzas_data_lbl = tk.Label(master=s_pizzas_frm,
                                     text=pizza,
                                     font=("Zain", 18))
        s_pizza_price_data_lbl = tk.Label(master=s_pizzas_frm,
                                          text=f"(${PIZZAS[pizza]})",
                                          font=("Zain", 18))
        # Packs s_pizzas_frm, s_pizzas_data_lbl, and s_pizza_price_data_lbl
        # widgets and defines widget placement
        s_pizzas_frm.pack(anchor="center", expand=True)
        s_pizzas_data_lbl.pack(side="left", padx=5)
        s_pizza_price_data_lbl.pack(side="left", padx=5)
    # Creates s_address_lbl, s_address_data_lbl, s_phone_lbl,
    # s_phone_data_lbl, s_total_lbl, s_total_data_lbl, s_btn_frm,
    # s_cancel_order_btn, s_confirm_order_btn, and s_sign_out_btn
    # widgets and defines properties
    s_address_lbl = tk.Label(master=summary_window,
                             text="Address:",
                             font=("Zain", 24))
    s_address_data_lbl = tk.Label(master=summary_window,
                                  text=address,
                                  font=("Zain", 18))
    s_phone_lbl = tk.Label(master=summary_window,
                           text="Phone Number:",
                           font=("Zain", 24))
    s_phone_data_lbl = tk.Label(master=summary_window,
                                text=phone_number,
                                font=("Zain", 18))
    s_total_lbl = tk.Label(master=summary_window,
                           text="Total Price:",
                           font=("Zain", 24))
    s_total_data_lbl = tk.Label(master=summary_window,
                                text=total_price,
                                font=("Zain", 18))
    s_btn_frm = tk.Frame(master=summary_window)
    # Assigns buttons to s_btn_frm
    s_cancel_order_btn = tk.Button(master=s_btn_frm,
                                   text="Cancel Order",
                                   font=("Zain", 12),
                                   command=s_cancel_order_function)
    s_confirm_order_btn = tk.Button(master=s_btn_frm,
                                    text="Confirm Order",
                                    font=("Zain", 12),
                                    command=s_confirm_order_function)
    s_sign_out_btn = tk.Button(master=s_btn_frm,
                               text="Sign Out",
                               font=("Zain", 12),
                               command=terminate_program_function)
    # Packs s_address_lbl, s_address_data_lbl, s_phone_lbl, s_phone_data_lbl,
    # s_total_lbl, s_total_data_lbl, s_btn_frm, s_cancel_order_btn,
    # s_confirm_order_btn, and s_sign_out_btn widgets and defines widget
    # placement
    s_address_lbl.pack(anchor="center", expand=True)
    s_address_data_lbl.pack(anchor="center", expand=True)
    s_phone_lbl.pack(anchor="center", expand=True)
    s_phone_data_lbl.pack(anchor="center", expand=True)
    s_total_lbl.pack(anchor="center", expand=True)
    s_total_data_lbl.pack(anchor="center", expand=True)
    s_btn_frm.pack(anchor="center", expand=True)
    s_cancel_order_btn.pack(side="left", padx=5)
    s_confirm_order_btn.pack(side="left", padx=5)
    s_sign_out_btn.pack(side="left", padx=5)
    # Runs the window
    summary_window.mainloop()


order_type_function()
