import urllib2
import os
import sys
import csv
import datetime
import pprint


def is_connected():
    '''
    Checks internet connectivity
    '''
    try:
        urllib2.urlopen("http://google.com", timeout=2)
        return True
    except urllib2.URLError:
        return False

def is_cached(file_path):
    '''
    Checks if the file cached is still valid
    '''
    file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
    current_time = datetime.datetime.now()
    file_age = (current_time - file_time).total_seconds()
    
    if(file_age > 86400 and is_connected()):
        print "The file is old"
        return False
    elif(is_connected()):
        print "The file is cached"
        return True
    else:
        print "Not connected to the internet using last obtained file"
        return True



def fetch_file(url):
        '''
        Gets and downloads files
        '''
        file_fetcher = urllib2.build_opener()
        file_fetcher.addheaders =  [('User-agent', 'Mozilla/5.0')]
        file_data = file_fetcher.open(url).read()
        return file_data

def wiki_html(url,file_name):
    ''' 
    Obtains html from Wikipedia
    Note: API exist but for my use case. Data returned was not parsable. Preferred to use html
    python-wikitools - http://code.google.com/p/python-wikitools/
    Ex. http://en.wikipedia.org/w/api.php?format=xml&action=query&titles=List_of_S%26P_500_companies&prop=revisions&rvprop=content
    '''
    module_path = os.path.dirname(os.path.realpath(__file__))
    exchanges_dir = os.path.join(module_path,'exchanges')
    file_path = os.path.abspath(exchanges_dir) + os.sep + file_name
   
    if(os.path.exists(file_path) and is_cached(file_path)):
        opener = urllib2.build_opener()
        return opener.open("file://" + file_path).read()
    else:
        wiki_html = fetch_file('http://en.wikipedia.org/wiki/'+str(url))
        saved_file = open(file_path , "w")
        saved_file.write(wiki_html)
        saved_file.close()
        return wiki_html


def get_csv(exchange):
    '''
    Downloads the symbol list for each exchange from Nasdaq
    '''    
    module_path = os.path.dirname(os.path.realpath(__file__))
    exchanges_dir = os.path.join(module_path,'exchanges')
    file_path = os.path.abspath(exchanges_dir) + os.sep + exchange + '.csv'
    
    if(os.path.exists(file_path) and is_cached(file_path)):
        return file_path 
    else:
        csv_file = fetch_file('http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange='+str(exchange)+'&render=download')
        saved_file = open(file_path , "w")
        saved_file.write(csv_file)
        saved_file.close()
        return file_path

def read_csv(exchange):
    '''  
    Reads symbols in csv file as dict
    '''
    symbol_list = list()
    file_path = get_csv(exchange)
    exchange_file = csv.DictReader(open(file_path),fieldnames=['symbol', 'company', 'LastSale', 'MarketCap', 'ADR TSO', 'IPOyear', 'sector', 'industry', 'Summary Quote', ''])
    next(exchange_file, None)
	
    for row in exchange_file:
        symbol_list.append(row)

    return symbol_list	


