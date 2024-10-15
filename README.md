**ดาวน์โหลด password lists**
$ sudo apt install wordlists
$ gunzip /usr/share/wordlists/rockyou.txt.gz

**โคลน security project**
$ git clone https://github.com/pichaicpc/security_python.git
$ cd security_python

**คอนฟิกและรัน login.py**
$ nano login.py
เปลี่ยน API endpoint, username id, password id, 
#username text, password text, และ wordlist path
$ python login.py
