from unicodedata import category

from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)
api_key = "59d2d00d14404d7f97c1cb82b9022905"
url = "https://newsapi.org/v2/top-headlines"

@app.route('/')
def hello():
    return render_template('index.html', message="Top Head Lines")

@app.route('/TopNews', methods=['POST', 'GET'])
def getnews():
    category = request.form.get('category')
    data = gettopnews(category)
    return render_template('showNews.html', message=category, data=data)

def gettopnews(category):
    params = {
        'country': 'us',
        'category': category,
        'apiKey': api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data["articles"]
        return articles
    else:
        return response.content

if __name__ == '__main__':
    app.run()