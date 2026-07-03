from typing import Protocol


class StockBrocker(Protocol):
    def login(self, id: str, pw: str): ...

    def buy(self, stock_code: str, price: int, count: int): ...

    def sell(self, stock_code: str, price: int, count: int): ...

    def get_price(self, stock_code: str): ...


class KiwerStockBrocker:
    def __init__(self, kiwer_api):
        self.kiwer_api = kiwer_api

    def login(self, id: str, pw: str):
        self.kiwer_api.login(id, pw)


