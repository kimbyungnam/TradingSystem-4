import pytest
from pytest_mock import MockerFixture

from auto_trading_system import KiwerStockBrocker


@pytest.fixture
def kiwer_api(mocker: MockerFixture):
    return mocker.Mock()


@pytest.fixture
def brocker(kiwer_api):
    return KiwerStockBrocker(kiwer_api)


def test_kiwer_stock_brocker_name(brocker):
    assert brocker.name == "kiwer"


def test_kiwer_stock_brocker_login(kiwer_api, brocker):
    # Action
    brocker.login("ID_NOT_IMPORTANT", "PW_NOT_IMPORTANT")

    # Assert
    kiwer_api.login.assert_called_once_with("ID_NOT_IMPORTANT", "PW_NOT_IMPORTANT")


def test_kiwer_stock_brocker_buy(kiwer_api, brocker):
    # Action
    brocker.buy("Stock1", 1000, 3)

    # Assert
    kiwer_api.buy.assert_called_once_with("Stock1", 1000, 3)


def test_kiwer_stock_brocker_sell(kiwer_api, brocker):
    # Action
    brocker.sell("Stock1", 1000, 3)

    # Assert
    kiwer_api.sell.assert_called_once_with("Stock1", 1000, 3)


def test_kiwer_stock_brocker_get_price(kiwer_api, brocker):
    # Action
    brocker.get_price("Stock1")

    # Assert
    kiwer_api.current_price.assert_called_once_with("Stock1")
