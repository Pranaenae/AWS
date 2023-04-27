import boto3

client = boto3.client('dynamodb', region_name = "ap-south-1")

try: 
    resp = client.create_table(
        TableName = "Books",

        KeySchema = [
            {
                "AttributeName": "Author",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Title",
                "KeyType": "RANGE"
            }
        ],

        AttributeDefinitions = [
            {
                "AttributeName": "Author",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Title", 
                "AttributeType": "S"
            }
        ],

        ProvisionedThroughput = {
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1

        }
    )

    print("Table Created Successfully") 
except Exception as e:
    print("Error:")
    print(e)