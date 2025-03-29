from tumblr_blog import TumblrBlog

class TumblrAPI:
    #Handles user input and displays the Tumblr blog data.
    
    def __init__(self):
        self.blog = None

    def get_user_input(self):
        blog_name = input("Enter the Tumblr blog name: ").strip()
        range_input = input("Enter the post range (start-end): ").strip()
        return self.parse_user_input(blog_name, range_input)

    def parse_user_input(self, blog_name, range_input):
        try:
            start, end = map(int, range_input.split('-'))
            if start < 1 or end < start:
                raise ValueError("Invalid range values.")
            self.blog = TumblrBlog(blog_name)
            return start, end
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None, None

    def display_blog_info(self, blog_info, total_posts):
        print(f"\nBlog Info:\nTitle: {blog_info['title']}\nName: {blog_info['name']}\nDescription: {blog_info['description']}\nNo of Posts: {total_posts}")
    
    def display_images(self, images):
        print("\nImage URLs:")
        for post_no, urls in images:
            print(f"{post_no}. {', '.join(urls) if urls else 'No image found in highest quality (1280)'}")

    def run(self):
        start, end = self.get_user_input()
        if start is None or end is None:
            return
        
        data = self.blog.fetch_data(start, end)
        if data:
            blog_info, total_posts = self.blog.get_blog_info(data)
            self.display_blog_info(blog_info, total_posts)
            images = self.blog.extract_image_urls(data['posts'], start)
            self.display_images(images)
