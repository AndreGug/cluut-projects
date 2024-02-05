import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd
from datetime import date

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')


def put_new_order(customerID, lastname, firstname, country, product, quantity):
    # Create a new order dictionary
    new_order = {
        'customerID': customerID,
        'orderID': date.today().strftime('%Y%m%d'),
        'lastname': lastname,
        'firstname': firstname,
        'country': country,
        'product': product,
        'quantity': int(quantity)
    }

    # Put the new order into the DynamoDB table
    response = table.put_item(Item=new_order)
    return response


def get_orders_timerange(product_name):
    # Query DynamoDB table for orders of a specific product within a time range
    response = table.query(
        IndexName='Products',
        KeyConditionExpression=Key('product').eq(product_name),
        ProjectionExpression='orderID, quantity'
    )
    
    df = pd.DataFrame(response['Items'])
    df['orderID'] = pd.to_datetime(df['orderID'])
    df = df.sort_values(by='orderID')

    return df
    
    
def get_total_orders(product_name):
    # Query DynamoDB table to get the total quantity of a specific product
    response = table.query(
        IndexName='Products',
        KeyConditionExpression=Key('product').eq(product_name),
        ProjectionExpression='quantity'
    )
    
    df = pd.DataFrame(response['Items'])
    total = int(df['quantity'].sum())

    return total


if __name__ == '__main__':
    # Test the functions
    print(put_new_order('andre.gug@gmx.net', 'Guggenheimer', 'André', 'Germany', 'plant', 5))
    print(get_orders_timerange('plant'))
    print(get_total_orders('plant'))
