import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import csv




def load_data():
    file_name = filedialog.askopenfilename(
        title="Ouvrir un fichier CSV",
        initialdir='C:\\Users\\Sa3d ka\\Documents',
        filetypes=[('CSV files', '*.csv')]
    )

    if file_name:
        with open(file_name, 'r', newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                nom, prenom, age, email = row
                tree_view.insert("", "end", values=(nom, prenom, age, email))
            messagebox.showinfo("Succes", "Ajouter avec succes")

def insert_info():
    nom = nom_input.get()
    prenom = prenom_input.get()
    age = age_input.get()
    email = email_input.get()

    if not nom or not prenom or not age or not email:
        messagebox.showerror("Erreur", "Les champs sont obligatoir")
    else:
        tree_view.insert("", "end", values=(nom, prenom, age, email))


root = tk.Tk()
root.title("CSV APP")

style = ttk.Style(root)



root.tk.call("source", r"C:\Users\Sa3d ka\Documents\Tkinter-Mini-Projects\Projects\Excel App\forest-light.tcl")
root.tk.call("source", r"C:\Users\Sa3d ka\Documents\Tkinter-Mini-Projects\Projects\Excel App\forest-dark.tcl")
style.theme_use("forest-dark")

try:
    icon_image = Image.open("Projects\Excel App\csvicon.png")
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(True, icon_photo)
except Exception as e:
    print(f"Error loading icon: {e}")



frame = ttk.Frame(root)
frame.pack() 

# Widgets Frame
widgets_frame = ttk.LabelFrame(frame, text="Insert row")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)  # Use grid inside the frame

# Nom
nom_input = ttk.Entry(widgets_frame)
nom_input.insert(0, "Nom")
nom_input.bind("<FocusIn>", lambda e: nom_input.delete(0, "end"))
nom_input.grid(row=0, column=0, sticky='ew', padx=5, pady=(0, 5))

# Prenom
prenom_input = ttk.Entry(widgets_frame)
prenom_input.insert(0, "Prenom")
prenom_input.bind("<FocusIn>", lambda e: prenom_input.delete(0, "end"))
prenom_input.grid(row=1, column=0, sticky='ew', padx=5, pady=(0, 5))

# Age
age_input = ttk.Spinbox(widgets_frame, from_=18, to=100)
age_input.insert(0, "Age")
age_input.bind("<FocusIn>", lambda e: age_input.delete(0, "end"))
age_input.grid(row=2, column=0, sticky='ew', padx=5, pady=(0, 5))

# Email
email_input = ttk.Entry(widgets_frame)
email_input.insert(0, "E-mail")
email_input.bind("<FocusIn>", lambda e: email_input.delete(0, "end"))
email_input.grid(row=3, column=0, sticky='ew', padx=5, pady=(0, 5))

# Insert Button
insert_button = ttk.Button(widgets_frame, text="Insert", command=insert_info)
insert_button.grid(row=4, column=0, sticky='ew', padx=5, pady=(0, 5))

# Line
separator = ttk.Separator(widgets_frame)
separator.grid(row=5, column=0, padx=10, pady=10, sticky='ew')

# Import button
import_button = ttk.Button(widgets_frame, text="Import", command=load_data)
import_button.grid(row=6, column=0, sticky='ew', padx=5, pady=(0, 5))

# ====================================================

# Table Frame + Scrollbar
tree_frame = ttk.Frame(frame)
tree_frame.grid(row=0, column=1, pady=10)
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

# Table
cols = ("Nom", "Prenom", "Age", "E-mail")
tree_view = ttk.Treeview(tree_frame, show='headings', columns=cols, height=13, yscrollcommand=tree_scroll.set)
tree_scroll.config(command=tree_view.yview)

# Define column headings
for col in cols:
    tree_view.heading(col, text=col)
    tree_view.column(col, width=100, anchor="center")

tree_view.pack()

# Run the application
root.mainloop() 