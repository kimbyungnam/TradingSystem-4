from auto_trading_system import AutoTradingSystem
from pytest_mock import MockerFixture

def test_select_stock_broker():
    # Arrange
    sut = AutoTradingSystem()

    # Action
    sut.select_stock_broker("kiwer")

    # Assert
    assert sut.stock_broker == "kiwer"

def test_get_price(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_broker")
    mock_brocker.get_price.return_value = 2000

    # Action
    price = sut.get_price("Stock1")

    # Assertion
    assert price == 2000

