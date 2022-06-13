# Import libs
from dash import Dash
import dash_bootstrap_components as dbc
from dash.html import H1, H2, Div, P

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
        P("Coloque o gráfico aqui"),
        H2("Gráfico 2"),
        P("Coloque o gráfico aqui")
    ]
)

# Executando o aplicativo
app.run_server(debug=True)
