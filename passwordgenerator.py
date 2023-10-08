import tkinter as tk
import random
import string

def generate_password(length):
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    
    all_chars = lower_case + upper_case + digits + special_chars

    
    if length < 8:
        return "Password length should be at least 8 characters for security."

    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate():
    try:
        desired_length = int(entry_length.get())
        generated_password = generate_password(desired_length)
        result_label.config(text=f"Generated Password: {generated_password}")
    except ValueError:
        result_label.config(text="Please enter a valid number for password length.")


window = tk.Tk()
window.title("Password Generator")


label_length = tk.Label(window, text="Enter Password Length:")
label_length.pack()
entry_length = tk.Entry(window)
entry_length.pack()


generate_button = tk.Button(window, text="Generate Password", command=generate)
generate_button.pack()


result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()
