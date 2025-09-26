import json

def lambda_handler(event, context):
    name = event.get('name', 'world')
    return {
        'statusCode':200,
        'body':json.dumps(f"Hello, {name}!")
    }