from dash import dcc, html, Input, Output, State, Dash
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
from queries_dynamodb import *

# Set Plotly template
pio.templates.default = "simple_white"

# List containing dictionaries for each product with keys: name and image
products = [
    {"name": "Book", "image": "book.png"},
    {"name": "Shoes", "image": "sneakers.png"},
    {"name": "Plant", "image": "spider-plant.png"}
]

# Dash application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout
app.layout = dbc.Container([
    html.H1('Create New Order'),
    html.H6('Order Information: Email, Lastname, Firstname, Country, Product, Quantity'),
    html.Div(dbc.Input(id='input', type='text')),        
    dbc.Button('Save', id='submit', n_clicks=0),
    html.Div(id='result'),
    
    html.H1('Sales for the Product:'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Book', 'value': 'book'},
            {'label': 'Shoes', 'value': 'shoes'},
            {'label': 'Plant', 'value': 'plant'}
        ],
        value='plant'
    ),
    dcc.Graph(id='orders'),
    
    html.H1('Product Orders Worldwide'),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.CardHeader(product["name"]),
                        dbc.CardBody(
                            [
                                dbc.CardImg(src=app.get_asset_url(product["image"]), top=True),
                            ]
                        ),
                        dbc.CardFooter(
                            [
                                html.P(id=f'{product["name"].lower()}-total'),
                                dcc.Interval(id=f'{product["name"].lower()}-interval',
                                             interval=10 * 1000,
                                             n_intervals=0
                                )
                            ]
                        )
                    ]
                )
            )
        ) for product in products
    ])
])


# Callback for saving orders
@app.callback(
    Output('result', 'children'),
    Input('submit', 'n_clicks'),
    State('input', 'value')
)

def new_order(n_clicks, value):
    # Check if the submit button is clicked and the input value is not None
    if n_clicks > 0 and value is not None:
        # Split the input value into individual values
        values = value.split(', ')
        # Check if there are exactly 6 values
        if len(values) == 6:
            customerID, lastname, firstname, country, product, quantity = values

            # Email address validation
            if '@' not in customerID:
                return "Invalid email address"
            
            # Valid products for order
            valid_products = ["plant", "book", "shoes"]

            # Product validation
            if product.lower() not in valid_products:
                return "Invalid product"

            # Quantity validation
            if not quantity.isdigit() or int(quantity) <= 0:
                return "Invalid quantity"

            # Add the order to the DynamoDB table
            response = put_new_order(customerID, lastname, firstname, country, product, quantity)
            # Check if the order was successfully saved
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return "Order successfully saved"
            else:
                return "Error saving the order"
        
        else:
            return "Incomplete order information"
            
    return "Enter order information"


# Callback for the sales graph
@app.callback(
    Output('orders', 'figure'),
    Input('dropdown', 'value')
)

def get_orders_graph(dropdown_product):
    # Retrieve order data for the selected product
    df = get_orders_timerange(dropdown_product)
    
    # Create an area plot using Plotly Express
    fig = px.area(
        df,
        x='orderID',
        y='quantity',
        labels={
            'orderID': 'Order Date',
            'quantity': 'Order Quantity'
        }
    )
    return fig


# Callbacks for product cards    
for product in products:
    @app.callback(
        Output(f'{product["name"].lower()}-total', 'children'),
        Input(f'{product["name"].lower()}-interval', 'n_intervals')
    )
    
    def update_product_orders(n_intervals, product_name=product["name"].lower()):
        # Update the total orders for each product at regular intervals
        return int(get_total_orders(product_name))


# Start the server
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
