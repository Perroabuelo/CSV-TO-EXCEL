import tkinter as tk
g

class Window:
g
    def __init__(self):
        window = tk.Tk()
        window.minsize(width=500, height=500)
        window.title("Data Converter")
        window.resizable(False, False)
        self.buttons()
        self.labels()
        window.mainloop()
    def buttons(self):
        select_bt = tk.Button(text="Seleccionar archivo")
        select_bt.grid(column=0, row=0)
        convert_bt = tk.Button(text="Convertir")
        convert_bt.grid(column=2, row=0)

    def canvas(self):
        canvas = tk.Canvas()
        canvas.config(width=500, height=500)
        canvas.grid(column=1, row=0)

    def labels(self):
        tittle = tk.Label(text="CVS a EXCEL", font=("Arial", 20, "bold"))
        tittle.grid(column=1, row=0)
