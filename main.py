"""A program that allows a phone operator to input an order for a customer."""
import tkinter as tk
from tkinter import ttk
import os

# VARIABLES, LISTS, AND DICTIONARIES
# H1, H2, H3, and S1 variables - used to store the sizes and fonts.
H1 = ("Zain", 32)
H2 = ("Zain", 24)
H3 = ("Zain", 18)
S1 = ("Zain", 12)
# MAX_PIZZAS and MIN_PIZZAS variables - used to store the maximum and minimum
# number of pizzas that can be ordered.
MAX_PIZZAS = 5
MIN_PIZZAS = 1
# DELIVERY_FEE variable - used to store the delivery fee.
DELIVERY_FEE = 3
# saved_orders dictionary - provides a demo to allow the phone operator to
# understand how the data is being laid out/displayed.
saved_orders = {"order_demo": ["Name",
                               "Address",
                               "Phone",
                               ["Chosen pizza(s) list"],
                               "Total price"]}
# order variable - keeps track of the order number.
order = 0
# total_price variable - keeps track of the total price of the order.
total_price = 0
# Pizza prices - used to store the prices of the pizza types.
REGULAR_PRICE = 10.50
GOURMET_PRICE = REGULAR_PRICE + 5.00
# PIZZAS variable - dictionary that contains the pizza names and prices.
PIZZAS = {"Classic Margherita": REGULAR_PRICE,
          "Pepperoni Delight": REGULAR_PRICE,
          "Veggie Supreme": REGULAR_PRICE,
          "BBQ Chicken": REGULAR_PRICE,
          "Hawaiian Paradise": REGULAR_PRICE,
          "Four Cheese Extravaganza": REGULAR_PRICE,
          "Meat Lover’s Feast": REGULAR_PRICE,
          "Truffle Mushroom Bliss": GOURMET_PRICE,
          "Prosciutto & Arugula Delight": GOURMET_PRICE,
          "Fig & Goat Cheese Fantasy": GOURMET_PRICE,
          "Lobster & Lemon Zest": GOURMET_PRICE,
          "Pesto & Sun-Dried Tomato Medley": GOURMET_PRICE}
# BG variable - variable which stores the background colour.
BG = "#b3c7f7"
# FG variable - a variable which stores the foreground colour.
FG = "#1b1b1e"


# GENERAL FUNCTIONS


def terminate_program_function():
    """General Function - terminates program"""
    try:
        # Saves orders to saved_orders.txt file
        with open("saved_orders.txt", "a", encoding="utf-8") as output:
            output.write("\n")
            for key, value in saved_orders.items():
                output.write(f"{key}: {value}\n")
        # Opens saved_orders.txt file
        os.startfile("saved_orders.txt")
        exit()
    # Checks for a PermissionError
    except PermissionError:
        print("Error saving orders to file.")
        exit()


def error_message_function():
    """General Function - displays an error message"""
    error_window = tk.Tk()
    error_window.title("Dream Pizzas - Error")
    error_window.configure(bg=BG)
    error_window.geometry("250x100")
    error_window.minsize(250, 100)
    error_lbl = tk.Label(master=error_window,
                         text="Error: Please recheck inputs",
                         bg=BG,
                         fg=FG,
                         font=S1)
    error_ok_btn = tk.Button(master=error_window,
                             text="OK",
                             bg=BG,
                             fg=FG,
                             font=S1,
                             command=error_window.destroy)
    error_lbl.pack(anchor="center", expand=True)
    error_ok_btn.pack(anchor="center", expand=True)
    error_window.mainloop()

# ORDER TYPE FUNCTIONS


def ot_pu_function(order, order_type_window):
    """Order Type Function - submits information, moves onto Pickup window"""
    # Handles lack of delivery requirements.
    total_price = 0
    delivery_fee_applied = False
    address = "N/A"
    phone_number = "N/A"
    order_type_window.destroy()
    pick_up_function(order, total_price, delivery_fee_applied, address,
                     phone_number)


def ot_d_function(order, order_type_window):
    """Order Type Function - moves onto Delivery window"""
    # Handles the presence of a delivery fee.
    total_price = DELIVERY_FEE
    delivery_fee_applied = True
    order_type_window.destroy()
    delivery_function(order, total_price, delivery_fee_applied)


