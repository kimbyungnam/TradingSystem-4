from pytest_mock import MockerFixture

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
