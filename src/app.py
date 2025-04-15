import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['HITS_TABLE_NAME'])

def lambda_handler(event, context):
    try:
        # Increment the hit counter for the resume
        response = table.update_item(
            Key={'id': os.environ['PRIMARY_KEY']},
            UpdateExpression='ADD visits :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues='UPDATED_NEW'
        )
        return {
            'statusCode': 200,
            'body': f"Updated visits count to {response['Attributes']['visits']}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
