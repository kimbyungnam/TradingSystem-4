from typing import Protocol


class StockBrocker(Protocol):
    def login(self, id: str, pw: str): ...

    def buy(self, stock_code: str, price: int, count: int): ...

    def sell(self, stock_code: str, price: int, count: int): ...

    def get_price(self, stock_code: str): ...


class AutoTradingSystem:
    stock_brocker = None
    def sell(self, stock_code: str, price: int, count: int):
        self.stock_brocker.sell(stock_code, price, count)