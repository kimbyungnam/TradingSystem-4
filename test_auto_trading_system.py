from pytest_mock import MockerFixture

from auto_trading_system import AutoTradingSystem, KiwerStockBrocker


def test_create_stock_brocker_kiwer(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_broker = mocker.Mock()
    mock_broker.name = 'kiwer'

    # Action
    sut.create_stock_brocker(mock_broker)

    # Assert
    assert sut.stock_brocker.name == "kiwer"


def test_create_stock_brocker_nemo(mocker):
    # Arrange
    sut = AutoTradingSystem()
    mock_broker = mocker.Mock()
    mock_broker.name = 'nemo'

    # Action
    sut.create_stock_brocker(mock_broker)

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


def test_sell(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")

    # Action
    sut.sell("Stock1", 1000, 2)

    # Assertion
    mock_brocker.sell.assert_called_once_with("Stock1", 1000, 2)


def test_get_price(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")
    mock_brocker.get_price.return_value = 2000

    # Action
    price = sut.get_price("Stock1")

    # Assertion
    assert price == 2000


def test_buy_nice_timing_get_price_3_times(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")
    mock_sleep = mocker.patch("auto_trading_system.time.sleep")

    calls = []

    def mock_get_price(stock_code):
        calls.append(("get_price", stock_code))
        return 0

    def mock_sleep_side_effect(seconds):
        calls.append(("sleep", seconds))

    mock_brocker.get_price.side_effect = mock_get_price
    mock_sleep.side_effect = mock_sleep_side_effect

    # Action
    sut.buy_nice_timing("Stock1", 1000)

    # Assert
    assert calls == [
        ("get_price", "Stock1"),
        ("sleep", 0.2),
        ("get_price", "Stock1"),
        ("sleep", 0.2),
        ("get_price", "Stock1"),
    ]


def test_buy_nice_timing_rising_trend_buy(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")
    mock_brocker.get_price.side_effect = [100, 200, 300]

    # Action
    sut.buy_nice_timing("Stock1", 1000)

    # Assert
    mock_brocker.buy.assert_called_once_with("Stock1", 300, 3)


def test_sell_nice_timing_get_price_3_times(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")
    mock_sleep = mocker.patch("auto_trading_system.time.sleep")

    calls = []

    def mock_get_price(stock_code):
        calls.append(("get_price", stock_code))
        return 0

    def mock_sleep_side_effect(seconds):
        calls.append(("sleep", seconds))

    mock_brocker.get_price.side_effect = mock_get_price
    mock_sleep.side_effect = mock_sleep_side_effect

    # Action
    sut.sell_nice_timing("Stock1", 3)

    # Assert
    assert calls == [
        ("get_price", "Stock1"),
        ("sleep", 0.2),
        ("get_price", "Stock1"),
        ("sleep", 0.2),
        ("get_price", "Stock1"),
    ]


def test_sell_nice_timing_falling_trend_sell(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")
    mock_brocker.get_price.side_effect = [300, 200, 100]

    # Action
    sut.sell_nice_timing("Stock1", 3)

    # Assert
    mock_brocker.sell.assert_called_once()


def test_sell_nice_timing_falling_trend_sell_all_last_price(mocker: MockerFixture):
    # Arrange
    sut = AutoTradingSystem()
    mock_brocker = mocker.patch("auto_trading_system.AutoTradingSystem.stock_brocker")
    mock_brocker.get_price.side_effect = [300, 200, 100]

    # Action
    sut.sell_nice_timing("Stock1", 3)

    # Assert
    mock_brocker.sell.assert_called_once_with("Stock1", 100, 3)
