import json

def lambda_handler(event, context):
    print("file recived:",json.dump(event))
    return {'statusCode': 200,
        'body': 'Hello from Lambda!'}