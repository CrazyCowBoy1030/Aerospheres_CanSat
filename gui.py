import dearpygui.dearpygui as dpg
import random

max_height = 1000
height = 600

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
    cisnienie_tymczas = random.randint(0,10)
    cisnienie[-1] = cisnienie_tymczas

    for i in range(len(temperatura) - 1):
        temperatura[i] = temperatura[i+1]
    temperatura_tymczas = random.randint(0,10)
    temperatura[-1] = temperatura_tymczas

    for i in range(len(wilgotnosc) - 1):
        wilgotnosc[i] = wilgotnosc[i+1]
    wilgotnosc_tymczas = random.randint(0,10)
    wilgotnosc[-1] = wilgotnosc_tymczas

for i in range(0, 500):
    cisnienie.append(0)
    temperatura.append(0)
    wilgotnosc.append(0)
    t.append(i)

def zmiana_wysokosci():
    dpg.set_value("height", height/max_height)

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
    dpg.add_slider_float(tag="height", vertical=True, callback=zmiana_wysokosci, height=300, width=200, no_input=True, tracked=False, format='%.3f of max height', max_value=1)
    dpg.add_text("Aktualna wysokosc " + str(height))
    dpg.add_text("Maksymalna wysokosc " + str(max_height))

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
    with dpg.plot(label="All_in_one", height=400, width=1600):
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
    zmiana_cisnienia_wilgotnosci_temperatury()
    zmiana_wysokosci()
    dpg.render_dearpygui_frame()
    

dpg.destroy_context()