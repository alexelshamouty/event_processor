import boto3
import os
from mypy_boto3_dynamodb.service_resource import Table

def handle(event, context):
    tableName = os.getenv("TABLE_NAME","usersTable")
    dclient = boto3.resource("dynamodb")
    table: Table = dclient.Table(name=tableName)
    connectionId = event["requestContext"]["connectionId"]
    try:
        table.put_item(Item={"connectionid": connectionId})
    except Exception as e:
        print(e)
        return {"statusCode": 500}

    return {"statusCode": 200}
