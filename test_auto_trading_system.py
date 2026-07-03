from auto_trading_system import AutoTradingSystem


def test_select_stock_brocker_kiwer():
    # Arrange
    sut = AutoTradingSystem()

    # Action
    sut.select_stock_brocker("kiwer")

    # Assert
    assert sut.stock_brocker.name == "kiwer"


def test_select_stock_brocker_nemo():
    # Arrange
    sut = AutoTradingSystem()

    # Action
    sut.select_stock_brocker("nemo")

    # Assert
    assert sut.stock_brocker.name == "nemo"
