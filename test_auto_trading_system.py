from pytest_mock import MockerFixture

from auto_trading_system import AutoTradingSystem





def test_get_price(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")
    mock_brocker.get_price.return_value = 2000

    # Action
    price = sut.get_price("Stock1")

    # Assertion
    assert price == 2000
