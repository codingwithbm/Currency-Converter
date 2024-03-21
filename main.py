# Import tkinter module
from tkinter import *
from tkinter import colorchooser

def settings():
    # Color Picker
    def pick_color():
        color = colorchooser.askcolor(title="Select Color")
        print(color)

    def save():
        pass


    # Create a settings window
    settings_window = Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x300")

    # Decimal places amount dropdown
    Label(settings_window,text="Decimal Places:",font=(None,15)).pack(padx=50,anchor="w")

    decimal_points = ["1","2","3","4","5"]
    decimal_var = StringVar()
    decimal_var.set("2")
    decimal_dropdown = OptionMenu(settings_window,decimal_var,*decimal_points)
    decimal_dropdown.pack(padx=50,pady=10,anchor="w")

    # Create the BG color picker
    Label(settings_window,text="Change Background Color:",font=(None,15)).pack(padx=50,anchor="w")

    bg_color = Button(settings_window,text="Pick Color",command=pick_color)
    bg_color.pack(padx=50,pady=10,anchor="w")

    # Offline mode
    Label(settings_window,text="Offline mode:",font=(None,15)).pack(padx=50,pady=10,anchor="w")
    offline_mode = Checkbutton(settings_window,text="Offline mode")
    offline_mode.pack(padx=50,anchor="w")

    # Save Changes
    Button(settings_window,text="Save",command=save).pack(pady=20,padx=50,anchor='w')


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
Button(root,text="Settings",command=settings).pack(side=BOTTOM,pady=20,padx=20,anchor="se")

# Run the main loop
root.mainloop()