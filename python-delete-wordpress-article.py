import pprint
from wordpress_helper import WordPressHelper

wph = WordPressHelper()
res = wph.delete_article(103)
pprint.pprint(res)
