import pytest
from binance.binance import TradingResult


def test_parameter():
    with pytest.raises(TypeError) as exec:
        TradingResult()
        assert (str(exec.value)) == "__init__() missing 1 required positional argument: 'file_name'"

    with pytest.raises(OSError):
        TradingResult('test.txt')

    with pytest.raises(Exception) as exec:
        TradingResult('tests/OrderHistoryInvalidHeader.xlsx')
        assert (str(exec.value)) == 'Invalid header'


def test_instance_variables(file_result_trading):
    assert file_result_trading.file_name


def test_import_results(file_result_trading):
    data = {
        '_datetime': '2018-11-13 01:58:03',
        '_pair': 'STORMBTC',
        '_type_operation': 'SELL',
        '_order_price': '0.0',
        '_order_amount': '2200.0',
        '_avg_trading_price': '0.00000126',
        '_filled': '2200.0',
        '_total': '0.002772',
        '_status': 'Filled',
        '_trading': [
            {
                '_datetime': 'Date(UTC)',
                '_filled': 'Trading Price',
                '_total': 'Filled',
                '_fee': 'Total',
                '_fee_coin': 'Fee'
            },
            {
                '_datetime': '2018-11-13 01:58:03',
                '_filled': '0.00000126',
                '_total': '2200',
                '_fee': '0.00277200',
                '_fee_coin': '0.00141268BNB'
            }
        ]
    }
    results = file_result_trading.import_file()
    assert results[0].get_json() == data
