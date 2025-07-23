#Jeremy Durdel
#Chapter 18 Lab 1
#07/23/2025

import tkinter as tk

class FeetInchesConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Feet and Inches Converter")

        tk.Label(self.window, text="Feet:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.window, text="Inches:").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self.window, text="Inches:").grid(row=1, column=0, padx=5, pady=5)

        self.feet_entry = tk.Entry(self.window, width=5)
        self.inches_entry = tk.Entry(self.window, width=5)
        self.result_label = tk.Label(self.window, text="")

        self.feet_entry.grid(row=0, column=1)
        self.inches_entry.grid(row=0, column=3)
        self.result_label.grid(row=1, column=1, columnspan=3)

        tk.Button(self.window, text="Convert", command=self.convert).grid(row=2, column=0, pady=5)
        tk.Button(self.window, text="Exit", command=self.window.quit).grid(row=2, column=1, pady=5)

        self.window.mainloop()

    def convert(self):
        try:
            feet = int(self.feet_entry.get())
            inches = int(self.inches_entry.get())
            total_inches = feet * 12 + inches
            self.result_label.config(text=str(total_inches))
        except ValueError:
            self.result_label.config(text="Invalid input")

if __name__ == "__main__":
    FeetInchesConverter()