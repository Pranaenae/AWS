![image](https://github.com/user-attachments/assets/d84444dc-b543-4aff-bee3-3929eaa44f4d)
![image](https://github.com/user-attachments/assets/f28bc9e1-5f65-482b-bb95-480e36349554)

Upload a file to an S3 bucket.

![image](https://github.com/user-attachments/assets/e2fb3c37-97a4-4ab9-af70-97160331fe77)

Create a policy with write access to logs and read access to S3.

![image](https://github.com/user-attachments/assets/aa41112d-b15e-4dad-92fa-d622f002ba38)

Create an execution role for lambda and attach the policy to it.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "s3:ListBucket",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:s3:::*",
                "arn:aws:logs:*:*:*"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::*/*"
        }
    ]
}
```
![image](https://github.com/user-attachments/assets/7b7eace6-bf42-455a-8ea6-e5d64b6813a0)

Create a new lambda function that returns the content type of the object uploaded and attach the role to it.
```
import urllib.parse
import json
import boto3

print("Loading function")

s3 = boto.client('s3')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("Content-Type: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(key, bucket))
        raise e
```
![image](https://github.com/user-attachments/assets/6546fc17-4630-4d5b-a6f9-6c1ab331e731)

Using the following test event
```
{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "ap-south-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "pranaygurung.me",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::pranaygurung.me"
        },
        "object": {
          "key": "python.png",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}
```
If we invoke the function using the dummy event, we get
![image](https://github.com/user-attachments/assets/c370074d-0602-4f6b-a7cc-9ab37f3119d4)

On uploading a test file to s3 the function gets triggered.
![image](https://github.com/user-attachments/assets/1adc7bd4-430a-4b7b-926c-7e2916372bdc)

![image](https://github.com/user-attachments/assets/096f019e-3a31-4132-a7c2-66a1f6f4027c)
