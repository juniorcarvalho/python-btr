import pytest
from binance.binance import TradingResult


@pytest.fixture
def file_result_trading():
    return TradingResult('tests/OrderHistory.xlsx')

