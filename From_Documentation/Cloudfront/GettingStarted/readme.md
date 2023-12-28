Create an s3 bucket, connect it to route 53 and upload the static files to it.

![image](https://github.com/Pranaenae/AWS/assets/80820244/6100c6fc-0b73-4ebc-89de-c7966529d199)

Create the distribution with s3 as origin.

![image](https://github.com/Pranaenae/AWS/assets/80820244/c6d02799-1b14-4500-8543-b2a1ac363817)


Create the ssl certificates and add the cname records to route53. Validate with DNS validation.

![image](https://github.com/Pranaenae/AWS/assets/80820244/219b67bb-374d-4554-8460-b6c3f782cb47)

![image](https://github.com/Pranaenae/AWS/assets/80820244/143d6e44-b57e-4e95-aaa5-7771aae14ead)

Create cloudfront distribution and alias record to point domain name to cloudfront.

![image](https://github.com/Pranaenae/AWS/assets/80820244/9151f666-d6f5-41e5-b4c3-4bef8725ed12)


![image](https://github.com/Pranaenae/AWS/assets/80820244/61ae4711-235b-4b9e-9b21-b3ce4ed0027d)
