import tkinter as tk
from tkinter import ttk

def convert():
    miles = entry_int.get()
    km = miles*1.61
    km_output = f"{km} Km"
    output_string.set(km_output)


window = tk.Tk()
window.title("Converter")
window.geometry("300x150")

title_label = ttk.Label(window, text="Miles To Kilometres", font="Calibri 24 bold")
title_label.pack(pady=10)


input_frame = ttk.Frame(window)

entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable=entry_int)
button = ttk.Button(input_frame, text="Convert", command=convert)
entry.pack(side="left")
button.pack(side="left")
input_frame.pack()

output_string = tk.StringVar()
output_label = ttk.Label(window, text="56", font="Calibri 24", textvariable=output_string)
output_label.pack(pady=10)



window.mainloop()