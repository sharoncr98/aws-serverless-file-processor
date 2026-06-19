import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = "MASKED_ARN"

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']

    print(f"File uploaded: {filename}")

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="New File Uploaded",
        Message=f"File {filename} was uploaded to bucket {bucket}"
    )

    return {
        'statusCode': 200
    }
