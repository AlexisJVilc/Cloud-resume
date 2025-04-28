import boto3
import os
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.getenv('HITS_TABLE_NAME', None)
if not table_name:
    raise ValueError("Environment variable 'HITS_TABLE_NAME' is not set.")

primary_key = os.getenv('PRIMARY_KEY', None)
if not primary_key:
    raise ValueError("Environment variable 'PRIMARY_KEY' is not set.")

table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': primary_key},
            UpdateExpression='ADD visits :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues='UPDATED_NEW'
        )
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': "Visits count updated successfully.",
                'updated_visits': response['Attributes']['visits']
            })
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': "An error occurred while updating visits count.",
                '

