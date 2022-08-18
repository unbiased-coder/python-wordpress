import pprint
from wordpress_helper import WordPressHelper

wph = WordPressHelper()
title = 'Unbiased Coders Test Article'
content = '<h1>Welcome To <b>Unbiased Coders</b> Blog</h1><p>Enjoy your stay</p>'
tags = ['Coding']
categories = ['Wordpress']
res = wph.post_article(title, content, tags, categories)
pprint.pprint(res)
