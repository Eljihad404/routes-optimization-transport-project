"""
app.py
------
Example Dash application for visualizing route assignments and CO2 emissions.
"""
"""
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Load data (or load from a DB or API in a real scenario)
vehicles_df = pd.read_csv("../data/vehicles.csv")
routes_df = pd.read_csv("../data/routes.csv")
shipments_df = pd.read_csv("../data/shipments.csv")

# Example figure (just to show some data)
fig = px.bar(vehicles_df, x='vehicle_id', y='max_capacity', title="Vehicle Capacities")

app.layout = html.Div([
    html.H1("CO2 Reduction Dashboard"),
    dcc.Graph(figure=fig),
    html.Div([
        html.H3("Routes Data"),
        dcc.Markdown(routes_df.to_markdown())
    ]),
    html.Div([
        html.H3("Shipments Data"),
        dcc.Markdown(shipments_df.to_markdown())
    ]),
])

if __name__ == "__main__":
    app.run_server(debug=True)
"""
"""
app.py
------
Example Dash application for visualizing route assignments and CO2 emissions,
now with a more modern look using dash-bootstrap-components.
"""

import dash
import dash_bootstrap_components as dbc  # <-- New import for Bootstrap components
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Use a Bootstrap theme (e.g., LITERA, FLATLY, etc.)
external_stylesheets = [dbc.themes.FLATLY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "CO2 Reduction Dashboard"  # This sets the browser tab title

# Load data (or load from a DB or API in a real scenario)
vehicles_df = pd.read_csv("../data/vehicles.csv")
routes_df = pd.read_csv("../data/routes.csv")
shipments_df = pd.read_csv("../data/shipments.csv")

# Example figure (just to show some data)
fig = px.bar(
    vehicles_df, 
    x='vehicle_id', 
    y='max_capacity', 
    title="Vehicle Capacities",
    template='plotly_white'  # A clean Plotly theme
)

# Create a navbar using Bootstrap components
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("CO2 Reduction Project", href="#"),
        ]
    ),
    color="primary",
    dark=True,
    className="mb-4"
)

# Main layout in a Bootstrap Container
app.layout = dbc.Container([
    # Navbar at the top
    navbar,

    dbc.Row([
        dbc.Col([
            html.H2("Dashboard Overview", className="text-center mb-4"),
            dcc.Graph(figure=fig),
        ], width=12),
    ]),

    dbc.Row([
        dbc.Col([
            html.H3("Routes Data"),
            dcc.Markdown(routes_df.to_markdown()),
        ], width=6),

        dbc.Col([
            html.H3("Shipments Data"),
            dcc.Markdown(shipments_df.to_markdown()),
        ], width=6)
    ], className="mt-4"),

], fluid=True)  # fluid=True makes the container 100% width on all devices

if __name__ == "__main__":
    app.run_server(debug=True)

