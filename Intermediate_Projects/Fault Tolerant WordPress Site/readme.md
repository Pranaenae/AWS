# Create a fault tolerant wordpress site.

## Setting up the required resources.

Creating IAM role to allow EC2 instances to connect to S3.

![image](https://user-images.githubusercontent.com/80820244/235603080-279596dd-fe02-4c8f-8547-d899e3ebe5fe.png)

Adding S3 full access.

![image](https://user-images.githubusercontent.com/80820244/235603314-c3e9eb6a-5b70-4085-b39f-138e92dc4117.png)

Provide a name for the role and create it.
![image](https://user-images.githubusercontent.com/80820244/235604538-bc5879f3-ed97-4b76-812c-5d92bd42c39a.png)


Create a security group for the WebTier that accepts traffic from SSH, HTTP and HTTPS.

![image](https://user-images.githubusercontent.com/80820244/235604554-cce74a9d-2b27-4877-8d5a-60d720b07c44.png)

Add a new database security group that accepts SQL/ Aurora traffic from the created security group for the WebTier.

![image](https://user-images.githubusercontent.com/80820244/235605594-aa0ed1b8-79fb-4109-8d0d-56bd93d60753.png)


Create a new s3 bucket with public read access.

![image](https://user-images.githubusercontent.com/80820244/235606362-3f746656-84b4-4fee-9d2b-f77c83ed77a6.png)

Enable read access in the Acl.

![image](https://user-images.githubusercontent.com/80820244/235606540-f4a53c4a-66cd-4a68-9338-6342dd9d441f.png)


Create a network Load Balancer.

![image](https://user-images.githubusercontent.com/80820244/235626009-9465c495-2df8-4036-95f4-655d671da8c4.png)


Create target groups for the load balancers.
![image](https://user-images.githubusercontent.com/80820244/235625934-522fd0d1-6b6e-4bc1-ae0f-172e80ccc6d7.png)


![image](https://user-images.githubusercontent.com/80820244/235607805-bd6dc8c1-204a-440a-8d89-7290beb005d2.png)

Select the subnets.

![image](https://user-images.githubusercontent.com/80820244/235626106-0c443d78-99d1-4f82-9a96-cd0a40fc39bf.png)

Setup target.

![image](https://user-images.githubusercontent.com/80820244/235626236-60f2d42b-a20e-47ff-94c1-dd5c7af29d2d.png)


Create the load balancers ProjectLB and ProjectReadLB.

![image](https://user-images.githubusercontent.com/80820244/235626326-9cee2ea1-6569-4e43-8c9a-1e755fef8558.png)

Create a cloudfront distribution for the created s3 bucket.

![image](https://user-images.githubusercontent.com/80820244/235627412-334f50a8-5c0e-438f-9334-7667b921d765.png)


