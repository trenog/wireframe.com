from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from g43exercise.models import Article

# Create your views here.
# Create the context list for all present/past dated articles
all_articles = Article.objects.filter(
				pub_date__lte=timezone.now()
				).order_by('pub_date')
def index(request):
	# List Page that enumerates all articles contained on the site that are
	# not future dated. If only future dated articles exist then return
	# a 404 error instead of the Index page
	count_of_present_articles = Article.objects.exclude(pub_date__gt=timezone.now()).count()
	try:
		context = {'all_articles':all_articles}
		if count_of_present_articles == 0:
			raise Exception("No Recent Articles!")
	except Exception:
		raise Http404
	return render(request, 'g43exercise/index.html', context)
	
	
def detail(request, article_id):
	# Detail page that displays all the contents of a 
	# particular article not published for a future date.
	# If a future dated article is requested, return a 404 error instead
	article = get_object_or_404(Article.objects.filter(pub_date__lte=timezone.now()), pk=article_id)
	context = {'all_articles': all_articles, 'article': article}
	return render(request, 'g43exercise/article.html', context)	
	
