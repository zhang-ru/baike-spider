from bs4 import BeautifulSoup as bs
import re
from urllib import parse
import urldownloader
class urlparser():

	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
		if links is None or len(links) ==0:
			return
		for link in links:
			new_url = link['href']
			new_full_url = parse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self,page_url,soup):
		new_data = {}

		title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
		summary_node = soup.find('div', class_="lemma-summary")
		new_data['title'] = title_node.get_text()
		new_data['summary'] = summary_node.get_text()
		new_data['url'] = page_url
		return new_data



	def parse(self,page_url,data):
		soup = bs(data,'html.parser')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data

