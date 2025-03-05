import pandas as pd
from tkinter import filedialog, Tk
import os
import xlsxwriter


def select_files():
    # Crear una ventana oculta de Tkinter
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal
    root.attributes("-topmost", True)  # Forzar que la ventana esté en el frente
    data_paths = filedialog.askopenfilenames()
    root.destroy()  # Destruir la ventana inmediatamente después de seleccionar archivos
    return data_paths


def save_file():
    # Crear una ventana oculta de Tkinter
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal
    root.attributes("-topmost", True)  # Forzar que la ventana esté en el frente
    save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    root.destroy()  # Destruir la ventana inmediatamente después de seleccionar la carpeta de guardado
    return save_path


# Proceso principal
print("Hola\nSelecciona los archivos '.csv' y los transformaré en un Excel, cada archivo será una hoja separada")
files = select_files()

if files:
    game = True
    while game:
        print("Elige la carpeta en la que guardarás el archivo")
        save_path = save_file()

        if save_path:
            # Usar ExcelWriter para escribir en múltiples hojas
            with pd.ExcelWriter(save_path, engine='xlsxwriter') as writer:
                for file in files:
                    # Leer cada archivo CSV
                    data = pd.read_csv(file, encoding="latin-1")
                    # Obtener el nombre del archivo sin la ruta ni la extensión
                    sheet_name = os.path.splitext(os.path.basename(file))[0]
                    # Escribir en una hoja con el nombre del archivo
                    data.to_excel(writer, sheet_name=sheet_name, index=False)

            print(f"¡Tu archivo está listo!")
            print("Gracias por usar el programa!")
            game = False
        else:
                print("No se seleccionó una carpeta de destino o la acción se canceló")
else:
    print("No se seleccionaron archivos CSV.")
