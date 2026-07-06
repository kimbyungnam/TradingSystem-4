import pytest
from pytest_mock import MockerFixture

from auto_trading_system import NemoStockBrocker


@pytest.fixture
def nemo_api(mocker: MockerFixture):
    print("nemo")
    return mocker.Mock()


@pytest.fixture
def brocker(nemo_api):
    return NemoStockBrocker(nemo_api)


def test_nemo_stock_brocker_name(brocker):
    assert brocker.name == "nemo"


def test_nemo_stock_brocker_login(nemo_api, brocker):
    # Action
    brocker.login("ID_NOT_IMPORTANT", "PW_NOT_IMPORTANT")

    # Assert
    nemo_api.certification.assert_called_once_with("ID_NOT_IMPORTANT", "PW_NOT_IMPORTANT")


def test_nemo_stock_brocker_buy(nemo_api, brocker):
    # Action
    brocker.buy("Stock1", 1000, 3)

    # Assert
    nemo_api.purchasing_stock.assert_called_once_with("Stock1", 1000, 3)


def test_nemo_stock_brocker_sell(nemo_api, brocker):
    # Action
    brocker.sell("Stock1", 1000, 3)

    # Assert
    nemo_api.selling_stock.assert_called_once_with("Stock1", 1000, 3)


def test_nemo_stock_brocker_get_price(nemo_api, brocker):
    # Action
    brocker.get_price("Stock1")

    # Assert
    nemo_api.get_market_price.assert_called_once()
