import tkinter
from tkinter import filedialog
import pathlib
def select_data():
    data_path = filedialog.askopenfilename()
    return data_path