# ORDER TYPE WINDOW


def order_type_function(order):
    """Order Type Function - creates the Order Type window"""
    order_type_window = tk.Tk()
    order_type_window.title("Dream Pizzas - Order Type")
    order_type_window.configure(bg=BG)
    order_type_window.geometry("500x300")
    order_type_window.minsize(500, 300)
    order_type_lbl = tk.Label(master=order_type_window,
                              text="Order Type",
                              bg=BG,
                              fg=FG,
                              font=H1)
    ot_pickup_btn = tk.Button(master=order_type_window,
                              text="Pickup",
                              bg=BG,
                              fg=FG,
                              font=H2,
                              width=10,
                              command=lambda: ot_pu_function(
                                order,
                                order_type_window))
    ot_delivery_btn = tk.Button(master=order_type_window,
                                text="Delivery",
                                bg=BG,
                                fg=FG,
                                font=H2,
                                width=10,
                                command=lambda: ot_d_function(
                                    order,
                                    order_type_window))
    ot_exit_btn = tk.Button(master=order_type_window,
                            text="Exit",
                            bg=BG,
                            fg=FG,
                            font=S1,
                            command=terminate_program_function)
    order_type_lbl.pack(anchor="n")
    ot_pickup_btn.pack(anchor="center", expand=True)
    ot_delivery_btn.pack(anchor="center", expand=True)
    ot_exit_btn.pack(anchor="se", padx=10, pady=10)
    order_type_window.mainloop()


# PICK UP WINDOW FUNCTIONS


def pu_submit_function(order, pick_up_window, pu_name_ent, total_price,
                       delivery_fee_applied, address, phone_number):
    """Pick Up Function - submits information, moves onto Number of Pizzas
    window."""
    # Retrieves value in pu_name_ent entry widget.
    name_ent = (pu_name_ent.get()).strip(" ")
    # Checks for error handling.
    if len(name_ent) != 0 and name_ent.isnumeric() is False:
        name = name_ent
        pick_up_window.destroy()
        number_pizzas_function(order, name, total_price, delivery_fee_applied,
                               address, phone_number)
    else:
        # Calls error message function if bad input.
        error_message_function()


def pu_cancel_order_function(order, pick_up_window):
    """Pick Up Function - cancels order, goes back to order type page"""
    pick_up_window.destroy()
    order_type_function(order)


def pick_up_function(order, total_price, delivery_fee_applied, address,
                     phone_number):
    """Pick Up Function - creates Pick Up window"""
    pick_up_window = tk.Tk()
    pick_up_window.title("Dream Pizzas - Pick Up")
    pick_up_window.configure(bg=BG)
    pick_up_window.geometry("500x300")
    pick_up_window.minsize(500, 300)
    pick_up_lbl = tk.Label(master=pick_up_window,
                           text="Pick Up",
                           bg=BG,
                           fg=FG,
                           font=H1)
    pu_name_lbl = tk.Label(master=pick_up_window,
                           text="Name:",
                           bg=BG,
                           fg=FG,
                           font=H2)
    pu_name_ent = tk.Entry(master=pick_up_window,
                           fg=FG,
                           font=H3)
    pu_submit_btn = tk.Button(master=pick_up_window,
                              text="Submit",
                              bg=BG,
                              fg=FG,
                              font=H2,
                              command=lambda: pu_submit_function(
                                  order, pick_up_window, pu_name_ent,
                                  total_price, delivery_fee_applied,
                                  address, phone_number))
    pu_cancel_order_btn = tk.Button(master=pick_up_window,
                                    text="Cancel Order",
                                    bg=BG,
                                    fg=FG,
                                    font=S1,
                                    command=lambda: pu_cancel_order_function(
                                        order,
                                        pick_up_window))
    pick_up_lbl.pack(anchor="n")
    pu_name_lbl.pack(anchor="center", expand=True)
    pu_name_ent.pack(anchor="center", expand=True)
    pu_submit_btn.pack(anchor="center", expand=True)
    pu_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    pick_up_window.mainloop()

# Delivery Window Functions


