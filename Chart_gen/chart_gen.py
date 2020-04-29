import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def new_chart():
    """Creates as dict for storage of chart objects and attributes"""
    return {}


def set_x_axis(object, dataframe):
    """Creates ability to save the proposed label as 'x_title' in the new_chart dict"""
    print(dataframe.to_string())
    x_axis_string = input("Select Column for X Axis or type 'index' for the index column")
    object['x_axis'] = x_axis_string


def set_y_axis(object):
    """Creates ability to save the proposed label as 'y_title' in the new_chart dict"""
    y_axis_string = input("Select Column for Y Axis or type 'index' for the index column")
    object['y_axis'] = y_axis_string


def chart_type(object):
    "Creates ability for chart style to be stored in dict as 'chart_style"
    chart_style_string = input("Select Chart Type - 'line, bar or scatter'").lower()
    object['chart_style'] = chart_style_string


def set_main_title(object):
    """Creates ability to save the proposed title as 'main_title' in the new_chart dict"""
    main_title_string = input("Type Proposed Chart Title").capitalize()
    object['main_title'] = main_title_string




