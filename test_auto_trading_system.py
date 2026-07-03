from pytest_mock import MockerFixture

from auto_trading_system import AutoTradingSystem


def test_select_stock_broker_kiwer():
    # Arrange
    sut = AutoTradingSystem()

    # Action
    sut.select_stock_broker("kiwer")

    # Assert
    assert sut.stock_broker == "kiwer"


def test_select_stock_broker_nemo():
    # Arrange
    sut = AutoTradingSystem()

    # Action
    sut.select_stock_broker("nemo")

    # Assert
    assert sut.stock_broker == "nemo"


def test_login(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")

    # Action
    sut.login("ID_NOT_IMPORTANT", "PW_NOT_IMPORTANT")

    # Assertion
    mock_brocker.login.assert_called_once_with("ID_NOT_IMPORTANT", "PW_NOT_IMPORTANT")
    pass


def test_buy(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")

    # Action
    sut.buy("Stock1", 1000, 2)

    # Assertion
    mock_brocker.buy.assert_called_once_with("Stock1", 1000, 2)


def test_sell(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")

    # Action
    sut.sell("Stock1", 1000, 2)

    # Assertion
    mock_brocker.sell.assert_called_once_with("Stock1", 1000, 2)
