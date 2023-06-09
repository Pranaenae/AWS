# Create a Continuous Distribution Pipeline through AWS.

Create the Elastic Beanstalk environment first.
![image](https://user-images.githubusercontent.com/80820244/235899560-1fd4302e-9799-49e6-8084-b86e3a6d1095.png)

Choose PHP as the platform.

![image](https://user-images.githubusercontent.com/80820244/235899798-472a8e33-a153-416c-96d0-babea267350c.png)

Setup the service access.

![image](https://user-images.githubusercontent.com/80820244/235899942-cad087cc-f566-4354-8c4d-ce2bde29f80f.png)

Launch the environment.

![image](https://user-images.githubusercontent.com/80820244/235902045-ca75c241-37fb-410d-9536-27456f3827c4.png)

Fork the sample code.

![image](https://user-images.githubusercontent.com/80820244/235902479-5b0f1742-31fe-4745-ab82-d6a470bed831.png)


Open the AWS CodePipeline.

Create a new Pipeline.

![image](https://user-images.githubusercontent.com/80820244/235903091-08412e34-2b1a-485a-a26e-0b8d542bd7d2.png)

Choose Github(version 2) and connect to GitHub.

![image](https://user-images.githubusercontent.com/80820244/235904659-68666a58-33a4-4797-be93-f7b7fa92064a.png)

Install a new GitHub App.

![image](https://user-images.githubusercontent.com/80820244/235904858-f73f1871-9650-46a3-aea0-18770581e21a.png)

Only select the forked repository.
![image](https://user-images.githubusercontent.com/80820244/235905844-3dec1033-f3fd-44c1-8338-d2e894d60b66.png)


Connect to GitHub.

![image](https://user-images.githubusercontent.com/80820244/235904951-b7c9a33f-3100-4b13-af80-3928482bd2c6.png)

Select the repository name, branch name and the output artifact format.

![image](https://user-images.githubusercontent.com/80820244/235906426-5eb4db39-645d-4045-acb8-008cbd3fcd31.png)

Select the following deployment attributes.

![image](https://user-images.githubusercontent.com/80820244/235906700-702bf332-f2ad-4468-981a-7fa5129c262c.png)

Review and activate your pipeline.

![image](https://user-images.githubusercontent.com/80820244/235907281-92eda0c0-9350-4c69-9aa5-e19a5c35882d.png)

![image](https://user-images.githubusercontent.com/80820244/235907363-adf98c7d-baf4-4c9f-ac53-ef0c2fb7c103.png)

Go the environment and click on the domain.

![image](https://user-images.githubusercontent.com/80820244/235907838-a51f57b3-2630-41e2-9b5e-d1cb70c10644.png)

## Commit a change and update your app.

Edit the index.html file in the forked repo.

![image](https://user-images.githubusercontent.com/80820244/235908674-0abdd915-a81a-4a09-b286-e6980e2083be.png)

Replace the heading on line 30.

![image](https://user-images.githubusercontent.com/80820244/235908886-a951dbd6-ce34-468d-a754-c1c9ee69721d.png)

Commit the changes.

Deployment in progress..

![image](https://user-images.githubusercontent.com/80820244/235909141-199d2370-74bd-4053-8ec1-08669e864d68.png)

Changes have been made. Let's go boyssss.

![image](https://user-images.githubusercontent.com/80820244/235909685-d9cb0a88-6588-4de8-9758-f578476fc9da.png)

Cleanup the resources.
