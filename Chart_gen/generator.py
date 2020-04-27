import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys

# TODO further add functions for data clean and series selection
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
    elif file_ext == 'html':
        df1 = pd.read_html(filename)
        return df1
    else:
        df1 = pd.read_html(filename)
        return df1


def fix_header(dataframe):
    """Function for data cleaning, allows for manual specification of the header row and replaces, returning
    resultant dataframe"""
    loop = True
    while loop:
        fix = input('Change Header Row? Type Y/N').upper()
        if fix == "Y":
            loop2 = True
            while loop2:
                if loop2:
                    print(dataframe.to_string())
                    header_row = int(input("Specify Header Row (from 0)"))
                    headers = dataframe.iloc[header_row]
                    new_df = dataframe[header_row:]
                    new_df.columns = headers
                    print(new_df.to_string())
                    correct = input("Is this correct? 'Y/N'").upper()
                    if correct == "Y":
                        loop2 = False
                        return new_df
                    elif correct == "N":
                        continue
                    else:
                        print("Incorrect specification, try again.")
            loop = False
        elif fix == "N":
            loop = False
            return dataframe
        else:
            print("Incorrect entry, enter 'Y' or 'N'.")
            continue


def fix_index(dataframe):
    """Function for data cleaning, allows for manual specification of the index column and replaces, returning
    resultant dataframe"""
    loop = True
    while loop:
        fix = input('Change Index Column? Type Y/N').upper()
        if fix == "Y":
            loop2 = True
            while loop2:
                if loop2:
                    print(dataframe.columns)
                    index_col = [(input("Specify Index Column (by name)"))]
                    dataframe.set_index(index_col, inplace=True)
                    print(dataframe.to_string())
                    correct = input("Is this correct? 'Y/N'").upper()
                    if correct == "Y":
                        loop2 = False
                        return dataframe
                    elif correct == "N":
                        continue
                    else:
                        print("Incorrect specification, try again.")
            loop = False
        elif fix == "N":
            loop = False
        else:
            print("Incorrect entry, enter 'Y' or 'N'.")
            continue

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
    new_df = fix_header(data)
    new_df2 = fix_index(new_df)
    sys.exit(app.exec_())