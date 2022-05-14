import urllib.request,json
from .models import Quotes

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    get_quotes_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        quotes_data=url.read()
        quotes_response=json.loads(quotes_data)

        quotes_object=None
        if quotes_response:
            author = quotes_response.get('author')
            quotes = quotes_response.get('quotes')

    return quotes_object
