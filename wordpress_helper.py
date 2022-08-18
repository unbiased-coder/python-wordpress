import os
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost, GetPosts, DeletePost
from dotenv import load_dotenv

load_dotenv()

class WordPressHelper:
    def __init__(self) -> None:
        self.user = os.getenv('WORDPRESS_USER')
        self.passwd = os.getenv('WORDPRESS_PASS')
        self.host = os.getenv('WORDPRESS_HOST')
        self.port = os.getenv('WORDPRESS_PORT')
        self.proto = os.getenv('WORDPRESS_PROTO')
        self.wp_url = f'{self.proto}://{self.host}:{self.port}'

    def delete_article(self, article_id):
        wp_url = f'{self.wp_url}/xmlrpc.php'
        print(f'Connecting to: {wp_url}')
        self.client = Client(wp_url, self.user, self.passwd)

        print(f'Deleting post {article_id} from wordpress')
        res = self.client.call(DeletePost(article_id))
        print(f'Successfully deleted post: {article_id} from server')
        return res

    def get_articles(self):
        wp_url = f'{self.wp_url}/xmlrpc.php'
        print(f'Connecting to: {wp_url}')
        self.client = Client(wp_url, self.user, self.passwd)

        print('Getting Posts from wordpress')
        res = self.client.call(GetPosts())
        print('Successfully received posts from server')
        return res

    def post_article(self, title, content, tags, categories):
        wp_url = f'{self.wp_url}/xmlrpc.php'
        print(f'Connecting to: {wp_url}')
        self.client = Client(wp_url, self.user, self.passwd)

        print(f'Creating wordpress post using title: {title}')
        post = WordPressPost()
        post.title = title
        post.content = content
        post.term_names = {
            'post_tag': tags,
            'category': categories
        }
        
        res = self.client.call(NewPost(post))
        print('Successfully sent post to server')
        return res
