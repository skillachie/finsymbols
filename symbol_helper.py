import urllib2
import os
import sys
import csv


"""
Helper functions that returns raw symbol data

"""



"""
Obtains html from Wikipedia

Note: API exist but for my use case. Data returned was not parsable. Preferred to use html
python-wikitools - http://code.google.com/p/python-wikitools/
Ex. http://en.wikipedia.org/w/api.php?format=xml&action=query&titles=List_of_S%26P_500_companies&prop=revisions&rvprop=content

"""

def wiki_html(url):
	wiki_fetcher = urllib2.build_opener()
	wiki_fetcher.addheaders =  [('User-agent', 'Mozilla/5.0')]

	wiki_html = wiki_fetcher.open('http://en.wikipedia.org/wiki/'+str(url)).read()
	return wiki_html




"""
Reads symbols in csv file as dict
"""

def read_csv(exchange):
	
	symbol_list = list()
	module_path = os.path.dirname(os.path.realpath(__file__))
	exchanges_dir = os.path.join(module_path,'exchanges')
	file_path = os.path.abspath(exchanges_dir) + os.sep + exchange + '.csv'
	exchange_file = csv.DictReader(open(file_path),fieldnames=['symbol', 'company', 'LastSale', 'MarketCap', 'ADR TSO', 'IPOyear', 'sector', 'industry', 'Summary Quote', ''])
	
	for row in exchange_file:
		symbol_list.append(row)

	return symbol_list	


