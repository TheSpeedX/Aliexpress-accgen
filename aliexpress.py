from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import sleep
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
def acc_exists(email):
	url = "https://login.aliexpress.com:443/join/preCheckForRegister.htm?registerFrom=AE_MAIN_REGISTER&email="+email
	#url = "https://login.aliexpress.com:443/join/preCheckForRegister.htm?registerFrom=AE_MAIN_REGISTER&umidToken=C1575133203514201298035791575228273407242106054&ua=121%23dHwlkCmXKjwlVlmTGVB9l9kGecznpuiIK3OAxxrIeMCyO3uZv3i1lUZYAcfdK5j9lGgY%2Bzp5pMl98A9Kf0DIllxmRcffK7jypnRJxaPIDgtlO3rJqRD5lwLYAcfdK5jVlmuY%2BzLIKM9VA3rnEkDIll9YOiEdKujlx4JCmojYlBCgebCs8ySm%2F0rWaOK0COe2CpxSpX0lk654M3BmbgibCN%2BXQ%2BnvNjOhnnCLR2b0CZeZ4jNN2lS0CNhFFtK0bZJinjxSpXb0C6048u%2FmCbiDkeHaF960C6ibnnC9pCi0CK4fVuTVM2jQb%2BEqQ1HlDZTOnn%2BH8giuCNzT831hbZs0vwwAVau9t5oX4qs2Z%2FxIlX%2FB%2B93jYwcWSXXhEPG7H4stTuYBpxaZV0rEe4H1DewwFdMF6f2Jf6Bkp9WHLcg4tGeulRulRx0inrW7DgvcJm6RMtpYtUYuntmQUeFB7FEo8umIvexlgUr0BG2eZ6ovA0L%2FfmM8pAXvn0D3QRouhHYb0ngzBlkb1tp%2B0Or0%2FxRWbPt7tH1JwYMzAKyBA9Yqwp6OwleQZylNfoYBur2w4nA82R4rofeRCbSKQGy0wbVtDot%2FIjefgP4gsrXpjOKmoshroClLjpQLhK53VSXbG0%2BnQlcdTKnknOBdimq21fs0KFc27ZTlzcvNa3GqHa%2Fh2QOuBhBOB6TeoR0jbJMCdO97q2T198q1eVLf2biDIxNQX8%2Ba8VzqFxO1a27j2ppJ0%2BaFfj6uj8Tv5JG1oLHpbPWJ25zH38TWLQhTtllxNXqNJCgTm4Ura8t3bUIFCo5HwPAm48kVFm3IitK2CauvdVWBCRGNFLp3ssNAOL6BV%2FdVrlsCpkCiMn0wp5I8MvPZDd7XC9lMKRowz3c5zA%2BXzZo3RZ9piDh9IJ9K5hL91O2YhJTdtiyr8MKqUp2%2FazMkiBzTbN7ycKfSLpvuoEXH6mIU5V7y1IrrhchobJTWhQmdEEh2cAA8XTMIF4B9AUlajTYIfsU36XuYiq6VTHrgOpZUFyl3%2BXb1F1mCP%2BXxoAZqgF7x%2B%2FlDrT19dxb%2FiobLWZ1zsPBRXGp5oYR1gXyxtw%3D%3D&email=hello1100@gmail.com"
	#cookies = {"ali_apache_id": "10.182.250.129.157513276631.542536.9", "xman_us_f": "zero_order=y&x_locale=en_US&x_l=0&x_user=IN|IN|shopper|ifm|2289405277&acs_rt=7c572bcf0f55484591d665c6508fe404", "acs_usuc_t": "acs_rt=7c572bcf0f55484591d665c6508fe404&x_csrf=7u1id14otsjv", "intl_locale": "en_US", "aep_usuc_f": "site=glo&c_tp=USD&x_alimid=2289405277&isb=y&region=IN&b_locale=en_US", "intl_common_forever": "4CELkipbQLzVT5HzwIS1aw433644spDmjy4YILsRsEjbuRLglKw60A==", "xman_f": "j4iLnVm6Kl80sGH8Diy+J85DjCVHNN6bDQvDk/Ny84wfyvdQClt2XglolhIGZTnTf5XwgcDMssOJIVgTA57OqeElo04FowdWvRcwxpsASqFu5WsMhOVQn+4qApbmoEo6Zqq8ikieMRNwxzoQgy0lED4bCx8xqC6ebTMAXeGX9OrHt/RkXr86foXXd//5Ezn0I0BkIMK2kb/8YMjck4debpUbhwJPC7nI8phzFNAnZ3PviY7CSc5xSxgrYdx9wxdRX8xMC39lGbUD7ygRswiIerShf1qolIvVEMinu2guhfnzBCrHvSE+0ALCNCIzFkfclOj2clGmDvpJltED4Ljgdh+J+me9RMJ+RehrYl+RxQXsSZ0iBT/TIAikbki2wtURKUMqRottioQ=", "cna": "TB9oFlw5K1wCAXXt6Aicwjbc", "isg": "BHFxNaitiOTs8yT2XVK7PQA4g_3L9s4zdSz9h1ONrTh-eqHM8695oIzcnNa5qX0I", "l": "dBS2GVjqq5XmNsoUBOfamuIRXkbOrLd2DkPzw4ZIDICP_cBJo2BdWZKJreKvCn6NnsHVF35u5_48BrYUPyUIhpGAfRedVEbzodTh.", "_m_h5_tk": "29e00f71dcd063318a941c1aa84ffdf0_1575135111956", "_m_h5_tk_enc": "9252bbbb826eb1c4ea107191a3b2f6cb", "ali_apache_track": "mt=1|mid=in688525276pizae", "ali_apache_tracktmp": "W_signed=Y", "JSESSIONID": "5BBB5A20D4BE8436335956993805E5F2", "aep_common_f": "ni5szgMe40xedBZMu/TXCUBTylfQHldGupOc0c5WLPgkTN4rccSCYw==", "xman_t": "HDTi2svvhC1AoTNQiiM/X/ZuMCIhvfPZz0/Z18I/RTaFYQCIGrJ8fkzYa6DUQbr8GSrLCUob4YigQitVnjeJ/y0ODDe8SGcB", "_uab_collina": "157513320298812488366246", "_bl_uid": "jtkv73djlg0tdFnOt4hUob4v35RU", "re_ri_f": "/opC6sv+Rn1VBGvjS0IL/YUujFRvRaG8dHMgc7RR4NPKSXXOAcgMKdecMULNENaf"}
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Referer": "https://login.aliexpress.com/"}
	#requests.get(url, headers=headers, cookies=cookies)
	r=requests.get(url,headers=headers).text
	return not '"isEmailExisted":false' in r
