import urlmanager,urldownloader,urlparser,urloutputer

class crawer(object):
	"""initial object"""
	def __init__(self):
		self.urls = urlmanager.urlmanager()
		self.parser = urlparser.urlparser()
		self.downloader = urldownloader.urldownloader()
		self.outputter = urloutputer.urloutputer()
		
	def craw(self,url):
		self.urls.add_new_url(url)
		count = 1
		while self.urls.has_url():
			try:
				new_url = self.urls.get_new_url()
				print("craw %d : %s" %(count,new_url))
				html_content = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url,html_content)
				self.urls.add_new_urls(new_urls)
				self.outputter.collect_data(new_data)

				if count == 3:
					break
				count = count+1
			except:
				print("craw faild")

		self.outputter.write_html()




if __name__ == "__main__":
	root_url = 'http://baike.baidu.com/view/21087.htm'
	obj_crawer = crawer()
	obj_crawer.craw(root_url)