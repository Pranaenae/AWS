Initializing the cluster using eks-ctl
![image](https://github.com/Pranaenae/AWS/assets/80820244/9a1007d4-672c-432f-8d12-3a1d4e68f230)

Information on the created cluster.
![image](https://github.com/Pranaenae/AWS/assets/80820244/b93ca8ac-5f76-4948-9253-97d3e6b61896)

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: eks-sample-linux-deployment
  namespace: eks-sample-app
  labels:
    app: eks-sample-linux-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: eks-sample-linux-app
  template:
    metadata:
      labels:
        app: eks-sample-linux-app
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/arch
                operator: In
                values:
                - amd64
                - arm64
      containers:
      - name: nginx
        image: public.ecr.aws/nginx/nginx:1.23
        ports:
        - name: http
          containerPort: 80
        imagePullPolicy: IfNotPresent
      nodeSelector:
        kubernetes.io/os: linux

Create the namespace.
![image](https://github.com/Pranaenae/AWS/assets/80820244/637d6351-0340-4633-974e-ecd89061eac1)

Create the deployment
![image](https://github.com/Pranaenae/AWS/assets/80820244/e35ae3b1-8a37-4c66-abd9-3b16f06ea833)

