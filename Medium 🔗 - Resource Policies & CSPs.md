<p align="center">April 26, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{355}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/13f4c27b-45b5-4246-be5f-de6d1805ed82" alt="streak"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Resource Policies & CSPs}}$$</h1>
<p align="center"><em>Learn how AWS resources can have their own permissions.</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/resourcepoliciesscps">here</a>.</p>


<p align="center"> <img width="1000px" src=""> </p>



<br>
<br>

<h2>Task 1 . Other Policy Types</h2>

<p>While 80% of the time when working with AWS you'll be using IAM Policies, there are two other types of policies you need to know about. They use the same statement structure as an IAM Policy but are attached to resources or accounts to affect how access is authorized.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Let's get started...</em><br><a id='1.1'></a>
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
<br>

<h2>Task 3 . Resource Policies</h2>

<p>IAM Policies are attached to a specific Principal and define the resources the Principal can act on whereas Resource Policies are attached to a resource and define the Principals that can act on the resource.  Many resource types can have Resource Policies, and resource policies are how things become public in AWS.<br><br>

For example, you can attach Resource-based Policies to:<br>

- S3 Buckets<br>
- KMS Keys<br>
- SQS Queues<br>
- SNS Topics<br>
- AWS Lambda<br>
- Secrets Manager Secrets<br>
- IAM Roles - yes, an assume role trust policy is a resource policy since it defines the Principal who can act.</p>

<p>The command to apply a resource policy varies based on the service. S3 buckets are one of the most common use cases for Resource Policies. For demonstration purposes, we've created a public S3 bucket in another TryHackMe account. That bucket is creatively named "tryhackme-public-bucket". The Bucket Policy for the bucket is:</p>

<br>

```bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Make Object Readable",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::tryhackme-public-bucket/*"
    },
    {
      "Sid": "Make Bucket Attributed World Readable",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "s3:Get*",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::tryhackme-public-bucket"
    }
  ]
}
```

<br>

<p>In the case of S3, there are two AWS resources involved: the Bucket and the Objects in the bucket. The first statement allows anyone ("Principal": "*") to GetObject on all the objects in the bucket (arn:aws:s3:::tryhackme-public-bucket/*). The second statement applies only to the bucket itself (arn:aws:s3:::tryhackme-public-bucket) and allows anyone to get the attributes of the bucket (s3:Get*), and to list the objects in the bucket (s3:ListBucket).<br><br>

Give it a try. Run this command from your attack box or cloud-shell session:</p>

<br>

```bash
aws s3api get-bucket-policy-status --bucket tryhackme-public-bucket
```

<br>

<p>Now try and list the files in the bucket:</p>

<br>

```bash
aws s3 ls tryhackme-public-bucket
```

<br>

<p>Resource Policies also apply to whom can invoke a Lambda function. We'll cover Lambda in a future module, but try executing this Lambda, and then look at the output file:</p>

<br>

```bash
aws lambda invoke --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time time && cat time | jq -r
```

<br>

<p>Now try looking at the policy for that function:</p>

<br>

```bash
user@machine$ aws lambda get-policy --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time --query Policy --output text | jq
{
  "Version": "2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "THM-CommonResources-PublicLambdaGetPolicyPermission-1H4ZWNO1H6SFF",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "lambda:GetPolicy",
      "Resource": "arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time"
    },
    {
      "Sid": "THM-CommonResources-PublicLambdaInvokePermission-1KE9NRSHANU6U",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-ad4l00k0ts"
        }
      }
    }
  ]
}
```

<br>

<p>As you can see, the resource policy for this function allows anyone to run lambda:GetPolicy, and all members of the AWS Organization o-ad4l00k0ts to run lambda:InvokeFunction.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>Try running the s3api command "get-bucket-ownership-controls" against the tryhackme-public-bucket. What is the ObjectOwnership value set to?</em>Hint : <em>The command you need is: aws s3api get-bucket-ownership-controls --bucket tryhackme-public-bucket</em><br><a id='3.1'></a>
>> <strong><code>__________________</code></strong><br>
<p></p>

<br>

<br>

> 3.2. <em>ry invoking the Lambda function "TryHackMe-quote" in the same 019181489476 Account. What's the quote returned from the function?</em>Hint : <em>The command you need is: aws lambda invoke --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-quote flag ; cat flag | jq -r</em><br><a id='3.2'></a>
>> <strong><code>__________________</code></strong><br>
<p></p>

<br>
