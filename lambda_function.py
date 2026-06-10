import json

def lambda_handler(event, context):
    
    name = event.get('name', 'World')
    
    message = f"Hello {name}! This is Abhi's first Lambda function running on AWS Cloud!"
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message,
            'service': 'AWS Lambda',
            'region': 'Mumbai',
            'language': 'Python'
        })
    }