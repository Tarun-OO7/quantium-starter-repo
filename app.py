import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[

        # Header
        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        # Region Filter
        html.Div(
            [
                html.Label(
                    "Select Region:",
                    style={
                        "fontSize": "18px",
                        "fontWeight": "bold"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px"}
                )
            ],
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0px 2px 8px rgba(0,0,0,0.1)",
                "marginBottom": "20px"
            }
        ),

        # Graph
        dcc.Graph(id="sales-chart")
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[
            df["Region"].str.lower() == selected_region.lower()
        ]

    sales_by_date = (
        filtered_df.groupby("Date")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Date")
    )

    fig = px.line(
        sales_by_date,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales - {selected_region.title()}"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        title_x=0.5
    )

    # Price increase marker
    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
