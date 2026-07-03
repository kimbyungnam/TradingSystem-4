from typing import Protocol


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
    ...


class AutoTradingSystem:
    def select_stock_brocker(self, broker_name):
        self.stock_broker = broker_name

    @property
    def stock_brocker(self):
        return self._stock_broker

    @stock_brocker.setter
    def stock_brocker(self, broker_name):
        self._stock_broker = broker_name
