import urllib.request,json
from .models import Quotes

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    get_quotes_url=base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        quotes_data=url.read()
        quotes_response=json.loads(quotes_data)

        quotes_object=None
        if quotes_response:
            quote = quotes_response.get('quote')
            author = quotes_response.get('author')
           

            quotes_object= Quotes(quote,author)
            print(quotes_object)

    return quotes_object
