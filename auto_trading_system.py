class AutoTradingSystem:
    def select_stock_broker(self, broker_name):
        self.stock_broker = broker_name

    @property
    def stock_broker(self):
        return self._stock_broker
    @stock_broker.setter
    def stock_broker(self, broker_name):
        self._stock_broker = broker_name