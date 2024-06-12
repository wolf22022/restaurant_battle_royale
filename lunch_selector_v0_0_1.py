import tkinter as tk
from random import randint

root = tk.Tk()
root.title("lets fucking go")

restaurant_options = []
restaurant_variables = []
current_row = 1

def add_line():
    
    global current_row

    restaurant_variables.append(tk.StringVar())
    
    restaurant_option = tk.Frame(root)

    option_label = tk.Label(restaurant_option, text="Culinary Competitor:")
    option_label.grid(row=0, column=0)

    option_entry = tk.Entry(restaurant_option, textvariable=restaurant_variables[-1])
    option_entry.grid(row=0, column=1)

    option_button = tk.Button(restaurant_option, text="Remove")
    option_button.grid(row=0, column=2)
    restaurant_options.append(restaurant_option)

    restaurant_options[-1].pack()
    current_row += 1
    
main_frame = tk.Frame(root)
add_entry = tk.Button(main_frame, text="Add Option", command=add_line)
add_entry.grid(row=0, column=0)

begin_battle = tk.Button(main_frame, text="Commence Selection")
begin_battle.grid(row=0, column=1)
main_frame.pack()
root.mainloop()
