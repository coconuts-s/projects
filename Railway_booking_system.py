
from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk

master = Tk()
master.geometry("400x300+200+50")

class FontSizeAdjuster:
    def __init__(self, root, widgets):
        self.root = root
        self.widgets = widgets

        # Create a Scale widget to adjust font size
        self.scale = Scale(root, from_=8, to=25, orient=HORIZONTAL, label="Font Size", command=self.update_font_size)
        self.scale.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    def update_font_size(self, font_size):
        # Update the font size of all widgets in the list
        for widget in self.widgets:
            widget.config(font=("Arial", int(font_size)))

def home_window():

    def submit_ticket():

        from_var.set("Select an option")
        to_var.set("Select an option")
        name_input.delete(0, END)
        age_input.set(1)
        sleeper_var.set(0)
        passengers_check.delete(0, "end")  # Clear the current value
        passengers_check.insert(0, "1")     # Set the value to 0
        phone_input.delete(0, END)
        email_input.delete(0, END)
        address_input.delete("1.0", END)
        payment_var.set(0)
        messagebox.showinfo("Success", "Ticket submitted successfully")
        
    def payment_ticket():
        payment_choice = payment_var.get()
        passengers = passengers_check.get()
        sleeper_choice = sleeper_var.get()

        def calculate_amount(sleeper_choice, passengers):
            if (sleeper_choice == "sleeper"):
                price = 1000 * int(passengers)
            else:
                price = 500 * int(passengers)
            return price
        
        if (payment_choice == "cash"):
            cash_window = Toplevel(home)

            def calculate_change():
                total = float(amount_due.get())
                paid = float(amount_paid.get())
                change = paid - total
                if change < 0:
                    messagebox.showerror("Error", "Insufficient amount paid")
                else:
                    change_label.config(text=f"Change: ${change:.2f}")
            
            cash_window.title("Cash Payment")

            amount_due_label = Label(cash_window, text="Amount Due:")
            amount_due_label.pack()

            amount_due = Entry(cash_window)
            amount_due.insert(0, calculate_amount(sleeper_choice, passengers))
            # amount_due.config(state="disabled")
            amount_due.pack()

            amount_paid_label = Label(cash_window, text="Amount Paid:")
            amount_paid_label.pack()

            amount_paid = Entry(cash_window)
            amount_paid.insert(0, 0)
            amount_paid.pack()

            calculate_button = Button(cash_window, text="Calculate Change", command=calculate_change)
            calculate_button.pack()

            change_label = Label(cash_window, text="Change: $0.00")
            change_label.pack()

            image1 = Image.open("images/note100.jpeg")
            image1 = image1.resize((332, 152), Image.LANCZOS)
            note100_image = ImageTk.PhotoImage(image1)

            image2 = Image.open("images/note200.jpeg")
            image2 = image2.resize((332, 152), Image.LANCZOS)
            note200_image = ImageTk.PhotoImage(image2)


            def add_100():
                amount = float(amount_paid.get())
                amount += 100.00
                amount_paid.delete(0, END)
                amount_paid.insert(0, str(amount))

            def add_200():
                amount = float(amount_paid.get())
                amount += 200.00
                amount_paid.delete(0, END)
                amount_paid.insert(0, str(amount))

            coin_button = Button(cash_window, image=note100_image, command=add_100)
            coin_button.image = note100_image  # Keep a reference to the image
            coin_button.pack(side=LEFT)

            bill_button = Button(cash_window, image=note200_image, command=add_200)
            bill_button.image = note200_image  # Keep a reference to the image
            bill_button.pack(side=RIGHT)
        else:
            card_window = Toplevel(home)
            card_window.title("Card Payment")

            # Create a Canvas widget to simulate card movement
            canvas = Canvas(card_window, width=400, height=400, bg="white")
            canvas.pack()

            def on_drag(event):
                canvas.coords(card, event.x - 25, event.y - 25, event.x + 25, event.y + 25)

            def on_drop(event):
                total = calculate_amount(sleeper_choice, passengers)
                messagebox.showinfo("Card Payment", f"Amount paid: ₹{total}")

            card = canvas.create_rectangle(175, 175, 225, 225, fill="blue", tags="card")
            canvas.tag_bind("card", "<B1-Motion>", on_drag)
            canvas.tag_bind("card", "<ButtonRelease-1>", on_drop)

    home = Toplevel(master)
    home.geometry("700x600+500+100")
    home.title("Book tickets")

    home.grid_rowconfigure(0, weight=1)
    home.grid_rowconfigure(1, weight=1)
    home.grid_rowconfigure(2, weight=1)
    home.grid_rowconfigure(3, weight=1)
    home.grid_rowconfigure(4, weight=1)
    home.grid_rowconfigure(5, weight=1)
    home.grid_rowconfigure(6, weight=1)
    home.grid_rowconfigure(7, weight=1)
    home.grid_rowconfigure(8, weight=1)
    home.grid_rowconfigure(9, weight=1)
    home.grid_rowconfigure(10, weight=1)
    home.grid_rowconfigure(11, weight=1)
    home.grid_rowconfigure(12, weight=1)
    
    home.grid_columnconfigure(0, weight=1)
    home.grid_columnconfigure(1, weight=1)
    
    title_label = Label(home, text="Book tickets ", font=('Arial', 16))
    title_label.grid(row=0, column=0, columnspan=2)

    locations = ["Tambaram", "Chennai Egmore", "Chennai", "Vellore", "Arakkonam", 
                 "Coimbatore", "Chengalpattu", "Madurai", "Jolarpettai", "Salem", "Erode"]

    from_label = Label(home, text="From:")
    from_label.grid(row=1, column=0)
    from_var = StringVar(home)
    from_var.set("Select an option")
    from_menu = OptionMenu(home, from_var, *locations)
    from_menu.grid(row=1, column=1, sticky="N")

    to_label = Label(home, text="To:")
    to_label.grid(row=2, column=0)
    to_var = StringVar(home)
    to_var.set("Select an option")
    to_menu = OptionMenu(home, to_var, *locations)
    to_menu.grid(row=2, column=1, sticky="N")


    name_label = Label(home, text="Enter your name: ")
    name_label.grid(row=3, column=0)
    name_input = Entry(home)
    name_input.grid(row=3, column=1, sticky="N")

    age_label = Label(home, text="Scroll your age: ")
    age_label.grid(row=4, column=0)
    age_input = Scale(home, from_=1, to=100, orient=HORIZONTAL)
    age_input.grid(row=4, column=1, sticky="N")

    food_label = Label(home, text="Food: ")
    food_label.grid(row=5, column=0)

    food_frame = Frame(home)
    food_frame.grid(row=5, column=1, sticky="N")    
    biriyani_check = Checkbutton(food_frame, text="Biriyani")
    biriyani_check.pack(side=LEFT)
    parotta_check = Checkbutton(food_frame, text="Parotta")
    parotta_check.pack(side=LEFT)
    idli_check = Checkbutton(food_frame, text="Idli")
    idli_check.pack(side=LEFT)
    water_check = Checkbutton(food_frame, text="Water")
    water_check.pack(side=LEFT)

    sleeper_label = Label(home, text="Sleeper / Non-Sleeper ")
    sleeper_label.grid(row=6, column=0)

    sleeper_frame = Frame(home)
    sleeper_frame.grid(row=6, column=1, sticky="N")    
    sleeper_var = StringVar(home)
    sleeper_var.set("")
    sleeper_check = Radiobutton(sleeper_frame, text="Sleeper (₹1000 / person)", variable=sleeper_var, value="sleeper")
    sleeper_check.pack(side=LEFT)
    non_sleeper_check = Radiobutton(sleeper_frame, text="Non-Sleeper (₹500 / person)", variable=sleeper_var, value="non-sleeper")
    non_sleeper_check.pack(side=LEFT)
    
    passengers_label = Label(home, text="How many passengers are you travelling with? ")
    passengers_label.grid(row=7, column=0)
    passengers_check = Spinbox(home, from_= 1, to = 30) 
    passengers_check.grid(row=7, column=1, sticky="N")

    phone_label = Label(home, text="Enter your phone number: ")
    phone_label.grid(row=8, column=0)
    phone_input = Entry(home)
    phone_input.grid(row=8, column=1, sticky="N")
    
    email_label = Label(home, text="Enter your email: ")
    email_label.grid(row=9, column=0)
    email_input = Entry(home)
    email_input.grid(row=9, column=1, sticky="N")

    address_label = Label(home, text="Enter your address: ")
    address_label.grid(row=10, column=0)
    address_input = Text(home, height=6, width=53)
    address_input.grid(row=10, column=1, sticky="N")

    payment_label = Label(home, text="Payment Option: ")
    payment_label.grid(row=11, column=0)

    payment_frame = Frame(home)
    payment_frame.grid(row=11, column=1, sticky="N")    
    payment_var = StringVar(home)
    payment_var.set("")
    cash_payment_check = Radiobutton(payment_frame, text="Cash", variable=payment_var, value="cash")
    cash_payment_check.pack(side=LEFT)
    online_payment_check = Radiobutton(payment_frame, text="Online", variable=payment_var, value="online")
    online_payment_check.pack(side=LEFT)

    submit_button = Button(home, text='Submit', width=25, command=payment_ticket)
    submit_button.grid(row=12, column=0, columnspan=2)

    # List of widgets whose font size should be adjusted
    widgets_to_adjust = [
    title_label,
    from_label,
    to_label,
    name_label,
    age_label,
    food_label,
    sleeper_label,
    passengers_label,
    phone_label,
    email_label,
    address_label,
    submit_button,
    from_menu,
    to_menu,
    name_input,
    age_input,
    biriyani_check,
    parotta_check,
    idli_check,
    water_check,
    sleeper_check,
    non_sleeper_check,
    passengers_check,
    phone_input,
    email_input,
    address_input,
]
    font_size_adjuster = FontSizeAdjuster(home, widgets_to_adjust)


    
