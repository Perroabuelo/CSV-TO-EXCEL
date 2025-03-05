from tkinter import filedialog, Tk
import pandas
game = True
def select_file():
    window = Tk()
    window.withdraw()
    window.update()
    window.attributes("-topmost", True)
    data_path = filedialog.askopenfilename()
    window.destroy()
    return data_path

def save_file():
    window = Tk()
    window.withdraw()
    window.update()
    window.attributes("-topmost", True)
    data_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    window.destroy()
    return data_path


print("Hola\nSelecciona un archivo '.csv' y lo transformaré en un Excel")

file = select_file()
data = pandas.read_csv(file, encoding="latin-1")

while game:
    print("Elige la carpeta en la que guardaras el archivo")
    save_path = save_file()
    if save_path:
        data.to_excel(save_path, index=False)
        print(f"Tu archivo esta listo!!")
        print("Gracias por usar el programa!!")
        game = False
    else:
        print("No se seleccionó una carpeta de destino o la acción se canceló")