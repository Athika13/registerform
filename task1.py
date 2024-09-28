
#print("hi")
import tkinter as tk
from tkinter import messagebox

# Function to handle the form submission
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    if name and email and age:
        # Display the entered data using a message box
        messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nAge: {age}")
    else:
        # Show a warning if any fields are empty
        messagebox.showwarning("Incomplete Data", "Please fill in all fields.")

# Create the main application window
root = tk.Tk()
root.title("Registration Form")

# Create a label and entry for the Name field
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for the Email field
label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Create a label and entry for the Age field
label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, pady=20)

# Start the Tkinter main loop
root.mainloop()