def check_login():        
    credentials = (("fire", "password1"), ("water", "password2"))
    userID = username_input.get()
    password = password_input.get()

    user = []
    user.append(userID)
    user.append(password)

    user = tuple(user)

    if user in credentials:
        status = "Successful"
        message = "You have successfully logged in to your account"
        home_window()
        master.destroy
    else:
        status = "Unsuccessful"
        message = "You have entered the wrong UserId and/or password"

    messagebox.showinfo(status, message)

    

master.config(bg="#e29c82")
master.title("Railway ticket booking")

label_color = "#000000"
font_style = ('Arial', 12, 'bold') 

title_label = Label(master, text="Railways booking", fg="green", bg="#e29c82", font=('Arial', 16))
title_label.place(x=150, y=25)

Label(master, text="Login", bg="#e29c82", fg=label_color, font=font_style).place(x=150, y=50)

username_label = Label(master, text='Username', bg="#e29c82", fg=label_color, font=font_style)
username_label.place(x=50, y=100)
username_input = Entry(master)
username_input.place(x=150, y=100)    

password_label = Label(master, text='Password', bg="#e29c82", fg=label_color, font=font_style)
password_label.place(x=50, y=130)
password_input = Entry(master, show="*")
password_input.place(x=150, y=130)

Button(master, text='Submit', width=25, command=check_login).place(x=150, y=200)
Button(master, text='Stop', width=25, command=master.destroy).place(x=150, y=230)

mainloop()
