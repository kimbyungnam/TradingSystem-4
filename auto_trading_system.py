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
    def select_stock_brocker(self, broker_name):
        self.stock_broker = broker_name

    @property
    def stock_brocker(self):
        return self._stock_broker

    @stock_brocker.setter
    def stock_brocker(self, broker_name):
        self._stock_broker = broker_name

    def buy(self, stock_code: str, price: int, count: int):
        self.stock_brocker.buy(stock_code, price, count)

    def get_price(self, stock_code: str) -> int:
        return self.stock_brocker.get_price(stock_code)

    def buy_nice_timing(self, stock_code: str, price: int):
        price1 = self.get_price(stock_code)
        time.sleep(0.2)
        price2 = self.get_price(stock_code)
        time.sleep(0.2)
        price3 = self.get_price(stock_code)
        if price1 < price2 and price2 < price3:
            self.stock_brocker.buy(stock_code, price3, price // price3)
