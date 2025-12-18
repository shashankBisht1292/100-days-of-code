import tkinter as tk

def convert():
    in_km = float(entry.get()) * 1.609
    calculated_value.config(text=f"{in_km}")

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry = tk.Entry(width=7)
entry.insert(0, "0")
entry.grid(row=0, column=1)

tk.Label(text="Miles").grid(row=0, column=2)

tk.Label(text="is equal to").grid(row=1, column=0)

calculated_value = tk.Label(text="0")
calculated_value.grid(row=1, column=1)

tk.Label(text="Km").grid(row=1, column=2)

tk.Button(text="Calculate", command=convert).grid(row=2, column=1)

tk.mainloop()