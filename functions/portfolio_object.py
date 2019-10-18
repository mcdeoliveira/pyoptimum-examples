import pandas as pd
from functions.portfolio_io import get_data_for_ticker

class PortfolioObject():

    def __init__(self, ticker_list):
        self.ticker_list = ticker_list
        self.df = None
        self.calc_return = None
        self.covariance_matrix = None

        # start of data processing
        self._build_df_of_price_data()
        self._get_calc_return_covariance()


    def _build_df_of_price_data(self):
        for j, ticker in enumerate(self.ticker_list):
            tmp, stock_split = get_data_for_ticker(ticker)
            tmp.columns = [ticker]
            print(ticker, stock_split)
            if j == 0:
                self.df = tmp
            else:
                self.df = self.df.join(tmp, how='inner', rsuffix='1')

    def _get_calc_return_covariance(self):
        self.calc_return = pd.Series(name='return',index=self.df.columns)
        for ticker in self.df.columns:
            tmp = self.df.loc[:,[ticker]]
            return_val = tmp.values[-1:]/tmp.values[0] - 1
            if return_val < 0:
                print('Symbol {} has 1 year negative return {}'.format(return_val))
            self.calc_return.loc[ticker] = return_val
        self.covariance_matrix = self.df.cov()


