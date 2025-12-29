import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
import requests

# Initialize app
app = dash.Dash(__name__)
app.title = "E-Commerce Analytics Dashboard"

# Load data
def load_data():
    response = requests.get("http://127.0.0.1:8000/sales")
    df = pd.DataFrame(response.json())
    df["revenue"] = df["price"] * df["quantity"]
    return df

df = load_data()

# KPIs
total_sales = len(df)
total_revenue = int(df["revenue"].sum())
avg_price = int(df["price"].mean())

# ------------------- GRAPHS (DARK THEME) -------------------
bar_category = px.bar(
    df,
    x="category",
    y="revenue",
    color="category",
    title="Revenue by Category",
    template="plotly_dark"
)

pie_category = px.pie(
    df,
    names="category",
    values="revenue",
    title="Revenue Share",
    template="plotly_dark"
)

scatter_price_qty = px.scatter(
    df,
    x="price",
    y="quantity",
    size="revenue",
    color="category",
    title="Price vs Quantity Sold",
    template="plotly_dark"
)

line_revenue = px.line(
    df.reset_index(),
    y="revenue",
    title="Revenue Trend",
    template="plotly_dark"
)

hist_price = px.histogram(
    df,
    x="price",
    nbins=12,
    title="Price Distribution",
    template="plotly_dark"
)

# ------------------- LAYOUT -------------------
app.layout = html.Div(
    style={
        "backgroundColor": "#0e1117",
        "padding": "20px",
        "color": "white",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "E-Commerce Sales Analytics",
            style={"textAlign": "center", "marginBottom": "30px"}
        ),

        # KPI Cards
        html.Div(
            style={"display": "flex", "justifyContent": "space-around"},
            children=[

                html.Div([
                    html.H4("Total Sales"),
                    html.H2(total_sales)
                ], style={
                    "background": "#161b22",
                    "padding": "20px",
                    "borderRadius": "12px",
                    "width": "25%",
                    "textAlign": "center",
                    "boxShadow": "0px 0px 12px #00f2ff"
                }),

                html.Div([
                    html.H4("Total Revenue"),
                    html.H2(f"₹ {total_revenue}")
                ], style={
                    "background": "#161b22",
                    "padding": "20px",
                    "borderRadius": "12px",
                    "width": "25%",
                    "textAlign": "center",
                    "boxShadow": "0px 0px 12px #00ff85"
                }),

                html.Div([
                    html.H4("Average Price"),
                    html.H2(f"₹ {avg_price}")
                ], style={
                    "background": "#161b22",
                    "padding": "20px",
                    "borderRadius": "12px",
                    "width": "25%",
                    "textAlign": "center",
                    "boxShadow": "0px 0px 12px #ff8c00"
                })
            ]
        ),

        html.Br(), html.Br(),

        dcc.Graph(figure=bar_category),
        dcc.Graph(figure=pie_category),

        html.Div(
            style={"display": "flex"},
            children=[
                html.Div(dcc.Graph(figure=scatter_price_qty), style={"width": "50%"}),
                html.Div(dcc.Graph(figure=hist_price), style={"width": "50%"})
            ]
        ),

        dcc.Graph(figure=line_revenue),

        html.H3("Sample Sales Records", style={"marginTop": "30px"}),

        dash_table.DataTable(
            data=df.head(10).to_dict("records"),
            columns=[{"name": i, "id": i} for i in df.columns],
            style_table={"overflowX": "auto"},
            style_header={
                "backgroundColor": "#21262d",
                "color": "white",
                "fontWeight": "bold"
            },
            style_cell={
                "backgroundColor": "#0e1117",
                "color": "white",
                "textAlign": "center",
                "border": "1px solid #30363d"
            }
        )
    ]
)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
