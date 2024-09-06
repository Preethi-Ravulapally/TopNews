import requests

api_key = "59d2d00d14404d7f97c1cb82b9022905"
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-08-01&'
       'sortBy=popularity&'
       'apiKey=59d2d00d14404d7f97c1cb82b9022905')

# news_url = f"https://newsapi.org/v2/everything?sortBy=popularity&apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data["articles"]

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 50)
else:
    print(f"Error: {response.status_code}")
    print(f"Error stack: {response.content}")