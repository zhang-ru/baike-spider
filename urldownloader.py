# -*- coding:utf-8 -*- 
from urllib import request
import requests

class urldownloader():
	
	def download(self,url):
		if url is None:
			return None
		r = requests.get(url)
		if r.status_code != 200:
			return None
		r.encoding='uft-8'
		return r.text

# a=urldownloader()
# print(a.download("http://www.baidu.com"))
