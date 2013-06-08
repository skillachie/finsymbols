from unittest import TestCase, main
import sys
import os
sys.path.append('../')
import symbols

class test_size_of_list(TestCase):
	def test_sp500_size(self):
		sp500 = symbols.get_sp500_symbols()
  		assert len(sp500) == 500 ,'The S&P 500 is no more'
	

	def test_not_null(self):
		amex = symbols.get_amex_symbols()
		assert len(amex) != 0,'AMEX list is of size 0'

		nyse = symbols.get_nyse_symbols()
		assert len(nyse) != 0,'NYSE list is of size 0'

		nasdaq = symbols.get_nasdaq_symbols()
		assert len(nasdaq) != 0,'NASDAQ list is of size 0'
		

if __name__ == '__main__':
	main()	
