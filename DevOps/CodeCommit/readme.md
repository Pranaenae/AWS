# Migrating git repository to CodeCommit

Setup initial codecommit repository.

Attach the AWSCodeCommitPowerUser policy to the designated IAM user.

![image](https://user-images.githubusercontent.com/80820244/235858016-55bf58cb-acf8-4929-a2e7-a75c07686e53.png)

Generate GitHub credentials for the IAM user.
![image](https://user-images.githubusercontent.com/80820244/235885922-56855c2f-db3c-49fd-b6e5-7c2076778f20.png)


Copy the clone url and clone it into a folder my-demo-repo.

![image](https://user-images.githubusercontent.com/80820244/235885638-a4d9caa8-e7d8-4b2e-8932-d745083638ac.png)

Enter the generated GitHub credentials.

![image](https://user-images.githubusercontent.com/80820244/235885811-17f08af5-7a8f-404c-b893-87854847e6a2.png)

Push the github folder to CloudCommit with the git push cloned_url --all command.

![image](https://user-images.githubusercontent.com/80820244/235887483-733051cf-ab6e-46d9-a6ef-527634e349b2.png)
