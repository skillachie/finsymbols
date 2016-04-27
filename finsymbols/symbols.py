import pprint
import sys
from bs4 import BeautifulSoup
from finsymbols.symbol_helper import *


def get_sp500_symbols():
    page_html = wiki_html('List_of_S%26P_500_companies', 'SP500.html')
    wiki_soup = BeautifulSoup(page_html, "html.parser")
    symbol_table = wiki_soup.find(attrs={'class': 'wikitable sortable'})

    symbol_data_list = list()

    for symbol in symbol_table.find_all("tr"):
        symbol_data_content = dict()
        symbol_raw_data = symbol.find_all("td")
        td_count = 0
        for symbol_data in symbol_raw_data:
            if(td_count == 0):
                symbol_data_content[
                    'symbol'] = symbol_data.text
            elif(td_count == 1):
                symbol_data_content[
                    'company'] = symbol_data.text
            elif(td_count == 3):
                symbol_data_content[
                    'sector'] = symbol_data.text
            elif(td_count == 4):
                symbol_data_content[
                    'industry'] = symbol_data.text
            elif(td_count == 5):
                symbol_data_content[
                    'headquarters'] = symbol_data.text

            td_count += 1

        symbol_data_list.append(symbol_data_content)

    return symbol_data_list[1::]


def get_nyse_symbols():
    return _get_exchange_data("NYSE")


def get_amex_symbols():
    return _get_exchange_data("AMEX")


def get_nasdaq_symbols():
    return _get_exchange_data("NASDAQ")


def _get_exchange_data(exchange):
    url = get_exchange_url(exchange)
    file_path = os.path.join(os.path.dirname(finsymbols.__file__), exchange)
    if is_cached(file_path):
        with open(file_path, "r") as cached_file:
            symbol_data = cached_file.read()
    else:
        symbol_data = fetch_file(url)
        save_file(file_path, symbol_data)

    return get_symbol_list(symbol_data, exchange)
