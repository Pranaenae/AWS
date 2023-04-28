
# First Lambda Program

## **1. Create Lambda program.**

Open Lambda Dashboard. 

Click on select blueprint.

![Select a blueprint](images/Blueprint.PNG)

Choose the python version of the hello world blueprint and provide a name to the function.

![Python helloworld](images/python_hello.PNG)

Assign a basic role to lambda function.

![Assign role to lambda function](images/assignrole.PNG)

Create the function.

## **2. Configure the test event**.

![Configure test](images/configuretest.PNG)

Create new test event helloworld_event and replace "value1" with "hello-world"

![Create new test event](images/createevent.PNG)

Click Test.
Event tested and hello-world output received from the lambda code.

![Output from test](images/outputfromtest.PNG)

## **3. Viewing the metrics using CloudWatch**

Invoke the function a few more times.

Monitor the results.

![Results using cloudwatch](images/monitor.PNG)

## **4. Deleting the lambda function**

![Deleting the lambda](images/deletelambda.PNG)

