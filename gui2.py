import dearpygui.dearpygui as dpg


import logging

import random
import time

logger = logging.getLogger(__name__)
logging.basicConfig(filename='data.log', encoding='utf-8', level=logging.DEBUG)


now = [0, 0, 0, 0]

max_height = 1
height = 1

cisnienie = []
t = []

cisnienie_tymczas = 0

temperatura = []

temperatura_tymczas = 0

wilgotnosc = []

wilgotnosc_tymczas = 0

def push():
    for i in range(len(cisnienie) - 1):
        cisnienie[i] = cisnienie[i+1]
    cisnienie_tymczas = now[2]
    cisnienie[-1] = cisnienie_tymczas

    for i in range(len(temperatura) - 1):
        temperatura[i] = temperatura[i+1]
    temperatura_tymczas = now[1]
    temperatura[-1] = temperatura_tymczas

    for i in range(len(wilgotnosc) - 1):
        wilgotnosc[i] = wilgotnosc[i+1]
    wilgotnosc_tymczas = now[3]
    wilgotnosc[-1] = wilgotnosc_tymczas

for i in range(0, 500):
    cisnienie.append(0)
    temperatura.append(0)
    wilgotnosc.append(0)
    t.append(i)

def zmiana_wysokosci():
    dpg.set_value("height", height/max_height)
    dpg.set_item_label("wys", height)
    dpg.set_item_label("max_wys", max_height)

def zmiana_cisnienia_wilgotnosci_temperatury():
    update_series()

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


def update_series():

    push()
    dpg.set_value('series_tag', [t, cisnienie])
    dpg.set_value('series_tag2', [t, temperatura])
    dpg.set_value('series_tag3', [t, wilgotnosc])
    dpg.set_value('series_tagcis', [t, cisnienie])
    dpg.set_value('series_tagwilg', [t, temperatura])
    dpg.set_value('series_tagtemp', [t, wilgotnosc])
    # dpg.set_item_label('series_tag', "0.5 + 0.5 * cos(x)")

with dpg.window(label="GPS", pos=(0,0), height=450, width=250):
    dpg.add_text("Cansat GPS")
    dpg.add_slider_float(tag="height", vertical=True, callback=zmiana_wysokosci, height=300, width=200, no_input=True, tracked=False, format="%.3f of max height", max_value=1)
    dpg.add_text("Aktualna wysokosc ")
    dpg.add_button(label=height, tag="wys")
    dpg.add_text("Maksymalna wysokosc ")
    dpg.add_button(label=max_height, tag="max_wys")

with dpg.window(label="Cisnienie", tag="win", pos=(250,0), height=450, width=450):
    # create plot
    with dpg.plot(label="cisnienie", height=400, width=400):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="time")
        dpg.add_plot_axis(dpg.mvYAxis, label="cisnienie", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(t, cisnienie, label="cisnienie", parent="y_axis", tag="series_tag")

with dpg.window(label="Temperatura", tag="win2", pos=(700,0), height=450, width=450):
    # create plot
    with dpg.plot(label="temperatura", height=400, width=400):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="time")
        dpg.add_plot_axis(dpg.mvYAxis, label="temperatura", tag="y_axis2")

        # series belong to a y axis
        dpg.add_line_series(t, temperatura, label="temperatura", parent="y_axis2", tag="series_tag2")

with dpg.window(label="Wilgotnosc", tag="win3", pos=(1150,0), height=450, width=450):
    # create plot
    with dpg.plot(label="wilgotnosc", height=400, width=400):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="time")
        dpg.add_plot_axis(dpg.mvYAxis, label="wilgotnosc", tag="y_axis3")

        # series belong to a y axis
        dpg.add_line_series(t, temperatura, label="wilgotnosc", parent="y_axis3", tag="series_tag3")

with dpg.window(label="All_in_one", tag="win4", pos=(0,450), height=450, width=1600):
    # create plot
    with dpg.plot(label="All_in_one", height=400, width=1550):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="time")
        dpg.add_plot_axis(dpg.mvYAxis, label="temperatura", tag="y_axistemp")
        dpg.add_plot_axis(dpg.mvYAxis, label="cisnienie", tag="y_axiscis")
        dpg.add_plot_axis(dpg.mvYAxis, label="wilgotnosc", tag="y_axiswilg")
        

        # series belong to a y axis
        dpg.add_line_series(t, temperatura, label="temperatura", parent="y_axistemp", tag="series_tagtemp")
        dpg.add_line_series(t, temperatura, label="cisnienie", parent="y_axiscis", tag="series_tagcis")
        dpg.add_line_series(t, temperatura, label="wilgotnosc", parent="y_axiswilg", tag="series_tagwilg")


dpg.show_viewport()

zmiana_wysokosci()

while dpg.is_dearpygui_running() == True:
    wys4 = random.randint(1,1000)
    cis4 = random.randint(0,10)
    temp4 = random.randint(0,10)
    wilg4 = random.randint(0,10)

    logger.info("$" + str(wys4) + "$" +str(temp4) + "$" +str(cis4) + "$" +str(wilg4) + "$" + str(time.time()))
    with open('data.log', 'r') as f:
        last_line = f.readlines()[-1]
        x = last_line.find("$", 0, len(last_line)) + 1
        tymczas = last_line.find("$", x + 1, len(last_line)) + 1
        now[0] = float(last_line[x:tymczas - 1])
        tymczas2 = last_line.find("$", tymczas + 1, len(last_line)) + 1
        now[1] = float(last_line[tymczas:tymczas2 - 1])
        tymczas = last_line.find("$", tymczas2 + 1, len(last_line)) + 1
        now[2] = float(last_line[tymczas2:tymczas - 1])
        tymczas2 = last_line.find("$", tymczas, len(last_line)) + 1
        now[3] = float(last_line[tymczas:tymczas2 - 1])
    height = now[0]
    max_height = max(max_height, height)
    zmiana_cisnienia_wilgotnosci_temperatury()
    zmiana_wysokosci()  
    dpg.render_dearpygui_frame()
    

dpg.destroy_context()