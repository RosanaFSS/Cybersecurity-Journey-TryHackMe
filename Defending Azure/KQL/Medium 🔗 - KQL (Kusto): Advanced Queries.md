<h1 align="center"><a href="https://tryhackme.com/room/kqlkustoadvancedqueries">KQL (Kusto): Advanced Queries</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; KQL</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b018e5b8-9714-4fd9-ac69-92101e4252d7"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2025%2C%20APR%2028-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>
<br>


<h2>Task 1 . Introduction </h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>I am ready to go advanced!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Using the Join Operator </h2>
<p>[ ... ]</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>Which join flavor returns all the records from the left table and only matching values from the right table?</em><br><a id='2.1'></a>
>> <strong><code>Kind=leftouter</code></strong><br>
<p></p>

<br>

> 2.2. <em>Which join flavor contains a row in the output for every matching row combination from both tables?</em><br><a id='2.1'></a>
>> <strong><code>Kind=inner</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . Using the Union Operator</h2>
<p>[ ... ]</p>

<h3>Combining Two Tables</h3>

![image](https://github.com/user-attachments/assets/c158cf56-2a02-4f7e-a703-44dc0a7500fc)


<br>

<h3>Combining Single Columns From Different Tables</h3>

![image](https://github.com/user-attachments/assets/b6e0e06b-97da-4eb7-991c-135a2519fa3f)


<br>

<h3>Combining Multiple Columns From Different Tables</h3>

![image](https://github.com/user-attachments/assets/a4d58503-6455-44df-9818-aa5fcdb7f6df)



<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>Can the union operator return all rows from both tables? (Yea/Nay)</em><br><a id='3.1'></a>
>> <strong><code>Yea</code></strong><br>
<p></p>

<br>

> 3.2. <em>Run the "Combining Multiple Columns From Different Tables" query and modify the time range. What is the threat status detail?</em>Hint : <em>Check the ThreatStatusDetails</em><br><a id='3.1'></a>
>> <strong><code>Threat Status is currently not supported in MDATP</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/90609c91-6c31-46d5-a0d4-ee0858ca389f)

<br>
<br>

<h2>Task 4 . Using the Project Operator</h2>
<p>[ ... ]</p>

<h3>Project Specific Columns</h3>

<br>

<h3>Using "Project-Keep" To Select What Columns To Return</h3>

<br>

<h3>Using "Project-Away" To Discard Columns From the Output</h3>
<p>The query below retrieves the SecurityEvent table for machines for the past 5 days and removes the columns defined.</p>


![image](https://github.com/user-attachments/assets/656add3f-8bb5-4ee6-8744-f457856a32df)

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 4.1. <em>Which project operator sets the column order in the resulting output?</em><br><a id='4.1'></a>
>> <strong><code>project-reorder</code></strong><br>
<p></p>

<br>

> 4.2. <em>Run the "Combining Multiple Columns From Different Tables" query and modify the time range. What is the threat status detail?</em>Hint : <em>Check the ThreatStatusDetails</em><br><a id='4.1'></a>
>> <strong><code>Yea</code></strong><br>

<br>
<br>

<h2>Task 5 . Using the Extend Operator</h2>
<h3>Extend Operator</h3>
<p>By using the extend operator, you can create newly calculated columns in a query's output. However, unlike the project operator, which can also rename and remove columns, the extend operator retains all existing columns and appends the new columns to the result.</p>

<p>[ ... ]</p>

<h3>Using Extend To Create a New Calculated Column (TimeSinceReboot)</h3>

![image](https://github.com/user-attachments/assets/56373499-4f03-42d7-bae7-33e237dadd79)

<br>

<h4>Creating a New Calculated Column With Values</h4>
<p>This query adds a new calculated column, EventCategory, and populates the eventID 4624 as logon and 4634 as logoff, while other event IDs are treated as others.</p>

![image](https://github.com/user-attachments/assets/660decf4-9790-47db-81e5-93c1f11a87de)

<br>

<h3>Using Extend To Calculate Free Disk Spaces</h3>
<p>The query below uses the extend operator to create a new calculated column called FreeSpaceinGB and input the value of the CounterValue column when converted to gigabytes by dividing its value by 1000.
</p>

![image](https://github.com/user-attachments/assets/3fe7f3ec-64fc-4236-953c-d97d38ed3d21)

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>Run the "Using Extend To Calculate Free Disk Spaces" query mand modify the time range. What new column is created?</em><br><a id='5.1'></a>
>> <strong><code>FreeSpaceinGB</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/3fe7f3ec-64fc-4236-953c-d97d38ed3d21)

<br>

> 5.2. <em>What is the event category for event ID 4624?</em><br><a id='5.2'></a>
>> <strong><code>FreeSpaceinGB</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/660decf4-9790-47db-81e5-93c1f11a87de)

<br>
<br>

<h2>Task 6 . Using the Parse Operator</h2>
<h3>Parse Operator</h3>
<p>The parse operator evaluates a string expression and parses its value into one or more calculated columns. Unsuccessful parsed strings will result in null values in the calculated columns. It allows security admins to extract and parse specific information into separate columns for easier analysis and querying.<br><br>

Other parse operators include:<br><br>

<code>parse-kv</code><br><br>

<code>parse-kv</code> is used to extract structured information from a string expression and represent it in a key/value format.<br><br>

<code>parse-where</code><br><br>

<code>parse-where</code> is used to evaluate a string expression and parses its value into one or more calculated columns. In this case, the output is only the successf</p>

<h4>Syntax</h4>
<p></p><code>Table | parse [kind=regex [flags=regex_flags] |simple|relaxed] Expression with * (StringConstant ColumnName [: ColumnType]) *...</code></p>

<h4>Parameters Breakdown</h4>
<p>[ ... ]</p>

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 6.1. <em>What column was parsed in our example? </em><br><a id='6.1'></a>
>> <strong><code>EventData</code></strong><br>
<p></p>

<br>

> 6.2. <em>In our full example query, how many columns are we projecting? </em><br><a id='6.2'></a>
>> <strong><code>6</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 7 . Lab Instructions</h2>
<p>[ ... ]</p>

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 7.1. <em>Deployment ready!</em><br><a id='7.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 8 . Creating KQL Parsers</h2>

<p>Notice we are querying a custom log here to perform this particular query. First, leave the lab we started in Task 2 by pressing the Leave Lab button on the Cloud Details pop-up from Task 2. Then, access your new lab by clicking the Cloud Details button below in conjunction with the lab instructions from Task 7. Lab deployment may take about 4 mins. You can check the deployment status via <code>Resource groups -> Select the available resource group -> Settings -> Deployments</code>.</p>

<p>[  Cloud Details   ]</p>

<p>Please make sure to have performed these actions on the Cloud Details pop-up:</p>

![image](https://github.com/user-attachments/assets/158bd6a9-81a8-4c4d-998e-f580cd2afb20)


<br>

<p>Within the Azure portal:<br>

- Search for Log Analytics workspaces in the top search bar and click it<br>
- Select the available Log Analytics workspace<br>
- Click on Logs on the left side menu and close the pop-up box to see the query editor</p>

<h3>Parsers</h3>

<p>Alongside <code>parse operators</code>, there are also parse functions called <code>parsers</code>, which define a virtual table with already parsed unstructured string fields. To create parsers, after typing in your query in the query editor window, press the <code>Save</code> button, select <code>Save as function</code> from the dropdown, enter the <code>Function name</code>, define a <codeLegacy category</code>, and click <code>Save</code>. To use the saved function, click on the <code>Functions</code> tab on the left, select the <code>workspace functionsSave</code> dropdown, and select the function to run it.</p>

<h4>Example</h4>

<p>The query below searches for all the security logs for the computer with the name DC for the past month and then saves it as a function that can be used later.</p>

<p>[ ... ]</p>

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>Under which dropdown can you find your saved function?</em>Hint : <em>Select the Functions tab!</em><br><a id='8.1'></a>
>> <strong><code>Workspace functions</code></strong><br>
<p></p>


<br>
<br>

<h2>Task 9 . Lab-02: Discover</h2>
<p>Context: You received news that TeamViewer may have been compromised. The organization currently does not support the use of TeamViewer, so the security team has been tasked with verifying that no computer has TeamViewer installed on your Azure VMs. As the available SOC engineer onsite, what can you do to find all affected machines?<br><br>

Role: You are logged in as:<br>

- Log Analytics Contributor<br>
- Microsoft Sentinel Reader<br><br>

Lab scenario: Your initial assignment is to:<br>

1. First, verify which machines have TeamViewer installed and export them<br>
2. Then, verify if the machines have an update pending. Also, export these results<br>
3. Finally, recommend the next steps to the update management team<br><br>
Continue with your lab credentials from <code>Task 8</code>.</p>

<h3>Step 1: Log in To Azure Log Analytics Workspace</h3>

<p>
  
- Log in to the Azure portal using your lab credentials.<br>
- Search for Log Analytics workspaces in the top search bar and click it<br>
- Select the available Log Analytics workspace<br>
- Click on Logs on the left side menu and close the pop-up box to see the query editor</p>

<h3>Step 2: Step 2:Run the Query To See Machines With TeamViewer Installed</h3>

<p> Continue with the queries:<br>
  
- In the query editor, run the query ConfigurationData_CL to see all machines that have TeamViewer installed</p>

<p>You can see all the machines with their respective software, but this can be overwhelming, as you will need to filter through manually. With the next query below, you will be able to streamline your search to the specific software quickly.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

<h3>Step 3: Verify Which Machines Are up to Date or Require An Update</h3>

<p>- In the query editor, run the following query to see the machine's update status</p>

<p> Recommendations<br><br>

- Access the machines to uninstall TeamViewer. If you have a separate team in charge of device management, export and send the CVS document to the device management team so they can uninstall TeamViewer on affected machines<br>
- Pass the exported CVS to the update management team and request that they patch the servers as soon as possible<br>
- Check for all machines with pending updates using the update table<br>
- Save the query as a function so you can run it quickly at any time<br><br>
With your KQL knowledge, you can do many other things, such as searching the ingested logs for unusual network traffic, malicious access to sensitive files, suspicious PowerShell activities, and lateral movement across your infrastructure.</p>

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 9.1. <em>What table is queried to search for installed software?</em><br><a id='9.1'></a>
>> <strong><code>ConfigurationData_CL</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/d6009133-7ad8-41a6-94ae-674df2071db0)

<br>

![image](https://github.com/user-attachments/assets/a4b0285b-9da3-4040-9ecd-de2c671d32a4)


<br>

![image](https://github.com/user-attachments/assets/c5f72c45-67c0-44a8-9dc0-f1f2f8ee1537)

<br>

![image](https://github.com/user-attachments/assets/cb919da9-cc96-46ac-a5ca-a54ea6c2070d)


<br>

![image](https://github.com/user-attachments/assets/c4c4285a-466f-463c-bda3-ba2b6e54d750)

<br>

![image](https://github.com/user-attachments/assets/f54df3d1-d637-496c-a319-99efcfc92669)

<br>

![image](https://github.com/user-attachments/assets/8844c400-954f-4b38-98cb-d81ae5dbc8de)

<br>

![image](https://github.com/user-attachments/assets/57fa3c18-dbac-4955-bf11-7d4839d5f818)



<br>

> 9.2. <em>How many machines have TeamViewer installed on them?</em><br><a id='9.2'></a>
>> <strong><code>13</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/1992de2e-e993-4f21-89bc-ea812b1bcde1)

<br>

![image](https://github.com/user-attachments/assets/3e76f8ac-864a-43ef-b6e3-2f9c5e18dfbb)

<br>

> 9.3. <em>How many critical updates are found for JBOX00?</em>Hint : <em>Run Update_CL</em><br><a id='9.3'></a>
>> <strong><code>6</code></strong><br>
<p></p>

<br>

Update_CL
| where Computer == "JBOX00"
| where MSRCSeverity_s == "Critical"
| project TimeGenerated, Computer, Title_s, KBID_s, Classification_s, MSRCSeverity_s, PublishedDate_UTC__s, _ResourceId_s
| sort by TimeGenerated desc

<br>

![image](https://github.com/user-attachments/assets/d3d5dd0f-6306-429d-8be0-5ed2297b3f45)



<br>

> 9.4. <em>Search the Update_CL table. How many unique Linux machines can you find?</em>Hint : <em>Run Updated_CL and use the computer name!</em><br><a id='9.4'></a>
>> <strong><code>4</code></strong><br>
<p></p>

<br>

Update_CL
| where OSType_s == "Linux"
| summarize count() by Computer

<br>

![image](https://github.com/user-attachments/assets/eeab754d-c06a-412e-888d-34fddfae7b8d)


<br>

![image](https://github.com/user-attachments/assets/0357f703-038d-4136-bf6f-22d2d2b00643)

<br>



> 9.5. <em>How many machines have Google Chrome installed?</em>Hint : <em>Use ConfigurationData_CL</em><br><a id='9.5'></a>
>> <strong><code>2</code></strong><br>
<p></p>

<br>

ConfigurationData_CL
| summarize count() by SoftwareName_s
| top 5 by count_

<br>
<br>

<h2>Task 10 . Conclusion</h2>
<h3>Summary</h3>h3>
<p>Congratulations! Overall, we discussed some advanced KQL queries for effective threat hunting and investigation. Let's go through a quick recap of what we have learned in this room:<br>

- How to use the join operator<br>
- Using the union operator to combine multiple tables<br>
- Using the project operator to specify which columns should be displayed in the result<br>
- Using the extend operator to create a new calculated column<br>
- Working with parse functions<br>
- With all of this well understood, you can start hunting for threats proactively using Kusto Query Language.</p>


<p>With all of this well understood, you can start hunting for threats proactively using Kusto Query Language.</p>

<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 10.1. <em>I am ready to threat hunt!</em><br><a id='10.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/fd30fc0a-7b34-4240-8ef8-0baf811693ee"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/21769990-bb61-4767-ac5b-daf631025639"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| April 28, 2025    | 357      |     248ᵗʰ    |      6ᵗʰ     |     58ᵗʰ    |     2ⁿᵈ    |  97,995  |    694    |     60    |

</div>

<br>


<p align="center"> Global All Time:  248ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/5d718e48-f515-49d0-9923-9d8efec03f00"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/84649164-a875-4402-b3fb-52e2cb408f8b"> </p>

<p align="center"> Global monthly:    58ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/6a666c0d-02d6-4b79-be82-787baff43511"> </p>

<p align="center"> Brazil monthly:    2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/47860a33-491c-4cad-a456-b106ded7a302"> </p>


<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a>, <a href="https://tryhackme.com/p/zieglers">zieglers</a>,  <a href="https://tryhackme.com/p/not.hotdog">not.hotdog</a> and <a href="https://tryhackme.com/p/HumaneJard">HumaneJard</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
