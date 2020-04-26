import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys

# TODO create ability for dialog file open,
#  check if data is list, series or other,
#  create defaults for each plotting function,


def file_open():
    """uses PyQT5 dialog for easy file open"""
    dialog = QFileDialog()
    file_name = dialog.getOpenFileName()[0]
    return file_name


def file_check(filename):
    """Check type of file for parsing"""
    file_ext = filename.split('.')[-1]
    if file_ext == 'xlsx':
        df1 = pd.read_excel(filename)
        return df1
    elif file_ext == "csv":
        df1 = pd.read_csv(filename)
        return df1
    # # try:
    #     with open(filename, 'r') as f:
    #         data = f.read()
    #         print(data)
    # except UnicodeDecodeError:
    #     raise Exception("FileError incorrect file format/type")


def generate_plot(object):
    pass


def save_plot(object, filename):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_name = file_open()
    data = file_check(file_name)
    print(data)
    sys.exit(app.exec_())