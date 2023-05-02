# Lab of Getting Started with Cloud Operations

Estimating costs for the following 3-tier LAMP architecture.

![image](https://user-images.githubusercontent.com/80820244/235566817-119c5f62-e276-4376-a26e-99b90082ca55.png)

Open the pricing calculator. Press create estimate.

![image](https://user-images.githubusercontent.com/80820244/235566665-74ceae82-b9a6-4bc6-ae03-8f9afcdf90da.png)

## Add a configuration for the Elastic Load Balancer.

![image](https://user-images.githubusercontent.com/80820244/235567076-5ccd386d-2b27-452c-819f-cea6b59663cf.png)

Configure the Load Balancer Capacity Units(LCUs) as follows.

![image](https://user-images.githubusercontent.com/80820244/235567216-d182230b-0555-4101-9503-e50b93d0504e.png)

Save and add the service.

## Setting up EC2 configurations.

Set platform to linux and use to Daily Spike Traffic.

![image](https://user-images.githubusercontent.com/80820244/235567466-426a09e6-ed1d-467a-bfd7-24c02b715627.png)

Set the days as workload days and enter no. of instances for baseline and peak as 1 and 2 respectively.

![image](https://user-images.githubusercontent.com/80820244/235567618-9b0b2cbe-05c2-41dd-a43a-d9a8133b6491.png)

Set the instance type as tg4.small and the payment model as on-demand.

![image](https://user-images.githubusercontent.com/80820244/235567837-bdeb7142-469f-4db0-a4e5-19247b22a675.png)

Set EBS volume to 30 gb and storage type to gp3 (General purpose SSD)

![image](https://user-images.githubusercontent.com/80820244/235568104-fdf00b5c-6869-4d59-9efe-38c72ff8376f.png)

Setup inbound and outbound data transfer allocations.

![image](https://user-images.githubusercontent.com/80820244/235568130-af440c0f-992a-48d7-bcbe-c6a6e207c182.png)

Save and add the service.

## Add a configuration for the RDS.

Keep the default settings.

![image](https://user-images.githubusercontent.com/80820244/235568512-e3de873d-554b-47dd-ae82-b4ec4295c8e9.png)

Save and add the service.

## Review and Download the Summary.

Press view summary.

![image](https://user-images.githubusercontent.com/80820244/235568646-6340ed1b-143a-46bf-be35-3999de5429eb.png)

Export to csv

![image](https://user-images.githubusercontent.com/80820244/235568707-8209254a-fdf2-400b-8422-524f08d66851.png)

Copy public link and share the estimate. 

![image](https://user-images.githubusercontent.com/80820244/235568784-ddd5d4f1-edd4-48eb-a5a2-edb1fb4823af.png)





