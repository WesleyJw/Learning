# Import libs
from dash import Dash
import dash_bootstrap_components as dbc
from dash.html import H1, H2, Div, P
from dash.dcc import Graph

# Instanciar o aplicativo dash


# Criando um alista de extilos externos
external_stylesheets = [
    'https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css'
]
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Colocando um titulo
app.layout = Div(
    children=[
        H1("Hello world Dash"),
        P("Layout para composição de gráfico"),
        H2("Gráfico 1"),
        Graph(
            figure={
                'data': [
                    {'x': [1, 2, 3, 4, 5],
                     'type': 'box',
                     'name': 'Variavel'
                     }
                ],
                'layout': {
                    'title': 'Box-Plot (Gráfico Bigode)',
                    'plot_bgcolor': '#222225',  # background dentro do grafico
                    'paper_bgcolor': '#222225',  # background em volta do grafico
                    'titlefont': {
                        'size': 25,
                        'color': '#e8e9ed'
                    },
                    'font': {
                        'size': 16,
                        'color': '#e8e9ed'
                    }
                }

            }
        ),
        H2("Gráfico 2"),
        Graph(
            # Remove a barra lateral padrao no grafico
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'x': [1, 2, 2, 3, 3, 3, 4, 4, 5],
                     'type': 'histogram'
                     }
                ]
            }
        ),
        H2("Gráfico 3"),
        Graph(
            # Remove a barra lateral padrao no grafico
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2],
                        'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5],
                        'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ]
)

# Executando o aplicativo
app.run_server(debug=True)