def d_submit_function(order, delivery_window, d_name_ent, d_address_ent,
                      d_phone_ent, total_price, delivery_fee_applied):
    """Delivery Function - submits information, moves onto Number of Pizzas
    window"""
    # Retrieves values and strips any pre or post whitespace
    name_ent = (d_name_ent.get()).strip(" ")
    address_ent = (d_address_ent.get()).strip(" ")
    phone_ent = (d_phone_ent.get()).strip(" ")
    # Checks for error handling
    if (len(name_ent) != 0 and len(address_ent) != 0 and len(phone_ent) != 0
            and name_ent.isnumeric() is False and address_ent.isnumeric() is
            False and phone_ent.isnumeric() is True):
        # Sets values.
        name = name_ent
        address = address_ent
        phone_number = phone_ent
        delivery_window.destroy()
        number_pizzas_function(order, name, total_price, delivery_fee_applied,
                               address, phone_number)
    else:
        # Calls error message function if bad input.
        error_message_function()


def d_cancel_order_function(order, delivery_window):
    """Delivery Function - cancels order, goes back to order type page"""
    delivery_window.destroy()
    order_type_function(order)


def delivery_function(order, total_price, delivery_fee_applied):
    """Delivery Function - creates delivery window"""
    delivery_window = tk.Tk()
    delivery_window.title("Dream Pizzas - Delivery")
    delivery_window.configure(bg=BG)
    delivery_window.geometry("800x400")
    delivery_window.minsize(800, 400)
    delivery_lbl = tk.Label(master=delivery_window,
                            text="Delivery",
                            bg=BG,
                            fg=FG,
                            font=H1)
    d_disclaimer_lbl = tk.Label(master=delivery_window,
                                bg=BG,
                                fg=FG,
                                text=f"*${DELIVERY_FEE} delivery fee applies",
                                font=S1)
    d_name_frm = tk.Frame(master=delivery_window,
                          bg=BG)
    d_name_lbl = tk.Label(master=d_name_frm,
                          text="Name:",
                          bg=BG,
                          fg=FG,
                          font=H2)
    d_name_ent = tk.Entry(master=d_name_frm,
                          fg=FG,
                          font=H3)
    d_address_frm = tk.Frame(master=delivery_window,
                             bg=BG)
    d_address_lbl = tk.Label(master=d_address_frm,
                             bg=BG,
                             fg=FG,
                             text="Address:",
                             font=H2)
    d_address_ent = tk.Entry(master=d_address_frm,
                             fg=FG,
                             font=H3)
    d_phone_frm = tk.Frame(master=delivery_window,
                           bg=BG)
    d_phone_lbl = tk.Label(master=d_phone_frm,
                           bg=BG,
                           fg=FG,
                           text="Phone:",
                           font=H2)
    d_phone_ent = tk.Entry(master=d_phone_frm,
                           fg=FG,
                           font=H3)
    d_submit_btn = tk.Button(master=delivery_window,
                             text="Submit",
                             bg=BG,
                             fg=FG,
                             font=H2,
                             command=lambda: d_submit_function(
                                 order, delivery_window, d_name_ent,
                                 d_address_ent, d_phone_ent, total_price,
                                 delivery_fee_applied))
    d_cancel_order_btn = tk.Button(master=delivery_window,
                                   bg=BG,
                                   fg=FG,
                                   text="Cancel Order",
                                   font=S1,
                                   command=lambda: d_cancel_order_function(
                                       order,
                                       delivery_window))
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


def np_increase_function(np_number_ent):
    """Number of Pizzas Function - adds 1 to the quantity of pizzas wanted"""
    # Retrieves value
    number = int(np_number_ent.get())
    # Checks for error handling.
    if number < MAX_PIZZAS:
        # Sets np_number_ent value to number + 1
        np_number_ent.config(state="normal")
        np_number_ent.delete(0, tk.END)
        number += 1
        np_number_ent.insert(0, number)
        np_number_ent.config(state="disabled")


def np_decrease_function(np_number_ent):
    """Number of Pizzas Function - subtracts 1 from the quantity of pizzas
    wanted"""
    # Retrieves value
    number = int(np_number_ent.get())
    # Checks for error handling.
    if number > MIN_PIZZAS:
        # Sets np_number_ent value to number - 1
        np_number_ent.config(state="normal")
        np_number_ent.delete(0, tk.END)
        number -= 1
        np_number_ent.insert(0, number)
        np_number_ent.config(state="disabled")


