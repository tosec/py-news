import requests
from config import API_KEY

URL = 'https://newsapi.org/v2/top-headlines?'

def get_articles_by_category(category): # query top headlines using params given
    query_parameters = {         
        "category": category,
        "sortby": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()  # error thrown when http returns a bad response

        articles = response.json()['articles']

        results = []

        for article in articles: 
            results.append({"title": article["title"], "publishedAt": article["publishedAt"], "description": article["description"], "url": article["url"]})

        for result in results:
            print('Title: ',result['title'])
            print('Published at: ', result["publishedAt"])
            print('Description: ', result['description'])
            print('Link: ', result['url'])
            print('')

    except requests.exceptions.RequestException as e:   # catch any exceptions that may occur during request
        print(f"Error fetching data: {e}")

# set category u wish to fetch
get_articles_by_category("technology")


