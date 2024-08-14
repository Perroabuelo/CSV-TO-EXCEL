import tkinter as tk
import os
base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "./images/csv.png")
excel_path = os.path.join(base_path, "./images/excel.png")
next_path = os.path.join(base_path, "./images/next.png")

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Data Converter")
        self.window.resizable(False, False)
        self.csv_logo = tk.PhotoImage(file=csv_path)
        self.excel_logo = tk.PhotoImage(file=excel_path)
        self.next_logo = tk.PhotoImage(file=next_path)
        self.buttons()
        self.labels()
        self.canvas()

        self.window.mainloop()
    def buttons(self):
        select_bt = tk.Button(text="Seleccionar archivo")
        select_bt.grid(column=0, row=2)
        convert_bt = tk.Button(text="Convertir")
        convert_bt.grid(column=2, row=2)

    def canvas(self):
        canvas = tk.Canvas()
        canvas.config(width=600, height=600, highlightthickness=False)
        # canvas.create_image(300, 300, image=self.csv_logo)
        # canvas.create_image(300, 300, image=self.excel_logo)
        # canvas.create_image(300, 300, image=self.csv_logo)
        canvas.grid(column=1, row=1)

    def labels(self):
        tittle = tk.Label(text="CVS a EXCEL", font=("Arial", 20, "bold"))
        tittle.grid(column=1, row=0)
        csv_logo = tk.Label(image=self.csv_logo)
        csv_logo.grid(column=0, row=1)