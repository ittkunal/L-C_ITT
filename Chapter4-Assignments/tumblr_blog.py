import requests
import json
import re

class TumblrBlog:
    #Handles all interactions with Tumblr's API and processes the blog-related data.
    
    def __init__(self, blog_name):
        self.blog_name = blog_name
        self.base_url = f"https://{blog_name}.tumblr.com/api/read/json?type=photo"

    def fetch_data(self, start, end):
        api_url = f"{self.base_url}&num={end - start + 1}&start={start - 1}"
        return self.get_api_response(api_url)

    def get_api_response(self, api_url):
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return self.extract_json(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def extract_json(self, response_text):
        match = re.search(r'var tumblr_api_read = (.*);', response_text, re.DOTALL)
        return self.parse_json(match.group(1)) if match else None

    def parse_json(self, json_text):
        try:
            return json.loads(json_text)
        except json.JSONDecodeError:
            print("Error parsing JSON response.")
            return None

    def get_blog_info(self, data):
        blog_info = data.get('tumblelog', {})
        total_posts = data.get('posts-total', 0)
        return blog_info, total_posts

    def extract_image_urls(self, posts, start):
        return [(i, self.get_post_images(post)) for i, post in enumerate(posts, start=start)]

    def get_post_images(self, post):
        return [post.get('photo-url-1280')] + [photo['photo-url-1280'] for photo in post.get('photos', [])] if 'photo-url-1280' in post else []
