from typing import Protocol


class StockBrocker(Protocol):
    def login(self, id: str, pw: str): ...

    def buy(self, stock_code: str, price: int, count: int): ...

    def sell(self, stock_code: str, price: int, count: int): ...

    def get_price(self, stock_code: str): ...


class AutoTradingSystem:
    def select_stock_broker(self, broker_name):
        self.stock_broker = broker_name

    @property
    def stock_broker(self):
        return self._stock_broker

    @stock_broker.setter
    def stock_broker(self, broker_name):
        self._stock_broker = broker_name

    stock_brocker: StockBrocker = None
    def login(self, id, pw):
        self.stock_brocker.login(id, pw)
