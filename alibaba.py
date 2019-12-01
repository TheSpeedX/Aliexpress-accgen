from selenium import webdriver
from datetime import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys
import uuid,requests
import re,random
from itertools import cycle

def get_name():
	url = "https://fauxid.com:443/"
	cookies = {"__cfduid": "d603f0996162b0831bb0bf3b7e13a6db51573994588", "XSRF-TOKEN": "eyJpdiI6IlZheHNjMzI5bVZobEl3RXY3Y1IwU1E9PSIsInZhbHVlIjoiajU4ZjU0cWZkMUZaY3JRMzFybHpsUU9zVFBZNEhDbEhWMmJKbFRuUkZCN1pYdWFjcFkxNmZNT0dId3FGSTJ0QiIsIm1hYyI6IjNlODg4M2Y1MGE1ZTkxOTBjMmJhYTkzNTZkMWM5NGE0YzdmMmNhODM3ZDA3ZGQ2NzYwNTY0NjA2MTI3ZTZjYTYifQ%3D%3D", "fauxid_session": "eyJpdiI6ImFJWHdvbnF4cThRaVJuaGZzWWVCaFE9PSIsInZhbHVlIjoia2cyZ0FQc2RKVFdDVG9WcllDUllaZFwvdHI1NG9aeTFtbitUZFNVZ1ZwSVRTVzJ4Z0szWFc1bm5oYVRpOHlzWFkiLCJtYWMiOiJlYzY5ZGUzYzBiOTBiNmQ0Y2E4NDNhMGI1ZmE1NTE3OGFlOWQwNWY5YWUyODk0ZTNmN2ZiODc0YmIwN2Q1ZTM2In0%3D"}
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.google.com/", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Cache-Control": "max-age=0"}
	r=requests.get(url, headers=headers, cookies=cookies).text
	p1=r.find('<span class="id_name can-copy">',r.find('Fake Name:'))+31
	p2=r.find('</span>',p1)
	name=r[p1:p2].strip()
	return name
def get_mail():
	#Mail is From https://generator.email/
	name=get_name().replace(".","").replace(" ",".")
	name=name.lower()
	return name+"@2bin.ru"
def get_pass(len):
	return uuid.uuid4().hex.replace("-","")[0:len]
def makeacc(mail,passw,proxy):
	user_agent_list = [
   #Chrome
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	#Firefox
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]
	print("Making Account With Creds:    "+email+" : "+passw)
	if proxy:
		print("Using Proxy: "+proxy)
	profile = webdriver.FirefoxProfile()
	if not proxy.strip()=="":
		PROXY_HOST,PROXY_PORT=proxy.split(":")
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.http",PROXY_HOST)
		profile.set_preference("network.proxy.http_port",int(PROXY_PORT))
		profile.set_preference("network.proxy.https",PROXY_HOST)
		profile.set_preference("network.proxy.https_port",int(PROXY_PORT))
		profile.set_preference("network.proxy.ssl",PROXY_HOST)
		profile.set_preference("network.proxy.ssl_port",int(PROXY_PORT))
		profile.set_preference("network.proxy.ftp",PROXY_HOST)
		profile.set_preference("network.proxy.ftp_port",int(PROXY_PORT))
		profile.set_preference("network.proxy.socks",PROXY_HOST)
		profile.set_preference("network.proxy.socks_port",int(PROXY_PORT))
	profile.set_preference("general.useragent.override", random.choice(user_agent_list))
	profile.update_preferences()
	driver = webdriver.Firefox(profile)
	driver.get("https://login.aliexpress.com")
	sleep(3)
	element=driver.find_element_by_class_name("next-tabs-tab-inner")
	element.click()
	sleep(3)
	element=driver.find_element_by_class_name("email ")
	element.send_keys(email)
	element=driver.find_element_by_class_name("password ")
	element.send_keys(passw)
	element=driver.find_element_by_class_name("submit")
	element.click()
	sleep(4)
	flag=driver.page_source.find("This email already exists.")!=-1
	if flag:
		f=open("generated_"+datetime.now().strftime("%Y_%m_%d")+".txt","a")
		if proxy:
			f.write("Generated at "+str(datetime.strftime(datetime.now(),"%c"))+" Used Proxy: "+proxy+"\n"+email+" : "+passw+"\n")
		else:
			f.write("Generated at "+str(datetime.strftime(datetime.now(),"%c"))+" Used Proxy: NONE\n"+email+" : "+passw+"\n")
		f.close()
	else:
		f=open("existing_"+datetime.now().strftime("%Y_%m_%d")+".txt","a")
		f.write("Checked at "+str(datetime.strftime(datetime.now(),"%c"))+"\n"+email+" : "+passw+"\n")
		f.close()
	driver.quit()
	return flag
def get_proxies(fname):
	if not fname.strip()=="":
		f=open(fname,"r")
		dat=f.read()
		f.close()
	else:
		dat=requests.get("http://spys.me/proxy.txt").text
	match=re.findall(r'\d+\.\d+\.\d+\.\d+:\d+',dat)
	return match
def isdead(proxy):
	host,port=proxy.split(":")
	try:
		requests.get(url,proxies={"http": proxy, "https": proxy},timeout=5)
		return False
	except:
		print("Skipping. Connnection error")
		return True
def main():
	n=int(input("Enter Number Accounts You Want: "))
	combos=[]
	if "n" in input("Do You Want To use Random Mail And Pass(Y/N): ").lower():
		fp=input("Please Provide A Mail Combo Path: ")
		combos=re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+[:][a-zA-Z0-9]+)',open(fp,"r").read())
	if "n" in input("Do You Want To use Random Proxies(Y/N): ").lower():
		fp=input("Please Provide A Mail Combo Path: ")
		proxies=get_proxies(fp)
	else:
		print("Please Wait Generating Proxies....")
		proxies=get_proxies("")
	used_mails=[]
	c,i=0,0
	proxies_pool=cycle(proxies)
	while i<n:
		print("[+] Generating Account Number: ",i)
		proxy = next(proxy_pool)
		print("[!] Checking Proxy: ",proxy)
		if isdead(proxy):
			proxies.remove(proxy)
			random.shuffle(proxies)
			proxies_pool=cycle(proxies)
			continue
		if not len(combos)!=0:
			email,passw=combos[c].split(":")
		else:
			email,passw=get_mail(),get_pass(10)
		if not email in used_mails:
			c+=1
			used_mails.append(email)	
		if makeacc(email,passw,proxy):
			i+=1
	print("Accounts Have Been Generated !!!")
print("""
				Alibaba Account Generator 
		By 

   ▄████████    ▄███████▄    ▄████████    ▄████████ ████████▄  ▀████    ▐████▀ 
  ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███   ███▌   ████▀  
  ███    █▀    ███    ███   ███    █▀    ███    █▀  ███    ███    ███  ▐███    
  ███          ███    ███  ▄███▄▄▄      ▄███▄▄▄     ███    ███    ▀███▄███▀    
▀███████████ ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀     ███    ███    ████▀██▄     
         ███   ███          ███    █▄    ███    █▄  ███    ███   ▐███  ▀███    
   ▄█    ███   ███          ███    ███   ███    ███ ███   ▄███  ▄███     ███▄  
 ▄████████▀   ▄████▀        ██████████   ██████████ ████████▀  ████       ███▄ 
                                                                               


	""")
main()