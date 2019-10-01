import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    #Obtain URL parameters from Lambda function using proxy parameters
    id = event["queryStringParameters"]['url']
    # Check if id is falsy or not
    if not id:
        return {
            'statusCode': 400,
            'body': 'Empty parameters '
        }
    # Query DynamoDB for the item using the 
    try:
        big_url = dynamodb.get_item(TableName='links',Key={'id':{'S':id}})
        return {
            'statusCode': 200,
            'body': big_url['Item']['url']['S']
        }
    except Exception as error:
        return {
            'statusCode': 500,
            'body': error
        }
