In this module, you will use Amazon API Gateway to expose the Lambda function you built in the previous module as a RESTful API. This API will be accessible on the public Internet. It will be secured using the Amazon Cognito user pool you created in the previous module. Using this configuration, you will then turn your statically hosted website into a dynamic web application by adding client-side JavaScript that makes AJAX calls to the exposed APIs.

Create REST API.
![image](https://github.com/Pranaenae/AWS/assets/80820244/c7cd529b-80b5-480d-a490-3823a495ab88)

Create the authorizer for the API.
![image](https://github.com/Pranaenae/AWS/assets/80820244/2102ed93-0ea5-4b35-8054-8d34950fdc7f)

Create a new method for the /ride.
![image](https://github.com/Pranaenae/AWS/assets/80820244/0a6da1e9-fff6-4605-a700-fec569e9a263)

Add the authorizer.
![image](https://github.com/Pranaenae/AWS/assets/80820244/a0c244e7-6b30-452f-91f4-04be8438038b)

Deploy the API with prod stage.
![image](https://github.com/Pranaenae/AWS/assets/80820244/e893f48b-9e92-4033-b9c8-3561e6ab30c5)

Add the invoke url of the API Gateway to the config.js file.
![image](https://github.com/Pranaenae/AWS/assets/80820244/3a53ff8c-9682-4392-8dee-8bce4bdf2cd3)

Requesting the unicorn.
![image](https://github.com/Pranaenae/AWS/assets/80820244/11a9a901-898b-490b-b208-be1c4f19b795)

Step 4 Completed.
