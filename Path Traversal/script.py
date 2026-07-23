import requests
from termcolor import colored
successful_payloads=[]
payloads = open("payloads", "r")
fuzz_url=input("Enter the URL: ")
for payload in payloads:
    url = fuzz_url.replace("FUZZ",payload)
    print(payload, end='    |    ')
    r = requests.get(url)
    print(r.status_code)
    if (r.status_code!=400):
        print(colored("[+] Possible Paylods: "+payload,"green"))
        successful_payloads.append(payload)
if (len(successful_payloads)):
    print(colored("---- RESULTS FOUND ----", "green"))
    for payload in successful_payloads:
        print(payload)
else:
    print(colored("[-] NO RESULTS FOUND", "red"))

    
payloads.close()