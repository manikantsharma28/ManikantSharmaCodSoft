import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == '+':
        result.set(num1 + num2)
    elif operation == '-':
        result.set(num1 - num2)
    elif operation == '*':
        result.set(num1 * num2)
    elif operation == '/':
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Error: Division by zero")


window = tk.Tk()
window.title("Simple Calculator")


label_num1 = tk.Label(window, text="Enter Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()


operations = ['+', '-', '*', '/']
operation_var = tk.StringVar()
operation_var.set('+')  
operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.pack()


calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()


window.mainloop()
