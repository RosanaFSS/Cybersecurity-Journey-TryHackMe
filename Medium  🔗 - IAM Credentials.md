<p align="center">April 26, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{355}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/59a3f9a9-09da-4563-883c-95bc2adafea3" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/13f4c27b-45b5-4246-be5f-de6d1805ed82" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{IAM Credentials}}$$</h1>
<p align="center"><em>Learn how IAM handles credentials for authentication to AWS APIs</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/iamcredentials">here</a>.</p>


<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/444af653-20e3-4b27-b56e-83e63fd51af7"> </p>



<br>
<br>

<h2>Task 1 . Introduction to IAM Authentication </h2>

<p>Every call to AWS is authenticated in some form. For the API, this is typically done through Request Signing. However, when using the AWS console you log in using a more traditional username/password combination. In this room, we'll dive into the various ways you authenticate to AWS and best practices for securing your AWS account and passwords.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Let's get started.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Accessing the Environament</h2>

<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>Generate environment or set up your credentials.</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/b762b38f-96f5-451a-8aa8-fee786ea111d)

<br>
<br>

<h2>Task 3 . Root Password</h2>

<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>Certify you are not a Robot.</em><br><a id='3.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<p>I checked. I did not access AWS Console as root.</p>

<br>
<br>

<h2>Task 4 . IAM Login Profile</h2>

<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>What’s the minimum number of numbers required in the password policy?</em>Hint : <em>Note that only three of the four types (uppercase, lowercase, numbers and special characters) are required.</em><br><a id='4.1'></a>
>> <strong><code>0</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/33d235f0-73c4-4ba8-898b-28904e6df8b7)



<br>
<br>

<h2>Task 5 . AWS API Access Key</h2>

<p>[ ... ]</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>How many active IAM Access Keys does the TryHackMe-IAM-User have?</em><br><a id='5.1'></a>
>> <strong><code>1</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/3d232999-882d-4674-aeea-68baeccdd67f)

<br>
<br>

<h2>Task 6 . MFA in AWS and Best Practices around Credentials</h2>

<p>AWS supports using a Virtual MFA (TOTP), Hardware token, or U2F Security Key (the last two links are the Amazon Retail pages for the products). MFA can be applied to either an IAM User or the Root User. When using an identity federation to assume an IAM Role, implementing MFA is the responsibility of the identity provider.<br><br>

When MFA is applied to an IAM User or the Root User, AWS will require the second factor when performing a console login. MFA is not required by default when making an AWS API call using access keys. However, IAM Policies can implement conditions to require MFA. To do this, the user must first request temporary credentials and pass the MFA token as part of the request. The new temporary credentials will have a flag that says MFA was present when they were created, and the IAM Policy Condition will be satisfied.<br><br>

Mishandling of AWS Credentials is the primary way an AWS Account is compromised. There are several best practices for handling AWS Access Keys that you should follow:<br>

1. Avoid using IAM Users where ever possible. Many cloud providers offer the ability to use SAML or OIDC to get session credentials for AWS API access. <br>
2. NEVER commit an access key to a source code repository (GitHub, GitLab, etc.). GitHub will scan all commits to public repositories for any AKIA and notify AWS, who will promptly disable the key. But even private repositories can be compromised, and attackers know to look for the AKIAs in source code and configuration files.<br>
3. Rotate Access Keys often. When creating an access key, you have the option to download the credentials as a CSV file. These CSV files collect in Download folders. If machines are not properly cleansed when decommissioned or a laptop is left in a taxi cab, these credentials can find themselves for sale on the dark web.<br>
4. Use MultiFactor Authentication for access to the Root and IAM Users.<br><br>

Many of the IAM Identifiers can be useful from a reconnaissance perspective. For example, AKIA strings, while not sensitive, can be used to identify an AWS Account with the following command:</p>

<br>

```bash
aws sts get-access-key-info --access-key-id AKIAEXAMPLE
```

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>Substitute the AKIAEXAMPLE in the above command with the Access Key ID in your Cloud Credentials and run the command to see if it matches your AWS Account ID.</em><br><a id='6.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/8d3c0165-2963-4eb2-a04c-5ef77c065bfa)

