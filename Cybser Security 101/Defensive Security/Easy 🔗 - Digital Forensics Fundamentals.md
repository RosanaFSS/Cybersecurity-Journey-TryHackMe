<h3> Welcome to the <em>TryHackMe ...</em></h3>
<h1>Cyber Security 101 Learning Path ><br>
Defensive Security > Digital Forensics Fundamentals</h1>
<p>Learn about digital forensics and related processes and experiment with a practical example.</p><br>
<p>October 22, 2024<br></p><br>

<img src="https://github.com/user-attachments/assets/59d88d83-e958-45ef-b30b-c19d2780b5a3" height="200" width="200">

![image](https://github.com/user-attachments/assets/0dfc4d3a-7384-4729-bfcb-e50e37ac5fb8)


<p>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure. It´s key part of my 169-day-streak. Let´s get started!!<br><br>
Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/digitalforensicsfundamentals">Digital Forensics Fundamentals</a></p>

<h2>Task 1 - Introduction to Digital Fundamentals</h2>
<p>Forensics is the application of methods and procedures to investigate and solve crimes. The branch of forensics that investigates cyber crimes is known as <strong>digital foresincs</strong>. <strong>Cyber crime</strong> is any criminal activity conducted on or using a digital device. Several tools and techniques are used to investigate digital devices thoroughly after any crime to find and analyze evidence for necessary legal action.<br><br>

Digital devices have solved many of our problems. Communication all around the globe is just a matter of a text or call. Due to the vast usage of digital devices, besides making life easier, an increase in digital crimes - cyber crimes has also been observed. A variety of crimes are committed using digital devices.<br><br>

Consider an example where law enforcement agencies raid a bank robber’s place with proper search warrants. Some digital devices, including a laptop, mobile phone, hard drive, and a USB, were found in the robber’s home. The law enforcement agency handed over the case to the digital forensics team. The team collected evidence securely and conducted a thorough investigation inside their digital forensics lab equipped with forensics tools. The following evidence was found on the digital devices:</p>

<ul style="list-style-type:square">
    <li>A digital map of the bank was found on the suspect’s laptop, which they kept for planning the robbery.</li>
    <li>A document with the bank’s entrance and escape routes was found on the suspect’s hard drive.</li>
    <li>A document on the hard drive that listed all the bank’s physical security controls. The suspect devised plans to bypass the security measures.</li>
    <li>Some media files, including photos and videos of the suspect’s previous robberies, were inside the suspect’s laptop.</li>
    <li>After conducting a thorough investigation of the suspect’s mobile phone, some illegal chat groups and call records related to the bank robbery were also found.</li>
</ul><br></p>

<p>After conducting a thorough investigation of the suspect’s mobile phone, some illegal chat groups and call records related to the bank robbery were also found.<br></p>
<h3>Learning Objectives</h3>
<ol type="1. ">
  <li>Phases of digital forensics</li>
  <li>Types of digital forensics</li>
  <li>Procedure of evidence acquisition</li>
  <li>Windows forensics</li>
  <li>Solving a forensics case</li>
</ol></p>

> 1.1 - <em>Which team was handed the case by law enforcement?</em><br>
>> <strong>digital forensics</strong><br>
<p><br></p>



<h2>Task 2 - Digital Forensics Methodology</h2>

> 2.1 - <em>Which phase of digital forensics is concerned with correlating the collected data to draw any conclusions from it?</em><br>
>> <strong>Analysis</strong><br>
<p><br></p>

> 2.2 - <em>Which phase of digital forensics is concerned with extracting the data of interest from the collected evidence?</em><br>
>> <strong>Examination</strong><br>
<p><br></p>

<h2>Task 3 - Evidence Acquisition</h2>

> 3.1 - <em>Which tool is used to ensure data integrity during the collection?</em><br>
>> <strong>write blocker</strong><br>
<p><br></p>

> 3.2 - <em>What is the name of the document that has all the details of the collected digital evidence?</em><br>
>> <strong>chain of custody</strong><br>
<p><br></p>

<h2>Task 4 - Windows Forensics</h2>

> 4.1 - <em>Which type of forensic image is taken to collect the volatile data from the operating system?</em><br>
>> <strong>memory image</strong><br>
<p><br></p>


<h2>Task 5 - Pratical Examples of Digital Forensics</h2>

> 5.1 - <em>Using <code>pdfinfo</code>, find out the author of the attached PDF file, <code>ransom-letter.pdf</code>.</em><br>
>> <strong>Ann Gree Shepherd</strong><br>
<p><br></p>

<pre><code>$ exiftool letter-image.jpg | grep GPS
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Time Stamp                  : 13:37:33
GPS Latitude                    : 51 deg 30' 51.90" N
GPS Longitude                   : 0 deg 5' 38.73" W
GPS Position                    : 51 deg 30' 51.90" N, 0 deg 5' 38.73" W
</code></pre>

> 5.2 - <em>Which type of forensic image is taken to collect the volatile data from the operating system?</em><br>
>> <strong>Milk Street</strong><br>
<p><br></p>

<pre><code>$ exiftool letter-image.jpg | grep Camera
Camera Model Name               : Canon EOS R6
Camera Profile                  : Adobe Standard
Camera Profile Digest           : 441F68BD6BC3369B59256B103CE2CD5C
History Software Agent          : Adobe Photoshop Lightroom Classic 10.2 (Macintosh), Adobe Photoshop Camera Raw 14.0, Adobe Photoshop Camera Raw 14.0.1 (Windows), Adobe Photoshop Camera Raw 14.0.1 (Windows), Adobe Photoshop 22.4 (Windows), Adobe Photoshop 22.4 (Windows), Adobe Photoshop 22.4 (Windows), Gimp 2.10 (Linux)
Look Parameters Camera Profile  : Adobe Standard
</code></pre>

> 5.3 - <em>What is the model name of the camera used to take this photo?</em><br>
>> <strong>Canon EOS R6</strong><br>
<p><br></p>


<h2>Room Complete</h2>

![image](https://github.com/user-attachments/assets/2a18b505-20bd-4f18-8a33-e703535d458f)
