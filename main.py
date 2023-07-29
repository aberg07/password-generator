import random
import string
import tkinter as tk

num_chars = "0123456789"
symbol_chars = "!#@$%^&*,./<>?][;"
def pword_gen(length, symbols, numbers):
    pword = ""
    try:
        length = int(length)
        if int(length) < 5:
            length_error_window = tk.Tk()
            length_error_window.title("Error")
            length_error_label = tk.Label(length_error_window, text="Passwords should be at least 5 characters long.")
            length_error_label.grid(row=0, column=0)
        else:
            length = int(length)
            has_symbol = False
            has_number = False
            if symbols and numbers:
                while not (has_symbol and has_number):
                    pword = ""
                    has_symbol = False
                    has_number = False
                    for i in range(0, length):
                        pword += random.choice(string.ascii_letters + symbol_chars + num_chars)
                    for char in pword:
                        if not char.isalnum():
                            has_symbol = True
                            break
                    for char in pword:
                        if char.isdigit():
                            has_number = True
                            break
            elif symbols and not numbers:
                while not has_symbol:
                    pword = ""
                    has_symbol = False
                    for i in range(0, length):
                        pword += random.choice(string.ascii_letters + symbol_chars)
                    for i in range(0, len(pword)):
                        if pword[i] in symbol_chars:
                            has_symbol = True
                            break
            elif numbers and not symbols:
                while not has_number:
                    pword = ""
                    has_number = False
                    for i in range(0, length):
                        pword += random.choice(string.ascii_letters + num_chars)
                    for i in range(0, len(pword)):
                        if pword[i] in num_chars:
                            has_number = True
                            break
            else:
                for i in range(0, length):
                    pword += random.choice(string.ascii_letters)
            pword_field["text"] = pword
    except ValueError:
        error_window = tk.Tk()
        error_window.title("Error")
        error_label = tk.Label(error_window, text="Invalid entry. Please type an integer that is 5 or greater.")
        error_label.grid(row=0, column=0)

window = tk.Tk()
window.title("Password Generator")
has_symbol = tk.BooleanVar()
has_number = tk.BooleanVar()
len_label = tk.Label(window, text="Password length")
len_entry = tk.Entry(window, width=10)
len_entry.insert(0,"8")
has_symbol_label = tk.Label(window, text="Has symbols?")
y_has_symbol = tk.Radiobutton(window, text="Yes", variable=has_symbol, value=True)
n_has_symbol = tk.Radiobutton(window, text="No", variable=has_symbol, value=False)
has_number_label = tk.Label(window, text="Has numbers?")
y_has_number = tk.Radiobutton(window, text="Yes", variable=has_number, value=True)
n_has_number = tk.Radiobutton(window, text="No", variable=has_number, value=False)
gen_pword_button = tk.Button(window, text="Generate Password", command=lambda:pword_gen(len_entry.get(), has_symbol.get(), has_number.get()))
pword_label = tk.Label(window, text="Password")
pword_field = tk.Label(window)
len_label.grid(row=0, column=0)
len_entry.grid(row=0, column=1)
has_symbol_label.grid(row=1, column=0)
y_has_symbol.grid(row=1, column=1, pady=10)
n_has_symbol.grid(row=1, column=2, pady=10)
has_number_label.grid(row=2, column=0)
y_has_number.grid(row=2, column=1, pady=10)
n_has_number.grid(row=2, column=2, pady=10)
gen_pword_button.grid(row=3, column=1)
pword_label.grid(row=4, column=0, pady=20)
pword_field.grid(row=4, column=1)
window.mainloop()