import json
import os
import boto3

def hello(event, context):
    tableName = os.getenv("TABLE_NAME")
    try:
        body = json.loads(event.get('body',""))
    except Exception as e:
        print("There is no body in the request")
        print(e)
        return {"statusCode":501}

    dclient = boto3.resource('dynamodb')
    table = dclient.Table(tableName)
    if 'event' in body.keys():
        item = {
        "id": body.get("id", ""),  # Partition key
        "event": body.get("event", ""),
        "type_of_event": body.get("type_of_event", ""),
        "text": body.get("text", ""),
        "full_text": body.get("full_text", ""),
        "category": body.get("category", ""),
        "source_app": body.get("source_app", ""),
        "when": body.get("when", ""),
        "timestamp": body.get("timestamp", ""),
    }

        try:
            table.put_item(Item=item)
        except Exception as e:
            print(e)
            return {"statusCode":500} 

    print(body)
    print(tableName)
    response = {"statusCode": 200}

    return response
