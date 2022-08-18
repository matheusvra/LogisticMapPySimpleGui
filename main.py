import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# VARS CONSTS:
# Upgraded mu to global...
_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False,
         'mu': 2.0,
         'bifurcation': None}


plt.style.use('Solarize_Light2')

# Helper Functions


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# \\  -------- PYSIMPLEGUI -------- //

AppFont = 'Any 16'
SliderFont = 'Any 14'
sg.theme('black')

# New layout with slider and padding

layout = [
        [sg.Text(text="Logistic map - F(x[k]) = µ(1 - x[k-1])x[k-1]",
                   font=SliderFont,
                   background_color='#FDF6E3',
                   pad=((0, 0), (10, 0)),
                   text_color='Black')],
        [sg.Text(text="",
                   font=SliderFont,
                   background_color='#FDF6E3',
                   pad=((0, 0), (30, 0)),
                   text_color='Black',
                   key='screen')],
        [sg.Canvas(key='figCanvas', background_color='#FDF6E3')],
          [sg.Text(text="µ :",
                   font=SliderFont,
                   background_color='#FDF6E3',
                   pad=((0, 0), (10, 0)),
                   text_color='Black'),
           sg.Slider(range=(2, 4), orientation='h', size=(47, 20),
                     default_value=_VARS['mu'],
                     background_color='#FDF6E3',
                     text_color='Black',
                     key='-Slider-',
                     resolution=.001,
                     enable_events=True),
           sg.Button('Bifurcation',
                     font=AppFont,
                     pad=((4, 0), (10, 0)))],
          # pad ((left, right), (top, bottom))
          [sg.Button('<', pad=((250, 0), (0, 0))), sg.Button('>', pad=((10, 0), (0, 0))), sg.Button('Exit', font=AppFont, pad=((210, 0), (0, 0)))]]

_VARS['window'] = sg.Window('Logistic Map',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(100, 100),
                            element_justification="center",
                            background_color='#FDF6E3')

# \\  -------- PYSIMPLEGUI -------- //


# \\  -------- PYPLOT -------- //




def logistic_map(N, x0, **kwargs):
    mu = kwargs.get('mu')
    N_points = kwargs.get('N_points', 100)
    if mu is None:
        raise ValueError("mu [float] precisa ser passado como parâmetro nomeado")
    
    x = np.empty(shape=(N,))
    x[0] = x0
    k_array = np.arange(1,N)
    for k in k_array:
        x[k] = mu*(1-x[k-1])*x[k-1]
    
    return k_array[-N_points:], x[-N_points:]

def makeSynthData():
    return logistic_map(N=1000, x0=1e-6, mu=_VARS['mu'], N_points=500)


def drawChart():
    _VARS['pltFig'] = plt.figure()
    dataXY = makeSynthData()
    plt.plot(dataXY[0], dataXY[1], '.k')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])


def load_bifurcation_map():
    _VARS['bifurcation'] = bifurcation()

def bifurcation():
    mu_vec = np.arange(2.001, 3.999, 0.001)
    mu_vec_logistic_map = np.empty(shape=(100*len(mu_vec),))
    x_logistic_map = np.empty(shape=(100*len(mu_vec),))
    x = np.empty(shape=(len(mu_vec),), dtype=np.ndarray)

    for k, mu in enumerate(mu_vec):
        mu_vec_logistic_map[k*100:k*100+100] = mu
        x_logistic_map[k*100:k*100+100] = logistic_map(500, 1e-6, mu=mu)[1][-100:]
    
    
    return mu_vec_logistic_map, x_logistic_map

def updateChart():
    _VARS['fig_agg'].get_tk_widget().forget()
    dataXY = makeSynthData()
    # plt.cla()
    plt.clf()
    plt.plot(dataXY[0], dataXY[1], '.k')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

def updateChartBifurcation():
    _VARS['fig_agg'].get_tk_widget().forget()
    dataXY = _VARS['bifurcation']
    # plt.cla()
    plt.clf()
    plt.plot(dataXY[0], dataXY[1], '.k')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

    _VARS['window']['screen'].update("Bifurcation Diagram")


def updateData(val):
    _VARS['mu'] = val
    updateChart()
    _VARS['window']['screen'].update("")

def decrement_mu():
    _VARS['mu'] = max(2, _VARS['mu'] - 0.001)
    _VARS['window']['-Slider-'].update(_VARS['mu'])
    updateChart()
    _VARS['window']['screen'].update("")
    

def increment_mu():
    _VARS['mu'] = min(4, _VARS['mu'] + 0.001)
    _VARS['window']['-Slider-'].update(_VARS['mu'])
    updateChart()
    _VARS['window']['screen'].update("")

# \\  -------- PYPLOT -------- //

if __name__ == "__main__":

    load_bifurcation_map()

    drawChart()

    # MAIN LOOP
    while True:
        event, values = _VARS['window'].read(timeout=200)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Bifurcation':
            updateChartBifurcation()
        elif event == '-Slider-':
            updateData(float(values['-Slider-']))
        elif event == '<':
            decrement_mu()
        elif event == '>':
            increment_mu()
    _VARS['window'].close()