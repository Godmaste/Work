import tkinter as tk
import tkinter.ttk as ttk

def on_select(event=None):
    print('----------------------------')

    if event: # <-- this works only with bind because `command=` doesn't send event
        print("event.widget:", event.widget.get())

    for i, x in enumerate(all_comboboxes):
        print("all_comboboxes[%d]: %s" % (i, x.get()))

# --- main ---

root = tk.Tk()

all_comboboxes = []

cb = ttk.Combobox(root, values=("1", "2", "3", "4", "5"))
cb.set("1")
cb.pack()
cb.bind('<<ComboboxSelected>>', on_select)

all_comboboxes.append(cb)

cb = ttk.Combobox(root, values=("A", "B", "C", "D", "E"))
cb.set("A")
cb.pack()
cb.bind('<<ComboboxSelected>>', on_select)

all_comboboxes.append(cb)

b = tk.Button(root, text="Show all selections", command=on_select)
b.pack()

root.mainloop()