def np_submit_function(order, number_pizzas_window, np_number_ent, name,
                       total_price, delivery_fee_applied, address,
                       phone_number):
    """Number of Pizzas Function - submits information, moves onto Pizzas
    window"""
    # Retrieves value
    number_pizzas = int(np_number_ent.get())
    number_pizzas_window.destroy()
    pizzas_function(order, number_pizzas, name, total_price,
                    delivery_fee_applied, address, phone_number)


def np_cancel_order_function(order, number_pizzas_window):
    """Number of Pizzas Function - cancels order, goes back to order type
    page"""
    number_pizzas_window.destroy()
    order_type_function(order)


def number_pizzas_function(order, name, total_price, delivery_fee_applied,
                           address, phone_number):
    """Number of Pizzas Function - creates Number of Pizzas window"""
    number_pizzas_window = tk.Tk()
    number_pizzas_window.title("Dream Pizzas - Number of Pizzas")
    number_pizzas_window.configure(bg=BG)
    number_pizzas_window.geometry("800x400")
    number_pizzas_window.minsize(800, 400)
    number_pizzas_lbl = tk.Label(master=number_pizzas_window,
                                 bg=BG,
                                 fg=FG,
                                 text="Number of Pizzas",
                                 font=H1)
    np_how_many_lbl = tk.Label(master=number_pizzas_window,
                               bg=BG,
                               fg=FG,
                               text="How many pizzas?",
                               font=H2)
    np_frm = tk.Frame(master=number_pizzas_window,
                      bg=BG)
    np_number_ent = tk.Entry(master=np_frm,
                             bg=BG,
                             fg=FG,
                             font=("Zain"),
                             width=4,
                             justify="center")
    np_decrease_btn = tk.Button(master=np_frm,
                                bg=BG,
                                fg=FG,
                                text="-",
                                font=("Zain"),
                                command=lambda: np_decrease_function(
                                    np_number_ent),
                                width=2)
    # Implements error handling.
    np_number_ent.insert(0, MIN_PIZZAS)
    np_number_ent.config(state="disabled")
    np_increase_btn = tk.Button(master=np_frm,
                                bg=BG,
                                fg=FG,
                                text="+",
                                font=("Zain"),
                                command=lambda: np_increase_function(
                                    np_number_ent),
                                width=2)
    np_submit_btn = tk.Button(master=number_pizzas_window,
                              bg=BG,
                              fg=FG,
                              text="Submit",
                              font=H2,
                              command=lambda: np_submit_function(
                                  order, number_pizzas_window, np_number_ent,
                                  name, total_price, delivery_fee_applied,
                                  address, phone_number))
    np_cancel_order_btn = tk.Button(master=number_pizzas_window,
                                    bg=BG,
                                    fg=FG,
                                    text="Cancel Order",
                                    font=S1,
                                    command=lambda: np_cancel_order_function(
                                        order,
                                        number_pizzas_window))
    number_pizzas_lbl.pack(anchor="n")
    np_how_many_lbl.pack(anchor="center", expand=True)
    np_frm.pack(anchor="center", expand=True)
    np_decrease_btn.pack(side="left", padx=5)
    np_number_ent.pack(side="left", padx=5)
    np_increase_btn.pack(side="left", padx=5)
    np_submit_btn.pack(anchor="center", expand=True)
    np_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    number_pizzas_window.mainloop()


# Pizzas Window Functions


def p_submit_function(order, pizzas_window, dropdowns_list, name, total_price,
                      delivery_fee_applied, address, phone_number):
    """Pizzas Function - submits information, moves onto Summary window"""
    chosen_pizzas = []
    # Iterates through dropdowns_list and appends the value to chosen_pizzas
    for dropdown_choice in dropdowns_list:
        chosen_pizzas.append(dropdown_choice.get())
    # Iterates through chosen_pizzas list and adds the price to total_price
    for pizza in chosen_pizzas:
        total_price += PIZZAS[pizza]
    pizzas_window.destroy()
    summary_function(order, chosen_pizzas, name, total_price,
                     delivery_fee_applied, address, phone_number)


