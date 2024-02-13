# Import everything from the Tkinter module
from tkinter import *

# Initialize a variable to store the kilometers result
km = 0

# Define a function to calculate miles to kilometers
def calculate():
    # Get the value entered by the user, convert it to float, and calculate kilometers
    miles = float(entry.get())
    km = round(miles * 1.609)
    # Update the 'km_result' label with the calculated kilometers
    km_result.config(text=f"{km}", font=("Courier", 14))


# Create a Tkinter window
window = Tk()
window.title("Mile to Km Converter")  # Set the window title
window.minsize(200, 200)  # Set the minimum size of the window
window.config(padx=20, pady=20)  # Add padding around the widgets

# Create a label for the miles input
miles = Label(text="Miles", font=("Courier", 14))
miles.grid(column=3, row=0)  # Position the label in the grid

# Create a label that displays "is equal to"
is_equals = Label(text="is equal to", font=("Courier", 14))
is_equals.grid(column=0, row=1)  # Position the label in the grid

# Create a label to display the result in kilometers
km_result = Label(text=km, font=("Courier", 14))
km_result.grid(column=1, row=1)  # Position the label in the grid

# Create a label for the "Km" text
km_label = Label(text="Km", font=("Courier", 14))
km_label.grid(column=2, row=1)  # Position the label in the grid

# Create an entry widget for the user to input miles
entry = Entry(width=7)
entry.grid(column=1, row=0)  # Position the entry widget in the grid

# Create a button that triggers the 'calculate' function when clicked
new_button = Button(text="Calculate", command=calculate)
new_button.grid(column=1, row=2)  # Position the button in the grid

# Start the Tkinter event loop
window.mainloop()
