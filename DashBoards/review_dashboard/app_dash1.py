# Import libs
from dash import Dash
import dash_bootstrap_components as dbc
from dash.html import H1, H2, Div, P
from dash.dcc import Graph, Dropdown, Checklist, Interval
from dash.dependencies import Input, Output

from random import randint

# Criando um alista de extilos externos
external_stylesheets = [
    'https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css'
]
# Instanciar o aplicativo dash
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Dataset para os graficos
# Numero de lementos
N = 20
dataset = {
    'index': list(range(N)),
    'adults': [randint(18, 100) for _ in range(N)],
    'kids': [randint(10, 14) for _ in range(N)],
    'teenagers': [randint(15, 17) for _ in range(N)]
}

database = {
    'index': [],
    'maiores': [],
    'menores': [],
    'bebes': [],
}


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
        H2("Gráfico Com Dropdown e Call Back"),  # Grafico 2
        Dropdown(
            id="drop1",
            options=[
                {'label': 'Kids', 'value': 'kids'},
                {'label': 'Teenagers', 'value': 'teenagers'},
                {'label': 'Adults', 'value': 'adults'}
            ],
            value='adults'
        ),
        Graph(
            id="graph_call1",
            # Remove a barra lateral padrao no grafico
            config={'displayModeBar': False},
        ),
        H2("Gráfico com dois modos interativos"),    # Grafico 3
        Checklist(
            id="check1",
            options=[
                {'label': 'Adults', 'value': 'adults'},
                {'label': 'Teenagers', 'value': 'teenagers'},
                {'label': 'Kids', 'value': 'kids'}
            ],
            value=['kids', 'adults', 'teenagers'],
            inline=True
        ),
        Dropdown(
            id="drop2",
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barras', 'value': 'bar'}
            ],
            value='bar'
        ),
        Graph(
            id="graphic_call2",
            # Remove a barra lateral padrao no grafico
            config={'displayModeBar': False},
        ),
        # Grafico atualizando em tempo real
        H2("Gráfico em Tempo Real"),
        Interval(id="interval"),
        Checklist(
            id='meu_check_list',
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value=['bebes']
        ),
        Dropdown(
            id='meu_dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barra', 'value': 'bar'},
            ],
            value='bar'
        ),
        Graph(
            id='meu_grafico',
            config={'displayModeBar': False},
        )
    ]
)

# Estrutura de Calback para o Grafico 2


@app.callback(
    Output('graph_call1', 'figure'),
    Input('drop1', 'value')
)
def graph1_call(data_input):
    return {
        'data': [
            {'y': dataset[data_input],
             'type': 'line'
             }
        ]
    }

# Call back grafico 3


@app.callback(
    Output('graphic_call2', 'figure'),
    [
        Input('check1', 'value'),
        Input('drop2', 'value')
    ]
)
def graph2_call(data_input, type_graph):
    grafico = {
        'data': [],
        'layout': {
            'title': "Dash visualization"
        }
    }
    for x in data_input:
        grafico['data'].append({
            'y': dataset[x],
            'x': dataset['index'],
            'name': x,
            'type': type_graph
        })
    return grafico

# Grafico em tempo real


def update_database(value):
    """Minha query / Atualização do pandas."""
    database['index'].append(value)
    database['menores'].append(randint(1, 200))
    database['maiores'].append(randint(1, 200))
    database['bebes'].append(randint(1, 200))


@app.callback(
    Output('meu_grafico', 'figure'),
    [
        Input('meu_check_list', 'value'),
        Input('meu_dropdown', 'value'),
        Input('interval', 'n_intervals'),
    ]
)
def my_callback(input_data, graph_type, n_intervals):
    update_database(n_intervals)
    grafico = {
        'data': []
    }
    for x in input_data:
        grafico['data'].append(
            {
                'y': database[x][-20:],
                'x': database['index'][-20:],
                'name': x,
                'type': graph_type
            },
        )
    return grafico

    # Executando o aplicativo
app.run_server(debug=True)
