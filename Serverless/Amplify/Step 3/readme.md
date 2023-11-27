**Building a Backend with Lambda and DynamoDB**
To fulfill those requests, the JavaScript running in the browser will need to invoke a service running in the cloud.

Create a DynamoDB with Partition key as RideId.

![image](https://github.com/Pranaenae/AWS/assets/80820244/edb43d03-9fed-4df5-8ec4-561fa7e2c003)

![image](https://github.com/Pranaenae/AWS/assets/80820244/4ed6b03d-cbbf-47ee-abb8-510698a679e2)

Copy the ARN.

![image](https://github.com/Pranaenae/AWS/assets/80820244/ac3a9dff-0223-460b-a15e-c3f84ab34894)

create an IAM role that grants your Lambda function permission to write logs to Amazon CloudWatch Logs and access to write items to your DynamoDB table
![image](https://github.com/Pranaenae/AWS/assets/80820244/6fb7b4cc-b1e2-4c8f-a17d-2460387a56da)

LambdaBasicExecutionRole 
![image](https://github.com/Pranaenae/AWS/assets/80820244/3732030c-4b58-4333-a88b-b10116e57fb8)

Add dynamodb putitem permission to the lambdarole and add the arn.
![image](https://github.com/Pranaenae/AWS/assets/80820244/7b51a784-f8d9-4448-8bd4-f198a7d56389)

**Permission policies are attached to roles.**

![image](https://github.com/Pranaenae/AWS/assets/80820244/a8697e6c-11f9-4139-8c6c-5d3f267be488)

**Creating a Lambda Function**

![image](https://github.com/Pranaenae/AWS/assets/80820244/e6ebb046-20b7-419a-bad1-3f843b6a49cc)

Attach the created role

![image](https://github.com/Pranaenae/AWS/assets/80820244/5821b4e4-26ab-4519-9e38-eef505f05e4c)

Add the code to index.js.

![image](https://github.com/Pranaenae/AWS/assets/80820244/f315e6af-4e1e-49b6-a40e-0fc35d34c757)


