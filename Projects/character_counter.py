import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def counter():
    # Get the text from the Text widget
    text_count = text.get("1.0", tk.END)

    # Count characters (including spaces and newlines)
    character_count = len(text_count)-1

    # Count words (split by whitespace and filter out empty strings)
    words = text_count.split()
    word_count = len(words)

    # Count paragraphs (split by double newlines)
    paragraphs = text_count.split("\n\n")
    paragraph_count = len(paragraphs)

    # Update the labels with the counts
    character_label1_str.set(character_count)
    words_label1_str.set(word_count)
    paragraphs_label1_str.set(paragraph_count)

# Create the main window
window = ttk.Window(themename="darkly")
window.title("Character Counter")
window.geometry("700x610")

# Title label
title_label = ttk.Label(window, text="Character Counter", font="Arial 30 bold")
title_label.pack()

# Frame for counters
frame = ttk.Frame(window)
frame.pack(pady=20)

# Labels for descriptions
character_label = ttk.Label(frame, text="Characters", font="Arial 10")
words_label = ttk.Label(frame, text="Words", font="Arial 10")
paragraphs_label = ttk.Label(frame, text="Paragraphs", font="Arial 10")

# StringVar to dynamically update the counts
character_label1_str = tk.StringVar()
words_label1_str = tk.StringVar()
paragraphs_label1_str = tk.StringVar()

# Labels to display the counts
character_label1 = ttk.Label(frame, text="0", font="Arial 15 bold", textvariable=character_label1_str)
words_label1 = ttk.Label(frame, text="0", font="Arial 15 bold", textvariable=words_label1_str)
paragraphs_label1 = ttk.Label(frame, text="0", font="Arial 15 bold", textvariable=paragraphs_label1_str)

# Grid layout for labels
character_label.grid(row=0, column=0, padx=50)
words_label.grid(row=0, column=1, padx=50)
paragraphs_label.grid(row=0, column=2, padx=50)

character_label1.grid(row=1, column=0, padx=50, pady=15)
words_label1.grid(row=1, column=1, padx=50, pady=15)
paragraphs_label1.grid(row=1, column=2, padx=50, pady=15)

# Frame for the Text widget and button
text_fram = ttk.Frame(window)
text = tk.Text(text_fram, width=80, height=25, wrap=tk.WORD)
text.pack()

button = ttk.Button(text_fram, text="Count", command=counter)
button.pack(pady=10)

text_fram.pack()

# Run the application
window.mainloop()