try:
    import urllib2 as urllib
except ImportError:  # python3
    import urllib.request as urllib
import os
import datetime

import finsymbols


def get_symbol_list(symbol_data):
    symbol_list = list()
    symbol_data = symbol_data.replace('"', "")
    symbol_data = symbol_data.split("\r\n")
    symbol_data = list(map(lambda x: x.split(","), symbol_data))
    # We need to cut off the first row because it is the header and the last
    # row because it is a null string
    for row in symbol_data[1:-1]:
        symbol_list.append(row[0])
    return symbol_list


def get_exchange_url(exchange):
    return ("http://www.nasdaq.com/screening/companies-by-industry.aspx?"
            "exchange={}&render=download".format(exchange))


def is_cached(file_path):
    '''
    Checks if the file cached is still valid
    '''
    if not os.path.exists(file_path):
        return False

    file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
    current_time = datetime.datetime.now()
    file_age = (current_time - file_time).total_seconds()

    if file_age > 86400:
        return False
    else:
        return True


def fetch_file(url):
    '''
    Gets and downloads files
    '''
    file_fetcher = urllib.build_opener()
    file_fetcher.addheaders =  [('User-agent', 'Mozilla/5.0')]
    file_data = file_fetcher.open(url).read()
    if isinstance(file_data, str):  # Python2
        return file_data
    elif isinstance(file_data, bytes):  # Python3
        return file_data.decode("utf-8")


def wiki_html(url,file_name):
    '''
    Obtains html from Wikipedia
    Note: API exist but for my use case. Data returned was not parsable. Preferred to use html
    python-wikitools - http://code.google.com/p/python-wikitools/
    Ex. http://en.wikipedia.org/w/api.php?format=xml&action=query&titles=List_of_S%26P_500_companies&prop=revisions&rvprop=content
    '''
    file_path = os.path.join(os.path.dirname(finsymbols.__file__), file_name)

    if is_cached(file_path):
        with open(file_path, "r") as sp500_file:
            return sp500_file.read()
    else:
        wiki_html = fetch_file('http://en.wikipedia.org/wiki/' + str(url))
        saved_file = open(file_path , "w")
        saved_file.write(wiki_html)
        saved_file.close()
        return wiki_html
