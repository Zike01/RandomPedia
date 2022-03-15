import requests
import webbrowser


# This Wikibot fetches and opens a random article from wikipedia.org
class WikiBot: 
    def __init__(self):
        self.API_ENDPOINT = "https://en.wikipedia.org/w/api.php"
        self.PARAMS = {
                "action": "query",
                "format": "json",
                "list": "random",
                "rnnamespace": "0"
        }
        self.url_prefix = "https://en.wikipedia.org/wiki/"

    def fetch_article(self):
        response = requests.get(self.API_ENDPOINT, self.PARAMS).json()["query"]["random"][0]["title"]
        return response
    
    def open_article(self, title):
        title_url = "_".join(title.split(" "))
        webbrowser.open(f"{self.url_prefix}{title_url}", new=2)
