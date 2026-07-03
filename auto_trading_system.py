from typing import Protocol


class StockBrocker(Protocol):
    @property
    def name(self) -> str: ...

    def login(self, id: str, pw: str): ...

    def buy(self, stock_code: str, price: int, count: int): ...

    def sell(self, stock_code: str, price: int, count: int): ...

    def get_price(self, stock_code: str): ...


class KiwerStockBrocker(StockBrocker):
    ...


class AutoTradingSystem:
    def select_stock_broker(self, broker_name):
        self.stock_broker = broker_name

    @property
    def stock_broker(self):
        return self._stock_broker

    @stock_broker.setter
    def stock_broker(self, broker_name):
        self._stock_broker = broker_name
