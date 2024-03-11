# Import tkinter module
from tkinter import *

# Create a root window
root = Tk()
root.title("Currency Converter")
root.geometry("500x800")

# Create a label widget
Label(root,text="Currency Converter",font=("Courier",35)).pack(pady=20)

# Create the from dropdown
Label(root,text="From:",font=(None,25)).pack(pady=20,padx=75,anchor="w")
from_option = ["USD","EUR","GBP"]
from_dropdown = OptionMenu(root,*from_option)
from_dropdown.pack(padx=75,anchor="w")

# Create the to dropdown
Label(root,text="To:").pack(pady=20,padx=75,anchor="w")
to_option = ["USD","EUR","GBP"]
to_dropdown = OptionMenu(root,*to_option)
to_dropdown.pack(padx=75,anchor="w")

# Create the swap button
Button(root,text="Swap").pack(pady=10,padx=75,anchor="w")

# Create the amount entry
Entry(root).pack(padx=75,anchor="w",pady=20)

# Create the convert button
Button(root,text="Convert").pack(pady=30,padx=75,anchor="w")

# Create the result feild
Label(root,text="Result",borderwidth=7,font=("Currency",30),bg="#FFD733",width=14,height=3).pack(pady=20,padx=75,anchor="w")

# Setttings button
Button(root,text="Settings").pack(side=BOTTOM,pady=20,padx=20,anchor="se")

# Run the main loop
root.mainloop()