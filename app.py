import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('HITS_TABLE_NAME')
table = dynamodb.Table(table_name)
primary_key = os.environ.get('PRIMARY_KEY')

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={
                'id': primary_key
            },
            UpdateExpression='ADD hits :inc',
            ExpressionAttributeValues={
                ':inc': 1
            },
            ReturnValues='UPDATED_NEW'
        )
        print(f"DynamoDB update response: {response}")
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Visit counter updated successfully!'})
        }
    except Exception as e:
        print(f"Error updating DynamoDB: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error updating visit counter'})
        }

# Optional: To show the hit count
# def lambda_handler(event, context):
#     try:
#         get_response = table.get_item(
#             Key={
#                 'id': primary_key
#             }
#         )
#         hits = get_response.get('Item', {}).get('hits', 0)
#
#         update_response = table.update_item(
#             Key={
#                 'id': primary_key
#             },
#             UpdateExpression='SET hits = :val',
#             ExpressionAttributeValues={
#                 ':val': hits + 1
#             },
#             ReturnValues='UPDATED_NEW'
#         )
#         print(f"DynamoDB update response: {update_response}")
#         return {
#             'statusCode': 200,
#             'body': json.dumps({'hits': hits + 1})
#         }
#     except Exception as e:
#         print(f"Error interacting with DynamoDB: {e}")
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'error': 'Error updating visit counter'})
#         }