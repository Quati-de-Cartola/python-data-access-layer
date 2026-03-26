import tkinter as tk
from tkinter import ttk
from app_db import AppDB

class MainDB:
    def __init_(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Product Management by Vitor Bryan")
        
        # GUI Elements
        
        
        self.create_widgets()
        self.load_data()