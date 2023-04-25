from tkinter import *

pizza = Tk()
pizza.geometry("600x500")
pizza.title("Teba Pizza Shop")
pizza.config(bg='pink')

#Header
header_label = Label(pizza, text="Welcome to Teba's Pizza Shop", font=('Arial', 20))
header_label.grid(row=0, column=1)

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

#Add Button
add_btn = Button(pizza, text="Add to Cart")
add_btn.grid(row=5, column=0)

#Checkout Button
checkout_btn = Button(pizza, text="Checkout")
checkout_btn.grid(row=5, column=1)

#Delete Button
delete_btn = Button(pizza, text="Delete from Cart")
delete_btn.grid(row=5, column=2)


pizza.mainloop()