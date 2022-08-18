import pprint
from wordpress_helper import WordPressHelper

wph = WordPressHelper()
articles = wph.get_articles()
pprint.pprint(articles)
