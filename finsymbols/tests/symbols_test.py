from unittest import TestCase, main
import sys
import os

from finsymbols import symbols


class TestSizeOfList(TestCase):
    def test_sp500_size(self):
        sp500 = symbols.get_sp500_symbols()
        assert len(sp500) == 502 , 'len gathered data: {}. Expected len: 502'.format(len(sp500))

    def test_amex_not_null(self):
        amex = symbols.get_amex_symbols()
        assert len(amex) != 0,'AMEX list is of size 0'

    def test_nyse_not_null(self):
        nyse = symbols.get_nyse_symbols()
        assert len(nyse) != 0,'NYSE list is of size 0'

    def test_nasdaq_not_null(self):
        nasdaq = symbols.get_nasdaq_symbols()
        assert len(nasdaq) != 0,'NASDAQ list is of size 0'


if __name__ == '__main__':
	main()
