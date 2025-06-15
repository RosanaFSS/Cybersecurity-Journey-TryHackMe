<p align="center">November 30, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{208}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 2023, Day 15, Machine Learning}}$$

</h1>
<p align="center">Get started with Cyber Security in 24 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas.</p>
<p align="center">Access this 🆓 TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/adventofcyber2023">Advent of Cyber 2023</a>.</p><br>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/8d077e24-767e-4ac1-83f9-808a1dc8c077">
  <img height="150px" src="https://github.com/user-attachments/assets/b2e435b4-668c-478d-a7ab-23bae2902142">

</p>

<h2>[Day 15] Machine Learning,<br>
Jingle Bell SPAM: Machine Learning Saves the Day!<a id='1'></a></h2>
<p>Over the past few weeks, Best Festival Company employees have been receiving an excessive number of spam emails. These emails are trying to lure users into the trap of clicking on links and providing credentials. Spam emails are somehow ending up in the mailing box. It looks like the spam detector in place since before the merger has been disabled/damaged deliberately. Suspicion is on McGreedy, who is not so happy with the merger.</p>

<h3>Problem Statement</h3>
<p>McSkidy has been tasked with building a spam email detector using Machine Learning (ML). She has been provided with a sample dataset collected from different sources to train the Machine Learning model.</p>

<h3>Learning Objectives</h3>
<p>In this task, we will explore:</p>

<h3>Lab Connection</h3>
<p>Before moving forward, review the questions in the connection card shown below:</p>

