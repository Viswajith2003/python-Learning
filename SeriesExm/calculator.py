import tkinter as tk
from tkinter import messagebox

# Click handler for button events
def click(event):
    current = display.get()
    text = event.widget.cget("text")
    try:
        if text == "=":
            result = eval(current)  # Evaluate the expression
            display.delete(0, tk.END)  # Clear the display
            display.insert(tk.END, result)  # Show the result
        elif text == "C":
            display.delete(0, tk.END)  # Clear display
        else:
            display.insert(tk.END, text)  # Add text to the display
    except Exception as e:
        messagebox.showinfo("ERROR", str(e))
        display.delete(0, tk.END)  # Clear display if there's an error

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("320x450")

# Create the display
display = tk.Entry(window, font=("Arial", 25), justify="right")
display.pack(fill=tk.X, padx=10, pady=10, ipady=10)  # Pad inner space for better looks

# Create the frame for buttons
btn_frame = tk.Frame(window)
btn_frame.pack()

# Button labels for the calculator
btn_labels = [
    ["7", "8", "9", "C"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "-"],
    ["*", "0", "/", "."],
    ["="]  # Special row for equal sign
]

# Add buttons to the frame
for i in range(4):  # Loop through the first four rows
    for j in range(4):  # Each row contains four buttons
        button = tk.Button(
            btn_frame, font=("Arial", 16), padx=15, pady=10, text=btn_labels[i][j]
        )
        button.grid(row=i, column=j, padx=10, pady=10)  # Place the button in the grid
        button.bind("<Button-1>", click)  # Bind the click event

# Add the "=" button with a larger size
equal_button = tk.Button(
    btn_frame, font=("Arial", 16), padx=100, pady=10, text=btn_labels[4][0]
)
equal_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10)  # Span across 4 columns
equal_button.bind("<Button-1>", click)  # Bind the click event

# Start the main event loop
window.mainloop()
