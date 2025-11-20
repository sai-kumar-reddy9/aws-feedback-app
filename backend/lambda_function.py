import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('FEEDBACK_TABLE', 'FeedbackTable')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    # Expect event['body'] to be a JSON string with name, feedback, timestamp
    try:
        body = event.get('body')
        if body is None:
            return {'statusCode':400, 'body': json.dumps({'message':'Missing body'})}
        data = json.loads(body)
        name = data.get('name', 'Anonymous')[:100]
        feedback = data.get('feedback', '')[:2000]
        timestamp = data.get('timestamp', '')
        item = {
            'id': str(uuid.uuid4()),
            'name': name,
            'feedback': feedback,
            'timestamp': timestamp
        }
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Feedback stored', 'id': item['id']})
        }
    except Exception as e:
        return {'statusCode':500, 'body': json.dumps({'message':'Error','error': str(e)})}