def p_cancel_order_function(order, pizzas_window):
    """Pizzas Function - cancels order, goes back to order type page"""
    pizzas_window.destroy()
    order_type_function(order)


def pizzas_function(order, number_pizzas, name, total_price,
                    delivery_fee_applied, address, phone_number):
    """Pizzas Function - displays pizza choices and adds choices to the
    order"""
    pizzas_window = tk.Tk()
    pizzas_window.title("Dream Pizzas - Pizzas")
    pizzas_window.configure(bg=BG)
    pizzas_window.geometry("1200x600")
    pizzas_window.minsize(1200, 600)
    pizzas_lbl = tk.Label(master=pizzas_window,
                          bg=BG,
                          fg=FG,
                          text="Pizzas",
                          font=H1)
    pizzas_lbl.pack(anchor="n")
    # Creates p_menu_count variable and sets to 0, allows for the menu to
    # have numbers next to each pizza name.
    p_menu_count = 0
    for pizza, price in PIZZAS.items():
        # Creates menu for pizzas.
        p_menu_count += 1
        p_menu_frm = tk.Frame(master=pizzas_window,
                              bg=BG)
        p_menu_number_lbl = tk.Label(master=p_menu_frm,
                                     bg=BG,
                                     fg=FG,
                                     text=f"{p_menu_count}.",
                                     font=S1)
        p_menu_pizza_lbl = tk.Label(master=p_menu_frm,
                                    bg=BG,
                                    fg=FG,
                                    text=f"{pizza}",
                                    font=S1)
        p_menu_price_lbl = tk.Label(master=p_menu_frm,
                                    bg=BG,
                                    fg=FG,
                                    text=f"(${price})",
                                    font=S1)
        p_menu_frm.pack(anchor="center", expand=True)
        p_menu_number_lbl.pack(side="left", padx=5)
        p_menu_pizza_lbl.pack(side="left", padx=5)
        p_menu_price_lbl.pack(side="left", padx=5)
    dropdowns_list = []
    # Creates dropdowns as per number_pizzas.
    for number in range(1, number_pizzas + 1):
        dropdown_frm = tk.Frame(master=pizzas_window,
                                bg=BG)
        dropdown_pizza_number_lbl = tk.Label(master=dropdown_frm,
                                             text=f"Pizza {number}:",
                                             bg=BG,
                                             fg=FG,
                                             font=H3)
        dropdown_choice = ttk.Combobox(dropdown_frm,
                                       values=list(PIZZAS.keys()),
                                       state="readonly",
                                       width=35)
        # Implement error handling.
        dropdown_choice.set(list(PIZZAS.keys())[0])
        dropdowns_list.append(dropdown_choice)
        dropdown_frm.pack(anchor="center", expand=True)
        dropdown_pizza_number_lbl.pack(side="left", padx=5)
        dropdown_choice.pack(side="left", padx=5)
    p_submit_btn = tk.Button(master=pizzas_window,
                             bg=BG,
                             fg=FG,
                             text="Submit",
                             font=H2,
                             command=lambda:
                             p_submit_function(order, pizzas_window,
                                               dropdowns_list, name,
                                               total_price,
                                               delivery_fee_applied,
                                               address, phone_number))
    p_cancel_order_btn = tk.Button(master=pizzas_window,
                                   bg=BG,
                                   fg=FG,
                                   text="Cancel Order",
                                   font=S1,
                                   command=lambda: p_cancel_order_function(
                                       order,
                                       pizzas_window))
    p_submit_btn.pack(anchor="center", expand=True)
    p_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    pizzas_window.mainloop()

# Summary Window Functions


def s_cancel_order_function(order, summary_window):
    """Summary Function - cancels order, goes back to Order Type window"""
    summary_window.destroy()
    order_type_function(order)


def s_confirm_order_function(order, summary_window, chosen_pizzas, name,
                             total_price, address, phone_number):
    """Summary Function - confirms order, restarts order by opening
    Order Type window"""
    order += 1
    # Saves orders to saved_orders dictionary.
    saved_orders[f"order_{order}"] = [name,
                                      address,
                                      phone_number,
                                      chosen_pizzas,
                                      total_price]
    summary_window.destroy()
    order_type_function(order)


