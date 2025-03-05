import pandas
from tkinter import filedialog, Tk

window = Tk()
data_path = filedialog.askopenfilename()
data_save = filedialog.asksaveasfilename(defaultextension=".xlsx")
file = pandas.read_csv(data_path, encoding="latin-1", keep_default_na=False, sep=",")
print(file)