![image](https://github.com/user-attachments/assets/37d3ce79-5162-4279-8095-0aaa46637f4d)

<p>Deploy the machine attached to this task by pressing the green <code>Start Machine</code> button at the top-right of this task. After waiting 3-5 minutes, Jupyter will open on the right-hand side. If you cannot see the machine, press the blue "Show Split View" button at the top of the room.</p>

<h3>Overview of Jupyter Notebook</h3>
<p>Jupyter Notebook provides an environment where you can write and execute code in real time, making it ideal for data analysis, Machine Learning, and scientific research. In this room, we will perform the practical on the Jupyter Notebook.</p>

![image](https://github.com/user-attachments/assets/7aa91416-2d49-43c2-9db6-d7c37a9107cc)


<p>It's important to recall that we will need to run the code from the Cells using the run button or by pressing the shortcut Shift+Enter. Each step is explained on the Jupyter Notebook for better understanding. Let's dive into the details.</p>

![image](https://github.com/user-attachments/assets/32b521e8-47da-40cf-a7aa-03aeca59e200)


<h3>Exploring Machine Learning Pipeline</h3>
<p>A Machine Learning pipeline refers to the series of steps involved in building and deploying an ML model. These steps ensure that data flows efficiently from its raw form to predictions and insights.

A typical pipeline would include collecting data from different sources in different forms, preprocessing it and performing feature extraction from the data, splitting the data into testing and training data, and then applying Machine Learning models and predictions.</p>

![image](https://github.com/user-attachments/assets/2b062bad-a9f9-41f9-9469-b73c67c439f6)


<h3>STEP 0: Importing the required libraries</h3>
<p>Before starting with Data collection, we will import the required libraries. Jupyter Notebook comes with all the libraries we need for Machine Learning. Here, we are importing two key libraries: Numpy and Pandas. These libraries are already explained in detail in the previous task.</p>

![image](https://github.com/user-attachments/assets/59d5af85-85f6-4350-928f-e236cc3bd40f)

<p>Let’s start our SPAM EMAIL detection in the following steps:</p>

<h3>Step 1: Data Collection</h3>
<p><strong>Data Collection</strong> is the process of gathering raw data from various sources to be used for Machine Learning. This data can originate from numerous sources, such as databases, text files, APIs, online repositories, sensors, surveys, web scraping, and many others.

Here, we are using the Pandas library to load the data collected from various sources in the csv format. The dataset contains spam and ham (non-spam) emails.</p>

![image](https://github.com/user-attachments/assets/5f8343f2-40f9-4925-8815-0189d233d54e)

<p>................</p>


<h3>Step 2: Data Preprocessing</h3>

<h3>Step 3: Train/Test Split dataset</h3>

<h3>Step 4: Model Training</h3>

<h3>Step 5: Model Evaluation</h3>

<h3>Step 6: Testing the Model</h3>

<h3>Conclusion</h3>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>What is the key first step in the Machine Learning pipeline?</em><br><a id='1.1'></a>
>> <code><strong>Data Collection</strong></code>

<br>

> 1.2. <em>Which data preprocessing feature is used to create new features or modify existing ones to improve model performance?</em><br><a id='1.2'></a>
>> <code><strong>feature engineering</strong></code>

<br>

> 1.3. <em>During the data splitting step, 20% of the dataset was split for testing. What is the percentage weightage avg of precision of spam detection?</em><br><a id='1.3'></a>
>> <code><strong>0.98</strong></code>

<br>

> 1.4. <em>How many of the test emails are marked as spam?</em><br><a id='1.4'></a>
>> <code><strong>3</strong></code>

<br>

> 1.5. <em>One of the emails that is detected as spam contains a secret code. What is the code??</em><br><a id='1.5'></a>
>> <code><strong>I_Hate_Best_FestiVal</strong></code>

<br>

> 1.6. <em>If you enjoyed this room, please check out the Phishing module.</em><br><a id='1.6'></a>
>> <code><strong>No answer needed</strong></code>

<br>

![image](https://github.com/user-attachments/assets/775ad554-0c23-4650-90b9-6604be17f3b6)

<br>

![image](https://github.com/user-attachments/assets/659ece0c-3c97-453d-a88f-1552409002fb)

<br>

![image](https://github.com/user-attachments/assets/3a6a0e09-a140-4fee-b99d-bd22ba3ca701)


<br>

![image](https://github.com/user-attachments/assets/be4efc32-630b-4fe6-8948-8b6c967d79c4)


<p>Step 0: Importing the required libraries</p>

<br>

![image](https://github.com/user-attachments/assets/d119cbde-5aa1-4216-a78c-70c2688abc6e)

<br>

<p>Step 1: Data Collection<br>
I pressed [ Shift ] + [ Enter ] for the codes provided in the Jupyter Notebook.</p>

![image](https://github.com/user-attachments/assets/deaa4a43-0ac3-4cfe-b3d0-e868c3e4c18c)

<br>

![image](https://github.com/user-attachments/assets/cc7f7c54-a526-49bc-b1b7-8fe4a349f9f7)

<br>

![image](https://github.com/user-attachments/assets/88b83703-5bc4-4d40-a873-75216b118e08)
<br>

<p>Step 2: Data Preprocessing</p>

![image](https://github.com/user-attachments/assets/e96b9c26-8d1e-4b9e-bc23-26137ba3eb54)

<br>

![image](https://github.com/user-attachments/assets/925a2379-9fda-449b-9667-2ea5010b603b)

<br>

![image](https://github.com/user-attachments/assets/47790820-5fae-44b1-8987-23f29402698e)

<br>

<p>Step 3: Train/Test split dataset</p>

![image](https://github.com/user-attachments/assets/5701d304-4675-4b65-867b-d361e0b57733)

<br>

![image](https://github.com/user-attachments/assets/e8a64619-5c42-4120-a213-6e377491d628)

<p>Step 4: Model Training using Naive Bayes</p>

![image](https://github.com/user-attachments/assets/eb72d6d1-f295-4103-8258-e28200ed04a5)

<br>

<p>Step 5: Model Evaluation</p>

![image](https://github.com/user-attachments/assets/e097dbe0-da5f-43dc-bfa4-75a5176f9aff)

<br>

<p>Step 6: Testing the Model</p>

![image](https://github.com/user-attachments/assets/3df516e3-e64d-4785-9fbe-dbb060a48935)

<br>

![image](https://github.com/user-attachments/assets/8912784c-691d-440c-8c76-7a71708fe84c)

<br>

![image](https://github.com/user-attachments/assets/4ee366a3-7aea-4454-ab33-00e4a0575653)

<br>

![image](https://github.com/user-attachments/assets/95d5f5f0-04fd-458f-b7b1-e91ddac18d93)

<br>

![image](https://github.com/user-attachments/assets/4aff8bb2-1732-4a93-a845-519b07286720)

<br>

![image](https://github.com/user-attachments/assets/3ff63c8f-d726-4318-b515-aceeae00c9aa)

































<h2>Task Complete<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/6848d5b6-cba8-4104-9719-9384ec3b3e0e"> </h3>

<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/f348448a-51aa-4b11-8656-63c941c2ba96"> </h3>


<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