def summary_function(order, chosen_pizzas, name, total_price,
                     delivery_fee_applied,
                     address, phone_number):
    """Summary Function - creates Summary window"""
    summary_window = tk.Tk()
    summary_window.title("Dream Pizzas - Summary")
    summary_window.configure(bg=BG)
    summary_window.geometry("400x600")
    summary_window.minsize(800, 400)
    summary_lbl = tk.Label(master=summary_window,
                           bg=BG,
                           fg=FG,
                           text="Summary",
                           font=H1)
    s_name_lbl = tk.Label(master=summary_window,
                          bg=BG,
                          fg=FG,
                          text="Name:",
                          font=H2)
    s_name_data_lbl = tk.Label(master=summary_window,
                               bg=BG,
                               fg=FG,
                               text=f"{name}",
                               font=H3)
    s_pizzas_lbl = tk.Label(master=summary_window,
                            bg=BG,
                            fg=FG,
                            text="Pizzas:",
                            font=H2)
    summary_lbl.pack(anchor="n")
    s_name_lbl.pack(anchor="center", expand=True)
    s_name_data_lbl.pack(anchor="center", expand=True)
    s_pizzas_lbl.pack(anchor="center", expand=True)
    for pizza in chosen_pizzas:
        # Iterates to display the chosen pizzas and their prices.
        s_pizzas_frm = tk.Frame(master=summary_window,
                                bg=BG)
        s_pizzas_data_lbl = tk.Label(master=s_pizzas_frm,
                                     bg=BG,
                                     fg=FG,
                                     text=pizza,
                                     font=H3)
        s_pizza_price_data_lbl = tk.Label(master=s_pizzas_frm,
                                          bg=BG,
                                          fg=FG,
                                          text=f"(${PIZZAS[pizza]})",
                                          font=H3)
        s_pizzas_frm.pack(anchor="center", expand=True)
        s_pizzas_data_lbl.pack(side="left", padx=5)
        s_pizza_price_data_lbl.pack(side="left", padx=5)
    s_address_lbl = tk.Label(master=summary_window,
                             bg=BG,
                             fg=FG,
                             text="Address:",
                             font=H2)
    s_address_data_lbl = tk.Label(master=summary_window,
                                  bg=BG,
                                  fg=FG,
                                  text=address,
                                  font=H3)
    s_phone_lbl = tk.Label(master=summary_window,
                           bg=BG,
                           fg=FG,
                           text="Phone Number:",
                           font=H2)
    s_phone_data_lbl = tk.Label(master=summary_window,
                                bg=BG,
                                fg=FG,
                                text=phone_number,
                                font=H3)
    s_total_lbl = tk.Label(master=summary_window,
                           bg=BG,
                           fg=FG,
                           text="Total Price:",
                           font=H2)
    s_total_data_lbl = tk.Label(master=summary_window,
                                bg=BG,
                                fg=FG,
                                text=total_price,
                                font=H3)
    s_btn_frm = tk.Frame(master=summary_window,
                         bg=BG)
    # Displays if delivery fee is applied to total price.
    if delivery_fee_applied is True:
        s_total_data_lbl.config(text=f"{total_price} incl. $3 delivery fee")
    s_cancel_order_btn = tk.Button(master=s_btn_frm,
                                   bg=BG,
                                   fg=FG,
                                   text="Cancel Order",
                                   font=S1,
                                   command=lambda: s_cancel_order_function(
                                       order,
                                       summary_window))
    s_confirm_order_btn = tk.Button(master=s_btn_frm,
                                    bg=BG,
                                    fg=FG,
                                    text="Confirm Order",
                                    font=S1,
                                    command=lambda: s_confirm_order_function(
                                        order, summary_window, chosen_pizzas,
                                        name, total_price, address,
                                        phone_number))
    s_sign_out_btn = tk.Button(master=s_btn_frm,
                               bg=BG,
                               fg=FG,
                               text="Sign Out",
                               font=S1,
                               command=terminate_program_function)
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
    summary_window.mainloop()

# Runs program


order_type_function(order)
