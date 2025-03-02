import boto3
import os


def handle(event, context):
    tableName = os.getenv("TABLE_NAME")
    dclient = boto3.resource("dynamodb")
    table = dclient.Table(tableName)
    connectionId = event["requestContext"]["connectionId"]
    try:
        table.delete_item(Key={"connectionid": connectionId})
    except Exception as e:
        print(e)
        return {"statusCode": 500}

    return {"statusCode": 200}
