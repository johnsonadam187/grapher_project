import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def new_chart():
    """Creates as dict for storage of chart objects and attributes"""
    return {}


def set_main_title(object, title):
    """Creates ability to save the proposed title as 'main_title' in the new_chart dict"""
    object['main_title'] = title


def set_x_title(object, title):
    """Creates ability to save the proposed label as 'x_title' in the new_chart dict"""
    object['x_title'] = title


def set_y_title(object, title):
    """Creates ability to save the proposed label as 'y_title' in the new_chart dict"""
    object['y_title'] = title


def data_type(object, title):
    """Creates ability to specify the proposed data type as 'data_type' in the new_chart dict"""
    object['data_type'] = title


def use_data(object, series):
    """Creates ability to specify the proposed data as 'data' in the new_chart dict"""
    object['data'] = series


def chart_type(object, chart_style):
    "Creates ability for chart style to be stored in dict as 'chart_style"
    object['chart_style'] = chart_style