<br>

> 6.2. <em>What account ID does "AKIASTZ6PFXLJW3RQWXC" belong to?</em><br><a id='6.2'></a>
>> <strong><code>179982773718</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5e3e6a1e-b890-406f-b9c6-cd418e7a025d)

<br>
<br>

<h2>Task 7 . How services get credentials</h2>
<p>As we noted in the section on IAM Roles, AWS Services can also leverage temporary credentials to access resources in your account. The Role’s Assume Role Trust document must specify the service as a Principal allowed to assume the role.<br><br>

The mechanics for getting those credentials vary depending on the service. But when you’re attacking or defending cloud infrastructure, knowing how to get these credentials is vital.<br><br>

The Primary way to get credentials for a role is with the AWS STS AssumeRole API Call or the aws sts assume-role AWS CLI command.<br><br>

If you’re using an EC2 Instance, there is a special network address in the hypervisor you can use to request temporary credentials for the EC2 Instance Profile. It was through this Instance MetaData Service (IMDS) that the Capital One breach was executed. In a future room, we will show you how a curl to 169.254.169.254 will present temporary AWS Access Keys. As a response to the Capital One incident and outcry from the cloud security community, AWS released the IDMSv2 which requires a two-step session based method.<br><br>

If your code is running in AWS Lambda, the Access Key ID, Secret Access Key, and Session Token are available as environment variables.<br><br>

For ECS Containers, there is another IP address you can curl for the container’s credentials</p>

<br>

```bash
curl 169.254.170.2$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI
```

<br>

<p>The $AWS_CONTAINER_CREDENTIALS_RELATIVE_URI environment variable is populated if IAM Roles for Tasks is configured.<br><br>

Finally, you can get temporary credentials from your CloudShell with this simple command:</p>

<br>

```bash
curl $AWS_CONTAINER_CREDENTIALS_FULL_URI -H "X-aws-ec2-metadata-token: $AWS_CONTAINER_AUTHORIZATION_TOKEN" 
```

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 7.1. <em>Use the CloudShell and the curl command above to download temporary credentials, what is the JSON key that begins with "E"?</em><br><a id='7.1'></a>
>> <strong><code>Expiration</code></strong><br>
<p></p>

<br>

```bash
curl $AWS_CONTAINER_CREDENTIALS_FULL_URI -H "X-aws-ec2-metadata-token: $AWS_CONTAINER_AUTHORIZATION_TOKEN" 
```

<br>

![image](https://github.com/user-attachments/assets/963955ce-9eb1-4ab1-baa0-e1c8f2a72041)

<br>

> 7.2. <em>When using temporary credentials, what are the first four letters of the AccessKeyId?</em><br><a id='7.2'></a>
>> <strong><code>AKIA</code></strong><br>
<p></p>

<br>

<p>The first four letters of AWS temporary credentials are <code>ASIA</code>. These letters indicate that the credentials were generated by the AWS Security Token Service (STS) and are therefore temporary, unlike long-lived access keys which begin with <code>AKIA</code>.</p>

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/4708bc01-8372-4120-8c77-40406545580e"><br>
<img width="900px" src="https://github.com/user-attachments/assets/63d14c5f-fd0e-4623-bdad-cb6f64d148a0"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 26, 2025    | 355      |     254ᵗʰ    |      6ᵗʰ     |     50ᵗʰ    |     2ⁿᵈ    |  97,337  |    685    |     59    |

</div>

<br>


<p align="center"> Global All Time:  254ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/2cef33ec-dc0f-4855-b50f-bfb5ffd7e5bd"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/18f88e50-b8de-4f08-ae7b-a09726071891"> </p>

<p align="center"> Global monthly:    50ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/4c4bbaa8-b8fc-43ed-99ea-9286dd043042"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/6b8e50f6-e589-4524-bd86-ebfeabe6e250"> </p>

<br>
<br>

<p align="center"> Weekly League:    5ᵗʰ Gold<br><br><img width="1000px" src="https://github.com/user-attachments/assets/f25d6184-051d-4982-b8f7-b84796876422"> </p>

<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/jcfarris">jcfarris</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
