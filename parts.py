import tkinter as tk
import os
from PIL import Image, ImageTk
WIDTH = 300
HEIGHT = 300

BACKGROUND = "#EEF9BF"

base_path = os.path.dirname(__file__)

csv_path = os.path.join(base_path, "./images/csv.png")
excel_path = os.path.join(base_path, "./images/excel.png")
next_path = os.path.join(base_path, "./images/next.png")

csv_image = Image.open(csv_path)
excel_image = Image.open(excel_path)
next_image = Image.open(next_path)

csv_resize = csv_image.resize((WIDTH, HEIGHT))
excel_resize = excel_image.resize((WIDTH, HEIGHT))
next_resize = next_image.resize((WIDTH, HEIGHT))

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Data Converter")
        self.window.config(background=BACKGROUND)
        self.window.resizable(False, False)
        self.csv_logo = ImageTk.PhotoImage(csv_resize)
        self.excel_logo = ImageTk.PhotoImage(excel_resize)
        self.next_logo = ImageTk.PhotoImage(next_resize)
        self.buttons()
        self.labels()
        self.inputs()

        self.window.mainloop()
    def buttons(self):
        select_bt = tk.Button(text="Seleccionar archivo", font=("Arial", 30, "bold"))
        select_bt.grid(column=0, row=2)
        convert_bt = tk.Button(text="Convertir", font=("Arial", 30, "bold"))
        convert_bt.grid(column=2, row=2)

    def labels(self):
        csv_logo = tk.Label(image=self.csv_logo, background=BACKGROUND)
        csv_logo.image = self.csv_logo
        next_logo = tk.Label(image=self.next_logo, background=BACKGROUND)
        next_logo.image = self.next_logo
        excel_logo = tk.Label(image=self.excel_logo, background=BACKGROUND)
        excel_logo.image = self.excel_logo
        csv_logo.grid(column=0, row=1)
        next_logo.grid(column=1, row=1)
        excel_logo.grid(column=2, row=1)

    def inputs(self):
        filename_xlsx = tk.Entry(font=("Arial", 30, "bold"))
        filename_xlsx.grid(column=1, row=2)