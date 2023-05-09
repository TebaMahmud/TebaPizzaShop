from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

pizza = Tk()
pizza.geometry("1050x500")
pizza.title("Teba Pizza Shop")
pizza.config(bg='pink')

#Header
header_label = Label(pizza, text="Welcome to Teba's Pizza Shop", font=('Arial', 20))
header_label.grid(row=0, column=2)
pizza_emoji = ImageTk.PhotoImage(Image.open("pizza_emoji.png"))
pizza_lbl = Label(pizza, image=pizza_emoji)
pizza_lbl.grid(row=0, column=1)

#First Name
firstname_label = Label(pizza, text="First Name")
firstname_label.grid(row=1, column=0)
firstname_input = Entry(pizza, width=30)
firstname_input.grid(row=1, column=1)

#Last Name
lastname_label = Label(pizza, text="Last Name")
lastname_label.grid(row=2, column=0)
lastname_input = Entry(pizza, width=30)
lastname_input.grid(row=2, column=1)

#Phone Number
phone_label = Label(pizza, text="Phone Number")
phone_label.grid(row=3, column=0)
phone_input = Entry(pizza, width=30)
phone_input.grid(row=3, column=1)

#Menu
my_pizza_menu = ["Cheese", "Hawaii", "Italian", "Margerita"]

pizza_menu = Listbox(pizza, selectmode=MULTIPLE, bg='pink', fg='black')
pizza_menu.grid(row=4, column=1)

for item in my_pizza_menu:
    pizza_menu.insert(0, item)


def add_pizza():
    for item_to_add in pizza_menu.curselection():
        pizza_cart.insert(END, pizza_menu.get(item_to_add))

def check_out():
    pizza_checkout = Tk()
    pizza_checkout.geometry("600x400")
    pizza_checkout.title("Teba Pizza Shop | Checkout")

    #Checkout Info
    checkout_lbl = Label(pizza_checkout, text= "Order has been placed!" + "\n")
    checkout_lbl.grid(row=1, column=2)
    text1 = firstname_input.get() + " " + lastname_input.get()
    text2 = "Phone: " + phone_input.get()
    new_fullname_lbl = Label(pizza_checkout, text="Full Name: " + text1)
    new_fullname_lbl.grid(row=2, column=2)
    new_phone_lbl = Label(pizza_checkout, text="Phone: " + text2)
    new_phone_lbl.grid(row=3, column=2)
    pizza_checkout.mainloop()

def delete_pizza():
    pizza_cart.delete(pizza_cart.curselection())

def exit_app():
    answer = messagebox.askyesno("Pizza App Exit?", "Are you sure you want to exit?")
    if answer == 1:
        pizza.destroy()
    else:
        return

#Add Button
add_btn = Button(pizza, text="Add to Cart", command=add_pizza)
add_btn.grid(row=5, column=0)

#Checkout Button
checkout_btn = Button(pizza, text="Checkout", command=check_out)
checkout_btn.grid(row=5, column=1)

#Delete Button
delete_btn = Button(pizza, text="Remove from cart", command=delete_pizza)
delete_btn.grid(row=5, column=2)

#My Cart
pizza_cart = Listbox(pizza, bg='pink', fg='black')
pizza_cart.grid(row=4, column=2)

#Exit button
exit_btn = Button(pizza, text="Exit", command=exit_app)
exit_btn.grid(row=1, column=3)

pizza_pic = ImageTk.PhotoImage(Image.open("pizza.png"))
pizza_lbl = Label(pizza, image=pizza_pic)
pizza_lbl.grid(row=4, column=3)

pizza.mainloop()