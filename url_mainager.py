# codeing:utf8

class urlManager(object):
	"""docstring for UrlManager"""
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()
		
	#添加一个新的URL
	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url) 	


	def add_new_urls(self,urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)	
			
	#判断是否有新的URL待爬	
	def has_new_url(self):
		return len(self.new_urls) != 0

	#从URL中得到一个新的URL	
	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
