![image](https://github.com/user-attachments/assets/d84444dc-b543-4aff-bee3-3929eaa44f4d)

Upload a file to an S3 bucket.

![image](https://github.com/user-attachments/assets/e2fb3c37-97a4-4ab9-af70-97160331fe77)

Create a policy with write access to logs and read access to S3.

![image](https://github.com/user-attachments/assets/aa41112d-b15e-4dad-92fa-d622f002ba38)

Create an execution role for lambda and attach the policy to it.

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

