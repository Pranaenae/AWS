Creating the Cluster.

Create an EKSClusterRole to allow management of resources such as creating load balancers, volumes, ec2, etc. for the EKS.

![image](https://github.com/Pranaenae/AWS/assets/80820244/8bee12a7-3ece-419e-8817-e1145d246d23)

Attach the role in the EKS creation wizard.

![image](https://github.com/Pranaenae/AWS/assets/80820244/13d6a5e1-d757-4b08-a97b-354beb01dff1)

Leaving VPC and security group settings the same and setting endpoint access as public endpoint access.

Create the cluster.
![image](https://github.com/Pranaenae/AWS/assets/80820244/ea810d9d-90cd-4e81-ab27-80c62eddde2a)


Provisioning a managed node type.

![image](https://github.com/Pranaenae/AWS/assets/80820244/4a9b79cf-228d-4abb-abe4-00626d7ea6ca)

Create a role for the ec2 with the following permissions.
![image](https://github.com/Pranaenae/AWS/assets/80820244/ea648240-bdaa-426c-a209-4168c13105a2)

Setup the node group.
![image](https://github.com/Pranaenae/AWS/assets/80820244/78a3be07-5c54-47d8-86df-ec94a12bcd00)

Specify the subnets.
![image](https://github.com/Pranaenae/AWS/assets/80820244/53c0ab64-3c80-4e5e-a5dc-5b25dda6d695)

Create the managed node group and update kubeconfig file.

![image](https://github.com/Pranaenae/AWS/assets/80820244/1d014f54-b87e-4747-a7c9-2e0986bb1d06)

Can see the running managed node.
![image](https://github.com/Pranaenae/AWS/assets/80820244/f42b36c9-0c7f-4e0a-ad46-e7c6b1319140)
