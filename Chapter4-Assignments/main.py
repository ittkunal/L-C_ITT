from tumblr_api import TumblrAPI

def main():
    #Main function to execute the Tumblr blog fetching and displaying process.
    tumblr_api = TumblrAPI()
    tumblr_api.run()

if __name__ == "__main__":
    main()