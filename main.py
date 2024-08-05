"""A program that will a phone operator to input an order for a customer."""
import tkinter as tk

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


def terminate_program_function():
    """General Function - terminates program"""
    with open("saved_orders.txt", "a") as output:
        for key, value in saved_orders.items():
            output.write(f"{key}: {value}\n")
    exit()

# Order Type Functions


def ot_pu_function():
    """Order Type Function - submits information, moves onto Pickup window"""
    global address
    address = "N/A"
    global phone_number
    phone_number = "N/A"
    order_type_window.destroy()
    pick_up_function()


def ot_d_function():
    """Order Type Function - moves onto Delivery window"""
    order_type_window.destroy()
    delivery_function()

# Order Type Window


def order_type_function():
    """Order Type Function - creates the Order Type window"""
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

# Pick Up Window Functions


def pu_submit_function():
    """Pick Up Function - submits information, moves onto Number of Pizzas
    window."""
    name_ent = pu_name_ent.get()
    name_check = name_ent.isspace()
    if len(name_ent) != 0 and name_check is False:
        global name
        name = pu_name_ent.get()
        pick_up_window.destroy()
        number_pizzas_function()


def pu_cancel_order_function():
    """Pick Up Function - cancels order, goes back to order type page"""
    pick_up_window.destroy()
    order_type_function()


def pick_up_function():
    """Pick Up Function - creates Pick Up window"""
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


def d_submit_function():
    """Delivery Function - submits information, moves onto Number of Pizzas
    window"""
    name_ent = d_name_ent.get()
    address_ent = d_address_ent.get()
    phone_ent = d_phone_ent.get()
    name_ent_check = name_ent.isspace()
    address_ent_check = address_ent.isspace()
    phone_ent_check = phone_ent.isspace()
    if (len(name_ent) != 0 and name_ent_check is False
            and len(address_ent) != 0 and address_ent_check is False
            and len(phone_ent) != 0 and phone_ent_check is False):
        global name
        name = d_name_ent.get()
        global address
        address = d_address_ent.get()
        global phone_number
        phone_number = d_phone_ent.get()
        delivery_window.destroy()
        number_pizzas_function()


def d_cancel_order_function():
    """Delivery Function - cancels order, goes back to order type page"""
    delivery_window.destroy()
    order_type_function()


def delivery_function():
    """Delivery Function - creates delivery window"""
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


def np_increase_function():
    """Number of Pizzas Function - adds 1 to the quantity of pizzas wanted"""
    number = int(np_number_ent.get())
    if number >= 1 and number < 5:
        np_number_ent.config(state="normal")
        np_number_ent.delete(0, tk.END)
        number += 1
        np_number_ent.insert(0, number)
        np_number_ent.config(state="disabled")


def np_decrease_function():
    """Number of Pizzas Function - subtracts 1 from the quantity of pizzas
    wanted"""
    number = int(np_number_ent.get())
    if number > 1 and number <= 5:
        np_number_ent.config(state="normal")
        np_number_ent.delete(0, tk.END)
        number -= 1
        np_number_ent.insert(0, number)
        np_number_ent.config(state="disabled")


def np_submit_function():
    """Number of Pizzas Function - submits information, moves onto Pizzas
    window"""
    global number_pizzas
    number_pizzas = int(np_number_ent.get())
    number_pizzas_window.destroy()
    pizzas_function()


def np_cancel_order_function():
    """Number of Pizzas Function - cancels order, goes back to order type
    page"""
    number_pizzas_window.destroy()
    order_type_function()


def number_pizzas_function():
    """Number of Pizzas Function - creates Number of Pizzas window"""
    global number_pizzas_window
    number_pizzas_window = tk.Tk()
    number_pizzas_window.title("Dream Pizzas - Number of Pizzas")
    number_pizzas_window.geometry("800x400")
    number_pizzas_window.minsize(800, 400)
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
    global np_number_ent
    np_number_ent = tk.Entry(master=np_frm,
                             font=("Zain"),
                             width=4,
                             justify="center")
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


def p_select_function():
    """Pizzas Function - selects pizza, adds to order"""
    dropdown.config(state="disabled")
    print(selected_option.get())


def p_submit_function():
    """Pizzas Function - submits information, moves onto Summary window"""
    pass


def p_cancel_order_function():
    """Pizzas Function - cancels order, goes back to order type page"""
    pizzas_window.destroy()
    order_type_function()


def pizzas_function():
    """Pizzas Function - displays pizza choices and adds choices to the
    order"""
    global pizzas_window
    pizzas_window = tk.Tk()
    pizzas_window.title("Dream Pizzas - Pizzas")
    pizzas_window.geometry("1200x600")
    pizzas_window.minsize(1200, 600)
    pizzas_lbl = tk.Label(master=pizzas_window,
                          text="Pizzas",
                          font=("Zain", 32))
    pizzas_lbl.pack(anchor="n")
    p_menu_count = 0
    for pizza, price in PIZZAS.items():
        p_menu_count += 1
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
        p_menu_frm.pack(anchor="center", expand=True)
        p_menu_number_lbl.pack(side="left", padx=5)
        p_menu_pizza_lbl.pack(side="left", padx=5)
        p_menu_price_lbl.pack(side="left", padx=5)
    global number
    global selected
    selected = True
    for number in range(1, number_pizzas + 1):
        dropdown_frm = tk.Frame(master=pizzas_window)
        dropdown_pizza_number_lbl = tk.Label(master=dropdown_frm,
                                             text=f"Pizza {number}:",
                                             font=("Zain", 18))
        global selected_option
        selected_option = tk.StringVar()
        selected_option.set(list(PIZZAS.keys())[0])
        global dropdown
        dropdown = tk.OptionMenu(dropdown_frm, selected_option, *PIZZAS.keys())
        p_select = tk.Button(master=dropdown_frm,
                             text="Select",
                             font=("Zain", 12))
        dropdown_frm.pack(anchor="center", expand=True)
        dropdown_pizza_number_lbl.pack(side="left", padx=5)
        dropdown.pack(side="left", padx=5)
        p_select.pack(side="left", padx=5)
    p_submit_btn = tk.Button(master=pizzas_window,
                             text="Submit",
                             font=("Zain", 18),
                             command=p_submit_function)
    p_cancel_order_btn = tk.Button(master=pizzas_window,
                                   text="Cancel Order",
                                   font=("Zain", 12),
                                   command=p_cancel_order_function)
    p_submit_btn.pack(anchor="center", expand=True)
    p_cancel_order_btn.pack(anchor="se", padx=10, pady=10)
    pizzas_window.mainloop()


order_type_function()
