import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys
from Chart_gen.chart_gen import new_chart, set_x_axis, set_y_axis, chart_type, set_main_title

# TODO fix line graph xtiks and yticks spec
#  setup specification of subplots function (multi-column selection)
#  fix incorrect spelling or entry into header and index change functions
#  further add functions for data clean and series selection
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
        print("Incorrect File Type Selected")
        sys.exit()


def transpose_data(dataframe):
    """Quick function to transpose data and return resultant dataframe"""
    print(dataframe.head(10).to_string())
    trans = input("Transpose data 'Y/N?").upper()
    if trans == "Y":
        df = dataframe.T
        return df
    else:
        return dataframe

def fix_header(dataframe):
    """Function for data cleaning, allows for manual specification of the header row and replaces, returning
    resultant dataframe"""
    print(dataframe.head(10).to_string())
    loop = True
    while loop:
        fix = input('Change Header Row? Type Y/N').upper()
        if fix == "Y":
            loop2 = True
            while loop2:
                if loop2:
                    print(dataframe.head(10).to_string())
                    header_row = int(input("Specify Header Row (from 0)"))
                    headers = dataframe.iloc[header_row]
                    new_df = dataframe[(header_row+1):]
                    new_df.columns = headers
                    print(new_df.head(10).to_string())
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
                    print(dataframe.head(10).to_string())
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
            return dataframe
        else:
            print("Incorrect entry, enter 'Y' or 'N'.")
            continue


def gather_data(dataframe):
    """runs dictionary functions to collect variables for graph construction"""
    obj = new_chart()
    set_x_axis(obj, dataframe)
    set_y_axis(obj)
    chart_type(obj)
    set_main_title(obj)
    print(obj)
    return obj


def generate_graph(obj, dataframe):
    if obj['chart_style'] == 'line':
        generate_line_graph(obj, dataframe)
    elif obj['chart_style'] == 'bar':
        pass
    elif obj['chart_style'] == 'scatter':
        pass


def generate_line_graph(obj, dataframe):
    "Function for plotting and displaying line graph"
    if obj['x_axis'] == 'index':
        plt.plot(dataframe.index, dataframe[obj['y_axis']])
        plt.xticks(np.linspace(0, len(dataframe.index)), dataframe.index, rotation='vertical')
        # plt.yticks(np.linspace(0, len(dataframe[obj['y_axis']])), dataframe[obj['y_axis']])
        plt.xlabel(" ") #fix this later
        plt.ylabel(obj['y_axis'])
        plt.title(obj['main_title'])
        plt.tight_layout()
        plt.show()
    elif obj['y_axis'] == 'index':
        plt.plot(dataframe[obj['x_axis']], dataframe.index)
        plt.yticks(np.linspace(0, len(dataframe.index)), dataframe.index)
        plt.xticks(np.linspace(0, len(dataframe[obj['x_axis']])), dataframe[obj['x_axis']], rotation= 'vertical')
        plt.xlabel(obj['x_axis'])
        plt.ylabel(" ") #fix this later
        plt.title(obj['main_title'])
        plt.tight_layout()
        plt.show()
    else:
        plt.plot(dataframe[obj['x_axis']], dataframe[obj['y_axis']])
        # plt.yticks(np.linspace(0, len(dataframe[obj['y_axis']])), dataframe[obj['y_axis']])
        plt.xticks(np.linspace(0, len(dataframe[obj['x_axis']])), dataframe[obj['x_axis']], rotation='vertical')
        plt.xlabel(obj['x_axis'])
        plt.ylabel(obj['y_axis'])
        plt.title(obj['main_title'])
        plt.tight_layout()
        plt.show()



def generate_bar_graph(obj, dataframe):
    "Function for plotting and displaying bar graph"
    pass


def generate_scatter(obj, dataframe):
    "Function for plotting and displaying scatter graph"
    pass

def save_plot(object, filename):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_name = file_open()
    data = file_check(file_name)
    data1 = transpose_data(data)
    new_df = fix_header(data1)
    new_df2 = fix_index(new_df)
    plot_elements = gather_data(new_df2)
    generate_graph(plot_elements, new_df2)
    sys.exit(app.exec_())