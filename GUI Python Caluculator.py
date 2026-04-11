import tkinter as tk

# Function to update the expression
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        if char == "=":
            btn = tk.Button(row_frame, text=char, font=("Arial", 18),
                            command=calculate)
        else:
            btn = tk.Button(row_frame, text=char, font=("Arial", 18),
                            command=lambda c=char: button_click(c))

        btn.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 18), command=clear)
clear_btn.pack(fill="both", padx=10, pady=10)

# Start the GUI
root.mainloop()