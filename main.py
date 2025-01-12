import tkinter as tk

# Initialize the global calculation variable
calculation = ""

# Function to add symbols to the calculation string
def add_to_calculate(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation
def evaluate_calculation():
    global calculation
    try:
        # Use eval to evaluate the calculation string
        result = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)  # Insert the result, not the original calculation
        calculation = result  # Update the global calculation to the result
    except Exception as e:
        clear_field()  # Clear the field in case of an error
        text_result.insert(1.0, "Error")

# Function to clear the calculation field
def clear_field():
    global calculation
    calculation = ""  # Clear the global calculation string
    text_result.delete(1.0, "end")  # Clear the text widget

# Initialize the main Tkinter window
root = tk.Tk()
root.geometry("379x250")

# Create the text widget to display results
text_result = tk.Text(root, height=2, width=16, font=("Arial", 25))
text_result.grid(columnspan=5)

# Create the number buttons
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculate(1), width=6, font=("Arial", 15))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculate(2), width=6, font=("Arial", 15))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculate(3), width=6, font=("Arial", 15))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculate(4), width=6, font=("Arial", 15))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculate(5), width=6, font=("Arial", 15))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculate(6), width=6, font=("Arial", 15))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculate(7), width=6, font=("Arial", 15))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculate(8), width=6, font=("Arial", 15))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculate(9), width=6, font=("Arial", 15))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculate(0), width=6, font=("Arial", 15))
btn_0.grid(row=5, column=2)

# Create buttons for operations
btn_add = tk.Button(root, text="+", command=lambda: add_to_calculate('+'), width=6, font=("Arial", 15))
btn_add.grid(row=2, column=4)

btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculate('-'), width=6, font=("Arial", 15))
btn_subtract.grid(row=3, column=4)

btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculate('*'), width=6, font=("Arial", 15))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculate('/'), width=6, font=("Arial", 15))
btn_divide.grid(row=5, column=4)

# Create the button to evaluate the calculation
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=6, font=("Arial", 15))
btn_equal.grid(row=5, column=3)

# Create the button to clear the field
btn_clear = tk.Button(root, text="C", command=clear_field, width=6, font=("Arial", 15))
btn_clear.grid(row=5, column=1)

root.mainloop()
