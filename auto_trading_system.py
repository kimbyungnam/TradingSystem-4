from typing import Protocol
import time


class StockBrocker(Protocol):
    @property
    def name(self) -> str: ...

    def login(self, id: str, pw: str): ...

    def buy(self, stock_code: str, price: int, count: int): ...

    def sell(self, stock_code: str, price: int, count: int): ...

    def get_price(self, stock_code: str): ...


class KiwerStockBrocker(StockBrocker):
    def __init__(self, kiwer_api):
        self._kiwer_api = kiwer_api

    @property
    def name(self):
        return 'kiwer'

    def login(self, id: str, pw: str):
        self._kiwer_api.login(id, pw)

    def buy(self, stock_code: str, price: int, count: int):
        self._kiwer_api.buy(stock_code, price, count)

    def sell(self, stock_code: str, price: int, count: int):
        self._kiwer_api.sell(stock_code, price, count)

    def get_price(self, stock_code: str):
        return self._kiwer_api.current_price(stock_code)


class NemoStockBrocker(StockBrocker):
    def __init__(self, nemo_api):
        self._nemo_api = nemo_api

    @property
    def name(self):
        return 'nemo'

    def login(self, id: str, pw: str):
        self._nemo_api.certification(id, pw)

    def buy(self, stock_code: str, price: int, count: int):
        self._nemo_api.purchasing_stock(stock_code, price, count)

    def sell(self, stock_code: str, price: int, count: int):
        self._nemo_api.selling_stock(stock_code, price, count)

    def get_price(self, stock_code: str):
        return self._nemo_api.get_market_price(stock_code)


class AutoTradingSystem:
    def __init__(self):
        self._delay_period = 0.2
        self._n_check = 3

    def create_stock_brocker(self, broker: StockBrocker):
        self.stock_brocker = broker

    @property
    def stock_brocker(self):
        return self._stock_broker

    @stock_brocker.setter
    def stock_brocker(self, broker):
        self._stock_broker = broker

    def login(self, id: str, pw: str):
        self.stock_brocker.login(id, pw)

    def buy(self, stock_code: str, price: int, count: int):
        self.stock_brocker.buy(stock_code, price, count)

    def get_price(self, stock_code: str) -> int:
        return self.stock_brocker.get_price(stock_code)

    def sell(self, stock_code: str, price: int, count: int):
        self.stock_brocker.sell(stock_code, price, count)

    def _is_buy(self, price_s):
        for idx in range(1, len(price_s)):
            if price_s[idx-1] >= price_s[idx]:
                return False
        return True

    def buy_nice_timing(self, stock_code: str, price: int):
        price_s = [self.get_price(stock_code)]
        for _ in range(self._n_check-1):
            time.sleep(0.2)
            price_s.append(self.get_price(stock_code))
        last_price = price_s[-1]
        if last_price > 0 and price // last_price >=1 and self._is_buy(price_s):
            self.stock_brocker.buy(stock_code, last_price, price // last_price)

    def sell_nice_timing(self, stock_code: str, count: int):
        price1 = self.get_price(stock_code)
        time.sleep(0.2)
        price2 = self.get_price(stock_code)
        time.sleep(0.2)
        price3 = self.get_price(stock_code)
        if price1 > price2 and price2 > price3:
            self.stock_brocker.sell(stock_code, price3, count)
