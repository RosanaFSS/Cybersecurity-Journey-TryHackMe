
<p align="center">March 201 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{319}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/fe489f22-d5c5-4702-a1aa-5d06a98c270f"></p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{[ Day 11 ] - Advent of Cyber 3 (2021)}}$$
</h1>
<p align="center">Get started with Cyber Security in 25 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas. It is classified as an easy-level walkthrough, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/adventofcyber3">Advent of Cyber 3 (2021)</a>.</p>
                                                              
<p align="center"> <img width="900px" src=""> </p>

<br>

<p align="center"> <img width="900px" src=""> </p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Where are The Reindeers? | Networking}}$$
</h1>

<p>Before we begin, we suggest that you start the attached Machine and the AttackBox as you will need to use these resources to answer the questions at the end.<br>

McDatabaseAdmin came rushing into the room and cried to McSkidy, “We’ve been locked out of the reindeer schedule - how will Santa’s transportation work for Christmas?” The grinch has locked McDatabaseAdmin of his system. You need to probe the external surface of the server to see if you get him his access back.<br>

MS SQL Server is a Relational Database Management System (RDBMS). One simple way to think of a relational database is a group of tables that have relations. To gain a rough understanding of relational databases work, consider a shop's database with the following three tables:<br>
- Electronic Items<br>
- Customers<br>
- Invoices<br>

Each item in the Electronic Items table has:<br>
- ID<br>
- Name<br>
- Price<br>
- Quantity<br>

Each item in the Customers table has its own attributes as well:<br>
- ID<br>
- Name<br>
- Email<br>
- Phone<br>

Finally, the Invoices table will refer to a customer and one or more electronic items. The Invoice table will refer to an “entity” from another table using its ID. This way, we only need to have the customer details and electronic item details written once instead of copying them to each new invoice. This case is a simplified example of a relational database. The figure below shows how the three tables are related.</p>


![image](https://github.com/user-attachments/assets/0b73689e-22b7-4276-995b-12b6b1f25296)

<p>The transportation schedule is in the reindeer database. However, McDatabaseAdmin can no longer log in to his system after the grinch changed the system password. Let’s see how we can help. Make sure you have started the attached Machine along with the AttackBox. Give them a few minutes to fully start before proceeding to answer the following questions.</p>


![image](https://github.com/user-attachments/assets/0741f2ce-5ddc-47d7-994b-ee68eb3dd7cf)

<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>You decided that the first step would be to check the running services on <code>10.10.238.97</code>. You resort to yesterday’s tool, Nmap.<br>Knowing that <code>10.10.238.97</code> is a MS Windows system, you expect it to not respond to ping probes by default; therefore, you need to add <code>-Pn</code> to your <code>nmap</code> command to perform the scan. <br>This instructs Nmap to skip pinging the target to see if the host is reachable. Without this option, Nmap will assume the target host is offline and not proceed with scanning.<br>There is an open port related to MS SQL Server accessible over the network. What is the port number?</em>
<a id='1.1'></a>
>> <code><strong>________</strong></code><br><br>


<br>

<p>Knowing the MS SQL Server is running and accessible over the network, we want to check if our username and password are still valid. Using the AttackBox terminal, we will use the command <code>sqsh</code> (pronounced skwish), an interactive database shell.<br>

A simple syntax would be sqsh -S server -U username -P password, where:<br>

- <code>-S server</code> is used to specify the server, for example <code>-S 10.10.238.97</code><br>
- <code>-U username</code> is used to provide the username; for example, <code>U sa</code> is the username that we have enabled.<br>
- <code>-P password</code> lets us specify the password.<br><br>
Let’s try to run, <code>sqsh -S 10.10.238.97 -U sa -P t7uLKzddQzVjVFJp</code></p>


> 1.2. <em>If the connection is successful, you will get a prompt. What is the prompt that you have received? </em><a id='1.2'></a>
>> <code><strong>McSkidy:Christmas2021</strong></code><br><br>

<br>

<p>McDatabaseAdmin told us the database name is <code>reindeer</code> and it has three tables:<br>
- <code>names</code><br>
- <code>presents</code><br>
- <code>schedule</code><br>

To display the table <code>names</code>, you could use the following syntax, <code>SELECT * FROM table_name WHERE condition</code>.<br>
- <code>SELECT *</code> is used to return specific columns (attributes). <code>*</code< refers to all the columns.<br>
- <code>FROM table_name</code>to specify the table you want to read from.<br>
- <code>WHERE condition</code> to specify the rows (entities).<br><br>

In the terminal below, we executed the query, <code>SELECT * FROM reindeer.dbo.names;</code>. This SQL query should dump all the contents of the table <code>names</code> from the database <code>reindeer</code>. Note that the <code>;</code> indicates the end of the SQL query, while <code>go</code> sends a SQL batch to the database.</p>

![image](https://github.com/user-attachments/assets/9ccfad71-cf53-49c6-9a1a-6f3419f57951)

<br>


> 1.3. <em>We can see four columns in the table displayed above: id, first (name), last (name), and nickname. What is the first name of the reindeer of id 9? </em>Hint : The query won't be executed unless you type "go" on a separate line and hit the Enter/Return key as shown in the example terminal.<a id='1.3'></a>
>> <code><strong>_________________</strong></code><br><br>

<br>


> 1.4. <em>Check the table <code>schedule</code>. What is the destination of the trip scheduled on December 7? </em>Hint : You need to execute a query similar to the query displayed in the previous question, but for the table schedule.<a id='1.4'></a>
>> <code><strong>_________________</strong></code><br><br>

<br>

> 1.5. <em>Check the table <code>presents</code>. What is the quantity available for the present “Power Bank”? </em>Hint : You need to execute a query similar to the query displayed in the previous question, but for the table presents.<a id='1.5'></a>
>> <code><strong>_________________</strong></code><br><br>

<br>

<p>You have done fantastic work! You have helped McDatabaseAdmin retrieve the schedule! Now, let’s see if we can run MS Windows commands while interacting with the database. Some MS SQL Servers have <code>xp_cmdshell</code> enabled. If this is the case, we might have access to something similar to a command prompt.<br>

The command syntax is <code>xp_cmdshell 'COMMAND';</code>. Let’s try a simple command, <code>whoami</code>, which shows the user running the commands. In the terminal output below, after connecting to MS SQL Server, we tried <code>xp_cmdshell 'whoami';</code>, and we can see that the user is <code>nt service\mssqlserver</code>. This means that any command we pass to <code>xp_cmdshell</code> will run as <code>nt service\mssqlserver</code>.</p>

![image](https://github.com/user-attachments/assets/850d133b-633b-4f8d-8368-543c00c011c3)


<p>We can run other commands that we can execute on the MS Windows command line. For example, we can use <code>dir</code> to list files and directories and <code>type filename</code> to display the contents of a file. Consider the example in the terminal window below where we reveal the contents of the text file <code>WindowsUpdate.log</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/9c123480-6ca7-40a1-a526-113d9c24ab29)

<br>


> 1.6. <em>There is a flag hidden in the <code>grinch</code> user's home directory. What are its contents?<a id='1.6'></a>
>> <code><strong>_________________</strong></code><br><br>

<br>

> 1.7. <em>Congratulations, the flag you have recovered contains the password of <code>McDatabaseAdmin!</code> In this task, we learned how to use <code>sqsh</code> to interact with a MS SQL Server. We learned that if <code>xp_cmdshell</code> is enabled, we can execute system commands and read the output using <code>sqsh</code>.<a id='1.6'></a>
>> <code><strong>_________________</strong></code><br><br>

<br>


