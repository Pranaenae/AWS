# Deploy Docker Containers on Amazon Elastic Container Service

## Configuring and creating the container and cluster.

Go to the Amazon ECS and press Get Started.

![image](https://user-images.githubusercontent.com/80820244/236460370-9cbdb808-00b6-46e4-b222-8800197c5f89.png)

In the Container definition field, select sample-app.
![image](https://user-images.githubusercontent.com/80820244/236460595-283da0b3-cea2-45f8-8701-d8816d2f2d13.png)

Review the default values and choose Next.
![image](https://user-images.githubusercontent.com/80820244/236461329-3481a0e5-b107-473b-922e-8286c3b7a965.png)

Select the application load balancer and press Next.  
![image](https://user-images.githubusercontent.com/80820244/236461567-003159ad-aca7-476b-a083-08984349f3be.png)

Configure your cluster.

![image](https://user-images.githubusercontent.com/80820244/236461986-0fe58249-309f-4920-b802-8cdd2b9951b1.png)

Review and choose create.
![image](https://user-images.githubusercontent.com/80820244/236462681-4b272d49-6605-4d40-855d-4d23f1240f7a.png)


## Open the sample application.

On the sample-app-service page, select the Details tab and select the entry under Target Group Name. 
![image](https://user-images.githubusercontent.com/80820244/236463014-f24b60c7-9dcd-44a0-bd37-5b5d38839d5b.png)

On the Target groups page, select the target group name. 
![image](https://user-images.githubusercontent.com/80820244/236463157-3dd78363-a9fa-4079-9ce3-d7816ba422ea.png)

In the Details section, choose the Load balancer link. 
![image](https://user-images.githubusercontent.com/80820244/236463383-aa0aab79-8fb1-4cc7-87b2-6449212e93f9.png)

copy the DNS name to your clipboard.

![image](https://user-images.githubusercontent.com/80820244/236463781-cce8ebb6-937f-4917-aa75-6de0fd9c9b30.png)

Paste the link to view the app.

![image](https://user-images.githubusercontent.com/80820244/236463990-b510eba6-46c6-4c0a-80a0-8feafb60bbb4.png)


