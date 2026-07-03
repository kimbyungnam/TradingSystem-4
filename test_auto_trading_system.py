from auto_trading_system import AutoTradingSystem


def test_select_stock_broker_kiwer():
    # Arrange
    sut = AutoTradingSystem()

    # Action
    sut.select_stock_broker("kiwer")

    # Assert
    assert sut.stock_broker == "kiwer"


def test_select_stock_broker_nemom():
    # Arrange
    sut = AutoTradingSystem()

    # Action
    sut.select_stock_broker("nemo")

    # Assert
    assert sut.stock_broker == "nemo"
