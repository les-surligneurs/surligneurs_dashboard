import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from views.index import index
from views.header import  header
from views.footer import footer


app = dash.Dash(__name__ ,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.LUX] )
server = app.server
app.layout = html.Div([dcc.Location(id='url', refresh=True), html.Div(id='page-content', children=[])])


@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')]  )
def display_page(pathname):
        if (pathname == '/'):
                return html.Div( [header , index , html.Br(children=[])  , footer])

if __name__ == '__main__':
    app.run_server(debug=True)
