# Online Shop with Dash

This project is a web application built using Dash, a Python web framework, and DynamoDB for database interaction. The application allows users to create new orders, view sales graphs, and monitor worldwide product orders.

## Project Structure

- `app.py`: The main application file containing the Dash web application.

- `queries_dynamodb.py`: Module for interacting with DynamoDB, including functions for putting new orders and querying order data.

- `assets/`: Folder containing images for product visualization.

- `dash_online_shop.pdf`: A screenshot of the running application.

## Features

1. **Create New Order:**
   
   - Enter customer information, product details, and quantity to create a new order. The application validates the input data and saves the order to DynamoDB.

2. **Sales Graph:**
   
   - View an area plot showing the quantity of orders over time for a selected product.

3. **Product Orders Worldwide:**
   
   - Monitor total orders for each product with real-time updates at regular intervals.

### How to Run

1. Before running the application, ensure that you have the following dependencies installed:
  - Dash library
  - Dash Bootstrap Components
  - Plotly Express
  - Boto3
  - Pandas
- You can install these dependencies using the following command: `pip install dash dash-bootstrap-components plotly boto3 pandas`

2. Clone the repository: `git clone [repository-url]`
3. Navigate to the project directory: `cd [project-directory]`
4. Run the Dash application: `python app.py`
5. Access the application in your browser at [http://localhost:8080/](http://localhost:8080/)
