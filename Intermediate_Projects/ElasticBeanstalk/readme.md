# Deploying a high-availability WordPress website with an external Amazon RDS database to Elastic Beanstalk

![image](https://user-images.githubusercontent.com/80820244/235382899-2d9f4efb-886e-4d0e-84c8-01ee4e5bb5aa.png)

Create a MySQL database with the following attributes. Write name ebdb and fill in the username and password.

![image](https://user-images.githubusercontent.com/80820244/235176744-b2818ecb-6638-4dfe-8cd7-357f50a8c051.png)

![image](https://user-images.githubusercontent.com/80820244/235177583-6d61043a-ef00-49c8-8b5c-08b989ea1a08.png)

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
