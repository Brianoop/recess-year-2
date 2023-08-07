# Author: Angoda Brian Nyanga
# Date: 2023-07-01
# Description: A receipt printing program with a GUI Interface
# Session: Morning
# Github: https://github.com/techymaj/recess-2.git
# Assignment: 5

# Using ttkbootstrap as ttk
# install ttkbootstrap using <pip install ttkbootstrap> or <pip3 install ttkbootstrap>

# import ttk bootstrap
import os
from tkinter import messagebox
import ttkbootstrap as ttk
import ttkbootstrap.tableview as tv
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.validation import add_regex_validation


class ReceiptBook(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.item = ttk.StringVar(value="")
        self.description = ttk.StringVar(value="")
        self.price = ttk.DoubleVar(value=0.0)
        self.quantity = ttk.IntVar(value=0)
        self.total = ttk.DoubleVar(value=0.0)
        self.receipt = []
        instructions = "Enter the item, description, price, and quantity:"
        instruction = ttk.Label(self, text=instructions)
        instruction.pack(fill=X, pady=10)
        # create the form
        self.create_inputs("Item: ", self.item)
        self.create_inputs("Description: ", self.description)
        self.create_inputs("Price: ", self.price)
        self.create_inputs("Quantity: ", self.quantity)

        self.create_buttons()
        self.table = self.create_table()


    # create text/numerical inputs
    def create_inputs(self, label, variable):
        # create a container
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X, expand=YES, pady=5)
        # create a label
        form_field_label = ttk.Label(master=form_field_container, text=label, width=15)
        form_field_label.pack(side=LEFT, padx=12)
        # create an entry
        form_input = ttk.Entry(master= form_field_container, textvariable=variable)
        form_input.pack(side=LEFT, fill=X, padx=5, expand=YES)
        # add validation. Only allow alphanumeric characters
        add_regex_validation(form_input, r"^[a-zA-Z0-9_ ]*$")
        return form_input
    

    # create buttons
    def create_buttons(self):
        # create a button
        button_container = ttk.Frame(self)
        button_container.pack(fill=X, expand=YES, pady=(15, 10))
        
        clear_button = ttk.Button(
            button_container, 
            text="Clear", 
            command=self.clear,
            bootstyle = DANGER,
            width=6
        )
        clear_button.pack(side=RIGHT, padx=5)

        create_receipt_button = ttk.Button(
            button_container, 
            text="Create Receipt", 
            command=self.on_create_receipt,
            bootstyle = SUCCESS,
            width=16
        )
        create_receipt_button.pack(side=RIGHT, padx=5)
    

    def clear(self):
        self.item.set("")
        self.description.set("")
        self.price.set(0.0)
        self.quantity.set(0)
        self.total.set(0.0)
        self.receipt = []
    

    def on_create_receipt(self):
        # check if the inputs are empty
        if self.item.get() == "" or self.description.get() == "" or self.price.get() == 0.0 or self.quantity.get() == 0:
            ToastNotification(
                title="Error",
                message="Please fill all the fields",
                duration=3000,
                bootstyle=DANGER,
                alert=True,
            ).show_toast()
            return
        self.create_receipt()
    

    def create_receipt(self):
        item = self.item.get()
        description = self.description.get()
        price = self.price.get()
        quantity = self.quantity.get()
        total = price * quantity
        self.total.set(total)
        receipt = f"""
        Item: {item}
        Description: {description}
        Price: {price}
        Quantity: {quantity}
        Total: {total}
        """
        # show the receipt
        messagebox.showinfo("Receipt", receipt)

        toast = ToastNotification(
            title="Success",
            message="Receipt created successfully",
            duration=3000,
            bootstyle=SUCCESS
        )
        toast.show_toast()
        self.receipt.append((item, description, price, quantity, total))
        self.table.destroy()
        self.table = self.create_table()
    

    def create_table(self):
        coldata = [
            {"text": "Item", "width": 100},
            {"text": "Description", "width": 200},
            {"text": "Price", "width": 100, "stretch": False},
            {"text": "Quantity", "width": 100, "stretch": False},
            {"text": "Total", "width": 100, "stretch": False},
        ]

        table = tv.Tableview(
            master = self,
            coldata=coldata,
            rowdata=self.receipt,
            paginated=True,
            searchable=True,
            bootstyle=INFO,
            stripecolor=("#808080", "white")
        )  

        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        return table


if __name__ == "__main__":
    app = ttk.Window("Angoda Brian Nyanga's Receipt Book", "darkly")
    ReceiptBook(app)
    app.mainloop()