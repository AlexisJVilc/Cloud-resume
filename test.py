import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

try:
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('alexisjvilches-resume')
except (NoCredentialsError, PartialCredentialsError) as e:
    raise e
except Exception as e:
    raise e

def lambda_handler(event, context):
    try:
        response = table.get_item(Key={'id': '1'})
        if 'Item' not in response:
            raise KeyError("El elemento con 'id=1' no existe en la tabla.")

        views = response['Item']['views']
        views += 1

        table.put_item(Item={'id': '1', 'views': views})

        return {
            'statusCode': 200,
            'body': json.dumps({'views': views})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error interno del servidor'})
        }