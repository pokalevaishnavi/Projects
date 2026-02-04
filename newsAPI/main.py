import requests

query = input("What type of news are you interested today?\n")
key = "30f5bf43f6d3496b91a304ff872971c0"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-02&sortBy=publishedAt&apiKey={key}"

print(url)

r = requests.get(url)
data = r.json()
articles = data['articles']

for index,article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("****************************\n")