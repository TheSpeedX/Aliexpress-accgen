from selenium import webdriver
from datetime import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys
import uuid,requests
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

email=get_mail()
passw=get_pass()
driver=webdriver.Firefox()
driver.get("https://login.aliexpress.com")
sleep(3)
element=driver.find_element_by_class_name("next-tabs-tab-inner")
element.click()
sleep(3)
element=driver.find_element_by_class_name("email ")
element.send_keys(email)
element=driver.find_element_by_class_name("password ")
element.send_keys(passw)
element.send_keys(Keys.RETURN)
sleep(4)
f=open("log.txt","w")
f.write("Generated at "+str(datetime.strftime(datetime.now(),"%c"))+"\n"+email+" : "+passw)
f.close()
element.close()