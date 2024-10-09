import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_label.config(text="Please enter a positive number.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        password_label.config(text=f"Generated Password: {password}")
    
    except ValueError:
        password_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

instruction_label = tk.Label(root, text="Enter the desired length of the password", font=("Arial", 12))
instruction_label.pack(pady=10)

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
password_label.pack(pady=10)

generate_another_button = tk.Button(root, text="Generate Another Password", command=generate_password, font=("Arial", 12))
generate_another_button.pack(pady=10)

root.mainloop()
