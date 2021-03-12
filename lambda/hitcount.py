import json
import os

import boto3


def handler(event, context):
    ddb = boto3.resource("dynamodb")
    table = ddb.Table(os.environ["HITS_TABLE_NAME"])

    table.update_item(
        Key={"path": event["path"]},
        UpdateExpression="ADD hits :incr",
        ExpressionAttributeValues={":incr": 1},
    )

    resp = boto3.client("lambda").invoke(
        FunctionName=os.environ["DOWNSTREAM_FUNCTION_NAME"],
        Payload=json.dumps(event),
    )

    body = resp["Payload"].read()
    return json.loads(body)
