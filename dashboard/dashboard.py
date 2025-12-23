import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import requests

# Create Dash app
app = dash.Dash(__name__)

# Fetch data from FastAPI
def load_data():
    response = requests.get("http://127.0.0.1:8000/sales")
    return pd.DataFrame(response.json())

df = load_data()

# Create a revenue column
df["revenue"] = df["price"] * df["quantity"]

# Graphs
fig1 = px.bar(
    df,
    x="category",
    y="revenue",
    title="Revenue by Category",
    color="category"
)

fig2 = px.pie(
    df,
    names="category",
    values="revenue",
    title="Revenue Distribution"
)

fig3 = px.scatter(
    df,
    x="price",
    y="quantity",
    title="Price vs Quantity Sold"
)

# Layout
app.layout = html.Div([
    html.H1("E-Commerce Sales Dashboard", style={"textAlign": "center"}),

    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)

