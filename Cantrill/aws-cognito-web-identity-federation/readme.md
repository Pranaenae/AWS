We will be implementing a simple serverless application which uses Web Identity Federation.
The application runs using the following technologies

    S3 for front-end application hosting
    Google API Project as an ID Provider
    Cognito and IAM Roles to swap Google Token for AWS credentials

The application runs from a browser, gets the user to login using a Google ID and then loads all images from a private S3 bucket into a browser using presignedURLs.

This advanced demo consists of 6 stages :-

    STAGE 1 : Provision the environment and review tasks
    STAGE 2 : Create Google API Project & Client ID
    STAGE 3 : Create Cognito Identity Pool
    STAGE 4 : Update App Bucket & Test Application
    STAGE 5 : Cleanup the account

Provisioned the environment using CloudFormation.

Creating authorization credentials for Google's OAuth 2.0 Server.
![image](https://github.com/Pranaenae/AWS/assets/80820244/d67eab9c-a9ad-441e-ab67-724befa931ad)

Creating the OAuth client ID.
![image](https://github.com/Pranaenae/AWS/assets/80820244/ef8e6dc6-69ea-48e9-904c-48085269b0b7)

Creating a cognito user pool.




