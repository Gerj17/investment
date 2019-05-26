import tkinter as tk
from pathlib import Path

# ----- Window Content -------
root = tk.Tk()
root.geometry("400x160")
root.title("\tDestination")


#  ----- Miscellaneous------
# default_entry_text = tk.StringVar(root, Path.home())


#  ----- Widget Functions ------
def set_path():
    """
    grabs content currently in widget

    :param event:
    :return: content in widget
    """
    print("hello")
    path = entry_box.get()
    print(path)


#  ------  Create Widgets ------
label = tk.Label(text="Enter or choose the desired location of the CSV file. "
                      "If no location is given it will default to the 'document' folder", font='Times 11',
                 wraplength="400")
entry_box = tk.Entry(root, font='Helvetica 10 bold')
bt_done = tk.Button(root, text="Enter", font='Helvetica 12 bold', command=set_path)

#  ----- Bindings and Miscellaneous------
# entry_box.bind("<Return>", set_path)
entry_box.focus()

#  ------  Set Widgets ------
label.pack(anchor="center")
entry_box.pack(anchor="center", ipadx=100, ipady=5, pady=5, padx=5)
bt_done.pack(anchor="center", ipadx=20, ipady=10, pady=5, padx=5, )

root.mainloop()

