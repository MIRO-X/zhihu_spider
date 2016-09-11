import scrapy

from zhihu.items import ZhihuItem

class ZhuhuSpider(scrapy.Spider):
	
	name = "zhihu"

	start_urls = ["https://www.zhihu.com"]

	def start_requests(self):
		return [scrapy.Request("https://www.zhihu.com/login", meta = {'cookiejar' : 1}, callback = self.post_login)]

	def post_login(self, response):
		xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
		return scrapy.FormRequest.form_response(
			response,
			meta = {'cookiejar':response.meta['cookiejar']},
			headers = self.headers,
			formdata = {
				'_xsrf':xsrf,
				'password':'19930913nth',
				'phone_num':'15757135736'
			},
			callback = self.test,
			dont_filter = True
		)

	def after_login(self, response):
		host = "https://www.zhihu.com/people/miro-x/followees"
		yield scrapy.Request(host, callback = self.test)

	def test(self, response):
		print("模拟登陆Success")

	def get_user_list(self, response):
		url_list = response.xpath('//')
		for url_user in url_list:
			yield scrapy.Request(url_people, callback = self.parse_user_profile)

	def parse_user_profile(self, response):
		for sel in response.xpath(''):
			item = ZhihuItem()
			item['user_name'] = sel.xpath('').extract()
			yield item