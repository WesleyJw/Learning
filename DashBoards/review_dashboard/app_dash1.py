# Import libs
from dash import Dash
from dash_html_components import H1, H2

# Instanciar o aplicativo dash
app = Dash(__name__)

# Colocando um titulo
app.layout = H1("Hello World Dash")

# Executando o aplicativo
app.run_server()
