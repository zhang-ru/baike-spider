
class urloutputer():
	def __init__(self):
		self.datas=[]
		
	def collect_data(self,new_data):
		if new_data is None:
			return None
		self.datas.append(new_data)

	def write_html(self):
		f = open("result.html","wb")
		f.write("<html>".encode('utf-8'))
		f.write("<body>".encode('utf-8'))
		f.write("<table>".encode('utf-8'))
		for data in self.datas:
			f.write("<tr>".encode('utf-8'))
			f.write("<td>%s</td>".encode('utf-8') %data['url'].encode('utf-8'))
			f.write("<td>%s</td>".encode('utf-8') %data['title'].encode('utf-8'))
			f.write("<td>%s</td>".encode('utf-8') %data['summary'].encode('utf-8'))
			f.write("</tr>".encode('utf-8'))
		f.write("</table>".encode('utf-8'))
		f.write("</body>".encode('utf-8'))
		f.write("</html>".encode('utf-8'))
		# f = open("result.html","w")
		# f.write("<html>")
		# f.write("<body>")
		# f.write("<table>")
		# for data in self.datas:
		# 	f.write("<tr>")
		# 	f.write("<td>%s</td>" %data['url'])
		# 	f.write("<td>%s</td>" %data['title'])
		# 	f.write("<td>%s</td>" %data['summary'])
		# 	f.write("</tr>")
		# f.write("</table>")
		# f.write("</body>")
		# f.write("</html>")

		f.close()