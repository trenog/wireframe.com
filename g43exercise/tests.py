from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from g43exercise.models import Article

import datetime
# Create your tests helpers here.
def create_article(title, text, days):
	"""
	Creates a sample article with a given title and article body based on an offset
	day of publication relative to today.
	"""
	time = timezone.now() + datetime.timedelta(days)
	return Article.objects.create(title=title,body_text=text,pub_date=time)
# Create your tests here.
class IndexTests(TestCase):
	def test_no_articles(self):
		"""
		If there are no articles posted to the website, then rather than an empty
		index page, the page should display a 404 error.
		"""
		response = self.client.get(reverse('g43:index'))
		self.assertEqual(response.status_code,404)
	def test_one_or_more_past_articles(self):
		"""
		If at least one article with a posted date dated before today is available to the
		website, then the index page should be populated with that page and display
		as normal.
		"""
		create_article(title="My First Article",text="This is the first article I made",days=-30)
		response = self.client.get(reverse('g43:index'))
		self.assertEqual(response.status_code,200)		
	def test_article_posted_today(self):
		"""
		If at least one article with a posted date dated today is available to the
		website, then the index page should be populated with that page and display
		as normal.		
		"""
		create_article(title="My First Article",text="This is the first article I made",days=0)
		response = self.client.get(reverse('g43:index'))
		self.assertEqual(response.status_code,200)			
	def test_one_or_more_future_articles(self):
		"""
		If the only articles posted to the website are future dated to prevent their
		immediate publication, then the index page should not display and instead a
		404 error page is shown.
		"""
		create_article(title="My First Article",text="This is the first article I made",days=30)
		response = self.client.get(reverse('g43:index'))
		self.assertEqual(response.status_code,404)		
	def test_one_past_one_future_article(self):
		"""
		If at least one article with a posted date dated before today is available, regardless
		of the number of articles posted that are future dated, the index page should be
		populated with the non-future dated articles and display as normal.
		"""
		create_article(title="My First Article",text="This is the first article I made",days=-30)
		create_article(title="Future News",text="What we've known for some time will shock you",days=30)
		response = self.client.get(reverse('g43:index'))
		self.assertEqual(response.status_code,200)	
		
class ArticleTests(TestCase):		
	def test_cant_read_future_article(self):
		"""
		If an attempt is made to access the detail page of a future dated article then
		the detail page should instead return a 404 page.
		"""
		create_article(title="My First Article",text="This is the first article I made",days=-30)
		future_article = create_article(title="Future News",text="What we've known for some time will shock you",days=30)
		response = self.client.get(reverse('g43:detail', args=(future_article.article_id,)))
		self.assertEqual(response.status_code,404)		
	def text_can_read_past_article(self):
		"""
		If an attempt is made to access the detail page of an article with a posting date
		dated before today then a call to that article's detail page should return that
		article's details
		"""
		present_article = create_article(title="My First Article",text="This is the first article I made",days=-30)
		create_article(title="Future News",text="What we've known for some time will shock you",days=30)
		response = self.client.get(reverse('g43:detail', args=(present_article.article_id,)))
		self.assertEqual(response.status_code,200)		