import tkinter as tk
from tkinter import ttk
from app_db import AppDB

class MainDB:
    def __init_(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Product Management by Vitor Bryan")
        
        ### GUI Elements
        ## Labels and Entry Fields
        # Code
        self.lblCode = tk.Label(root, text="Code:")
        self.lblCode.grid(row=0, column=0, padx=5, pady=5)
        self.txtCode = tk.Entry(root)
        self.txtCode.grid(row=0, column=1, padx=5, pady=5)
        # Name
        self.lblName = tk.Label(root, text="Name:")
        self.lblName.grid(row=1, column=0, padx=5, pady=5)
        self.txtName = tk.Entry(root)
        self.txtName.grid(row=1, column=1, padx=5, pady=5)
        # Price
        self.lblPrice = tk.Label(root, text="Price:")
        self.lblPrice.grid(row=2, column=0, padx=5, pady=5)
        self.txtPrice = tk.Entry(root)
        self.txtPrice.grid(row=2, column=1, padx=5, pady=5)
        ## Buttons
        # Register
        self.btnRegister = tk.Button(root, text="Register", command=self.register_product)
        self.btnRegister.grid(row=3, column=0, padx=5, pady=5)
        # Update
        self.btnUpdate = tk.Button(root, text="Update", command=self.update_product)
        self.btnUpdate.grid(row=3, column=1, padx=5, pady=5)
        # Delete
        self.btnDelete = tk.Button(root, text="Delete", command=self.delete_product)
        self.btnDelete.grid(row=3, column=2, padx=5, pady=5)
        ## Treeview for displaying products
        self.tree = ttk.Treeview(root, columns=("Code", "Name", "Price"), show="headings")
        self.tree.heading("Code", text="Code") 
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)
        
        self.load_initial_data()
    
    def register_product(self):
        code = self.txtCode.get()
        name = self.txtName.get()
        price = self.txtPrice.get()
        if code and name and price:
            self.db.add_product(code, name, price)
            self.load_initial_data()
            self.clear_fields()