# Create a serverless DynamoDB app with Lambda function for CRUD operations.

In this project, I have built a serverless DynamoDB application. A new API is built that takes POST requests from the client and passes it on to the lambda function which handles the CRUD operations on the DynamoDB table. The API is tested using Postman and then CRUD operations are passed as jsons.

## 1. Setup the IAM role. 

Role lambda-api-gateway has been set allowing Lambda entity access to DynamoDB and CloudWatch.

![Create role](images/lambda_api_gateway.PNG)

## 2. Create the lambda function.

Create the lambda function.

![Lambda function](images/functionname.PNG)

Select role for the lambda function.

![Use existing role](images/useexistingrole.PNG)

Create the function.

![Function created](images/Function_created.PNG)

Write the code for the lambda function.

![Lambda function code](images/lambda_function_code.PNG)

## 3. Create a Test Event.

Create a test event with the following json.

![Create test event](images/testevenjson.PNG)

Run the test event.

![Test event results](images/testevent_results.PNG)

## 4. Create a table in DynamoDB.

Create table lambdaapi-gateway with id as the partition key.

![Table creation](images/createtable.PNG)

## 5. Create an API.

Select the REST API.

![Rest api select](images/restapi.PNG)

Create a new API with DynamoDBOperations as its name.

![Create api](images/createapi.PNG)

## 6. Create a child resource and integrate lambda function with its post method.

Press actions and create a new child resource DynamoDBManager.

![Create child resource](images/createresource.PNG)

Press the created resource DynamoDBManager and create a new post method.

![Create post method](images/createmethod_post.PNG)

Integrate the lambda function with the post method.

![Integrate lambda](images/saveapi.PNG)

## 7. Create a stage and copy its invocation url.

Press actions and create a stage Prod.

![Prod stage created](images/stageprod.PNG)

Copy the invocation url.

![Invocation url copied](images/copyinvokeurl.PNG)

## 8. Run Postman and test the API.

Create a new POST HttpRequest in Postman. Paste the copied invocation url and write a JSON event for a create operation.

![Postman json](images/postmantest.PNG)

Check the AWS DynamoDB table for item.

![Item added](images/itemadded.PNG)

Send scan request from Postman to receive a response with the added item.

![Postman response](images/postmanitemsreturned.PNG)
