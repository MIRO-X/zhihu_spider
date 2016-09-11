# -*- coding: utf-8 -*-

import scrapy


class ZhihuItem(scrapy.Item):

	user_name = scrapy.Field()

	user_location = scrapy.Field()

	user_gender = scrapy.Field()

	user_employment = scrapy.Field()

	user_posotion = scrapy.Field()

	user_education = scrapy.Field()

	user_education_extra = scrapy.Field()

	user_description = scrapy.Field()