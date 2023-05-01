# Deploying a high-availability WordPress website with an external Amazon RDS database to Elastic Beanstalk

![image](https://user-images.githubusercontent.com/80820244/235382899-2d9f4efb-886e-4d0e-84c8-01ee4e5bb5aa.png)

Create a MySQL database with the following attributes. Write name ebdb and fill in the username and password.


![image](https://user-images.githubusercontent.com/80820244/235383227-603f6f5a-6273-4cd0-9e24-bca6083ff589.png)

Successfully created.

![image](https://user-images.githubusercontent.com/80820244/235383463-421e16e4-7294-4291-a9dd-f3ae20754e0b.png)

View the connectivity and security details and open the security group.

Open the security group and add a new inbound rule for the SQL engine with the source as the elastic beanstalk security group.

Go the Elastic Beanstalk Console.

Configure the application details and platform.
![image](https://user-images.githubusercontent.com/80820244/235384388-54cae374-328f-47cd-9894-93c1a03382c6.png)

Configure the service access and create the beanstalk application.

![image](https://user-images.githubusercontent.com/80820244/235384462-0c7d8bc4-50d7-43fd-821f-2c6ac83e42a1.png)

![image](https://user-images.githubusercontent.com/80820244/235384857-ba8d093f-c1e8-4abd-aa12-e53980fefe6c.png)

Change the EC2 security group to the previously assigned sg.
![image](https://user-images.githubusercontent.com/80820244/235386258-61d036a2-32d2-421e-8a4c-4c6d5313520c.png)

To configure environment properties for an Amazon RDS DB instance

Enable database in the configuration of the environment.

![image](https://user-images.githubusercontent.com/80820244/235386726-313707d4-503c-4679-9cc0-665e69e04a6c.png)

Install wordpress in WSL.
![image](https://user-images.githubusercontent.com/80820244/235386775-92414315-708d-4a96-bea2-38c86a451ffc.png)

Verify the structure of the wordpress directory

![image](https://user-images.githubusercontent.com/80820244/235386829-5042e760-7b3c-4850-b7b3-712921b57b93.png)

Create a source bundle for the wordpress file.

Go to Elastic Beanstalk Console and select the upload and deploy button. Choose the created bundle and deploy the app.

![image](https://user-images.githubusercontent.com/80820244/235387357-ac1b92d3-9379-45f8-9f01-3e14eae09714.png)

![image](https://user-images.githubusercontent.com/80820244/235387594-f1d5ac5f-472c-47a3-bd2a-330db68afd19.png)

