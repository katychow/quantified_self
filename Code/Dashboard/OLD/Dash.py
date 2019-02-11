import dash
import dash_core_components as dcc
import dash_html_components as html

dcc.Dropdown(
    options = [
        {'label': 'Test1','value':1},
        {'label': 'Test2', 'value':2}
    ],
    value = 2
)