def makeacc(email,passw,proxy):
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
	profile.set_preference("browser.privatebrowsing.autostart", true)
	profile.set_preference("general.useragent.override", random.choice(user_agent_list))
	profile.update_preferences()
	driver = webdriver.Firefox(profile)
	driver.get("https://login.aliexpress.com")
	sleep(3)
	element=driver.find_element_by_class_name("next-tabs-tab-inner")
	element.click()
	sleep(1)
	element=driver.find_element_by_class_name("email ")
	element.send_keys(email)
	element=driver.find_element_by_class_name("password ")
	element.send_keys(passw)
	element=driver.find_element_by_class_name("submit")
	element.click()
	sleep(4)
	f=open("generated_"+datetime.now().strftime("%Y_%m_%d")+".txt","a")
	if proxy:
		f.write("Generated at "+str(datetime.strftime(datetime.now(),"%c"))+" Used Proxy: "+proxy+"\n"+email+" : "+passw+"\n")
	else:
		f.write("Generated at "+str(datetime.strftime(datetime.now(),"%c"))+" Used Proxy: NONE\n"+email+" : "+passw+"\n")
	f.close()
	#input("Press Create Account Button And Press Enter..")
	driver.quit()
	return True
def get_proxies(fname):
	if not fname.strip()=="":
		f=open(fname,"r")
		dat=f.read()
		f.close()
	else:
		dat=requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=2000&country=all&ssl=yes&anonymity=all").text
	match=re.findall(r'\d+\.\d+\.\d+\.\d+:\d+',dat)
	random.shuffle(match)
	return match
def isdead(proxy):
	return False
	try:
		requests.get("https://httpbin.org/ip",proxies={"http": proxy, "https": proxy},verify=False)
		return False
	except:
		print("Skipping. Connnection error")
		return True
	# return requests.get("https://httpbin.org/ip",proxies={"http": proxy, "https": proxy},verify=False)
def main():
	n=int(input("Enter Number Accounts You Want: "))
	combos=[]
	if "n" in input("Do You Want To use Random Mail And Pass(Y/n): ").lower():
		fp=input("Please Provide A Mail Combo Path: ")
		combos=re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+[:][a-zA-Z0-9]+)',open(fp,"r").read())
	use_proxy=False
	if "y" in input("Do You Want To use Proxies(y/N): ").lower():
		use_proxy=True
		if "n" in input("Do You Want To use Random Proxies(Y/n): ").lower():
			fp=input("Please Provide A Mail Combo Path: ")
			proxies=get_proxies(fp)
		else:
			print("Please Wait Generating Proxies....")
			proxies=get_proxies("")
		proxies_pool=cycle(proxies)
	used_mails=[]
	c,i=0,0
	while i<n:
		print("[+] Generating Account Number: ",i+1)
		if use_proxy:
			proxy = next(proxies_pool)
			print("[!] Checking Proxy: ",proxy)
			if isdead(proxy):
				proxies.remove(proxy)
				random.shuffle(proxies)
				proxies_pool=cycle(proxies)
				continue
		else:
			proxy=""
		if len(combos)!=0 and c< len(combos):
			email,passw=combos[c].split(":")
		else:
			email,passw=get_mail(),get_pass(10)
		if not email in used_mails:
			c+=1
			used_mails.append(email)
		if acc_exists(email):
			f=open("existing_"+datetime.now().strftime("%Y_%m_%d")+".txt","a")
			f.write("Checked at "+str(datetime.strftime(datetime.now(),"%c"))+"\n"+email+" : "+passw+"\n")
			f.close()
		else:
			if makeacc(email,passw,proxy):
				i+=1
	print("Accounts Have Been Generated !!!")
print("""
				Aliexpress Account Generator 
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
