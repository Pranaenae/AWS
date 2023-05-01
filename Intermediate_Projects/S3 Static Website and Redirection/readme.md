## Hosting a static website in an S3 bucket and adding redirection rules.

## Points to remember for future.

Website redirection only works in static website hosting so:

1. http://hellohello.com.s3-website.ap-south-1.amazonaws.com/docs/index.html this supports website redirection
2. the object url doesn't ie.  https://s3.ap-south-1.amazonaws.com/hellohello.com/documents/index.html Note the "s3.website" part in the url.

Go to S3 and create a new bucket.

![image](https://user-images.githubusercontent.com/80820244/235432357-394d8ebb-21e2-48d7-9ea7-0adca5ecdd18.png)

Enable the static website hosting property and setup the index and error files. 

![image](https://user-images.githubusercontent.com/80820244/235432839-e5dc2c7c-0c68-4596-ad91-7500d43cd9e1.png)

![image](https://user-images.githubusercontent.com/80820244/235432843-04ddc71d-b7db-40a0-a6d6-de0803f7d749.png)

Uncheck block all public access.

![image](https://user-images.githubusercontent.com/80820244/235432969-2d7e4964-ee60-47c8-a70b-5a2a13b996c2.png)

Confirm the changes

![image](https://user-images.githubusercontent.com/80820244/235432980-a70305ab-c435-427f-adec-9617438ccffe.png)

Generate a new bucket policy for public access.

![image](https://user-images.githubusercontent.com/80820244/235433324-91bcbb9d-fa60-47b2-996b-5f235c8059de.png)

Put the generated policy into the s3 bucket and direct the arn resource to the index file.

![image](https://user-images.githubusercontent.com/80820244/235433773-4eb7266e-095c-46b3-9f32-3f54b29fe111.png)

Create an html file with the following code.

![image](https://user-images.githubusercontent.com/80820244/235433985-bb6de56c-93e1-442b-8eec-6d4f18e9f515.png)

![image](https://user-images.githubusercontent.com/80820244/235434034-779e40fc-39a0-4b12-b671-0042663fefc8.png)

Click the static website link to view the page.

![image](https://user-images.githubusercontent.com/80820244/235434213-07d31619-3016-4728-9cc1-998d68ba8f28.png)

## Creating redirection rules.

Create a rule for a change in directories of files so that the file goes to documents directory when prefix has docs in it.

![image](https://user-images.githubusercontent.com/80820244/235435040-d9497e89-7051-49e9-9ab9-b3fa50d797fb.png)

Change the bucket policy to match the change in directories.

![image](https://user-images.githubusercontent.com/80820244/235438397-d8987afd-1e19-405c-a78d-14180980b623.png)

No docs folder

![image](https://user-images.githubusercontent.com/80820244/235438308-691b5c62-3ef9-47ce-af42-e78fa09a2210.png)

Still shows index page.

This link
![image](https://user-images.githubusercontent.com/80820244/235439449-abd751e1-0aec-448a-98d5-7f6fc81b0d85.png)
redirects to

![image](https://user-images.githubusercontent.com/80820244/235439405-7c5f27d5-9e54-4d82-85f1-d90054e20417.png)




