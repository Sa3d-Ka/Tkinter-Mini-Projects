import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import openpyxl


def load_data():
    file_name = filedialog.askopenfilename(
        title="Ouvrir un fichier Excel",
        initialdir=r"C:\Users\Sa3d ka\Documents",
        filetypes=[("Excel Files CSV Files", "*.xlsx *.xls *.csv")]
    )

    if not file_name:  # Handle case where no file is selected
        return
    
    try:
        if file_name.endswith(".csv"):
            with open(file_name, 'r', newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                headings = next(reader)  # Get column headers
                
                # Set up columns and headings in Treeview
                tree_view["columns"] = headings
                for col_name in headings:
                    tree_view.heading(col_name, text=col_name)
                    tree_view.column(col_name, width=max(100, len(col_name) * 10), anchor="center")

                # Add rows to Treeview
                for row in reader:
                    tree_view.insert("", "end", values=row)
                messagebox.showinfo("Succès", "Ajouté avec succès")
        
        elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            workbook = openpyxl.load_workbook(file_name)
            sheet = workbook.active

            list_values = list(sheet.values)
            headings = list_values[0]
            
            # Set up columns and headings in Treeview
            tree_view["columns"] = headings
            for col_name in headings:
                tree_view.heading(col_name, text=col_name)
                tree_view.column(col_name, width=max(100, len(col_name) * 10), anchor="center")

            # Add rows to Treeview
            for value_tuple in list_values[1:]:
                tree_view.insert('', tk.END, values=value_tuple)
            messagebox.showinfo("Succès", "Ajouté avec succès")
        
        else:
            messagebox.showerror("Erreur", "Type de fichier non pris en charge")
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

def insert_info():
    nom = nom_input.get()
    prenom = prenom_input.get()
    age = age_input.get()
    email = email_input.get()

    if not nom or not prenom or not age or not email:
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
    else:
        cols = ("Nom", "Prenom", "Age", "E-mail")
        for col_name in cols:
                    tree_view.heading(col_name, text=col_name)
                    tree_view.column(col_name, width=max(100, len(col_name) * 10), anchor="center")
        tree_view.insert("", "end", values=(nom, prenom, age, email))

    # Clear the values
    nom_input.delete(0, "end")
    nom_input.insert(0, "Nom")
    prenom_input.delete(0, "end")
    prenom_input.insert(0, "Prenom")
    age_input.delete(0, "end")
    age_input.insert(0, "Age")
    email_input.delete(0, "end")
    email_input.insert(0, "E-mail")

def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")


root = tk.Tk()
root.title("EXCEL | CSV APP")

style = ttk.Style(root)

# Load theme files
root.tk.call("source", r"C:\Users\Sa3d ka\Documents\Tkinter-Mini-Projects\Projects\Excel App\forest-light.tcl")
root.tk.call("source", r"C:\Users\Sa3d ka\Documents\Tkinter-Mini-Projects\Projects\Excel App\forest-dark.tcl")
style.theme_use("forest-dark")

try:
    icon_image = Image.open("Projects\Excel App\csvicon.png")
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(True, icon_photo)
except Exception as e:
    print(f"Error loading icon: {e}")

# Frame Layout
frame = ttk.Frame(root)
frame.pack() 

# Widgets Frame
widgets_frame = ttk.LabelFrame(frame, text="Insert row")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

# Input Widgets
nom_input = ttk.Entry(widgets_frame)
nom_input.insert(0, "Nom")
nom_input.bind("<FocusIn>", lambda e: nom_input.delete(0, "end"))
nom_input.grid(row=0, column=0, sticky='ew', padx=5, pady=(0, 5))

prenom_input = ttk.Entry(widgets_frame)
prenom_input.insert(0, "Prenom")
prenom_input.bind("<FocusIn>", lambda e: prenom_input.delete(0, "end"))
prenom_input.grid(row=1, column=0, sticky='ew', padx=5, pady=(0, 5))

age_input = ttk.Spinbox(widgets_frame, from_=18, to=100)
age_input.insert(0, "Age")
age_input.bind("<FocusIn>", lambda e: age_input.delete(0, "end"))
age_input.grid(row=2, column=0, sticky='ew', padx=5, pady=(0, 5))

email_input = ttk.Entry(widgets_frame)
email_input.insert(0, "E-mail")
email_input.bind("<FocusIn>", lambda e: email_input.delete(0, "end"))
email_input.grid(row=3, column=0, sticky='ew', padx=5, pady=(0, 5))

# Insert Button
insert_button = ttk.Button(widgets_frame, text="Insert", command=insert_info)
insert_button.grid(row=4, column=0, sticky='ew', padx=5, pady=(0, 5))

# Import button
import_button = ttk.Button(widgets_frame, text="Import", command=load_data)
import_button.grid(row=6, column=0, sticky='ew', padx=5, pady=(0, 5))

# Line
separator = ttk.Separator(widgets_frame)
separator.grid(row=7, column=0, padx=10, pady=10, sticky='ew')

# Mode switch
mode_switch = ttk.Checkbutton(
    widgets_frame, text="Mode", style="Switch", command=toggle_mode)
mode_switch.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

# ====================================================

# Treeview Frame + Scrollbar
tree_frame = ttk.Frame(frame)
tree_frame.grid(row=0, column=1, pady=10)
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

# Treeview Table
cols = ("Nom", "Prenom", "Age", "E-mail")
tree_view = ttk.Treeview(tree_frame, show='headings', columns=cols, height=13, yscrollcommand=tree_scroll.set)
tree_scroll.config(command=tree_view.yview)

tree_view.pack()

# Run the app
root.mainloop()
