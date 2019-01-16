import ipywidgets as widgets
from ipywidgets import HBox, VBox, Layout
from beakerx import *
import pandas as pd
from IPython.display import display
from beakerx import *

def create_panel(widgetmatrix, stretch, valign, halign, height, width, widgetsize):
    """Creates Jupyter notebook panel

    Parameters:
    widgetmatrix (list): Takes in a matrix of ipywidgets (list of lists)
    stretch (list): Specify 1 to stretch widget or 0 to not
    valign (list): Specify 'top', 'center' or 'bottom' to vertically align each widget
    valign (list): Specify 'left', 'middle' or 'right' to horizontally align each ROW
    height (int): Specify height of panel
    width (int): Specify width of panel
    widgetsize (list): Specify height and width of each widget

    Function:
    Displays customised panel
    """
    panel = []
    i = 0
    for widgetlist in widgetmatrix:
        j = 0
        for w in widgetlist:
            w.layout.padding = '10px'
            if (widgetsize[i][j][0] != 0 and widgetsize[i][j][1] != 0):
                w.layout.height = str(widgetsize[i][j][0]) + 'px'
                w.layout.width = str(widgetsize[i][j][1]) + 'px'
            if stretch[i][j] == 1:
                w.layout.flex = '1 0 auto'
            if valign[i][j] != 0:
                if valign[i][j] == 'top':
                    w.layout.align_self = 'flex-start'
                if valign[i][j] == 'center':
                    w.layout.align_self = 'center'
                if valign[i][j] == 'bottom':
                    w.layout.align_self = 'flex-end'
            j += 1

        justify = halign[i]
        if justify == 'left':
            justify = 'flex-start'
        elif justify == 'middle':
            justify = 'center'
        elif justify == 'right':
            justify = 'flex-end'

        panel.append(HBox(widgetlist, layout=Layout(padding="15px", justify_content=justify)))
        i += 1
    if height == 0 and width == 0:
        display(VBox(panel, layout=Layout(border="solid")))
    else:
        h = str(height) + "px"
        w = str(width) + "px"
        display(VBox(panel, layout=Layout(border="solid", height=h, width=w)))

#print(create_panel.__doc__)
