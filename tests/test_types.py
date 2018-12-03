from decimal import InvalidOperation

import pytest
from binance.types import Results, Trading, format_fee


def test_results_attributes():
    tr = Results(
        datetime_value='2018-11-13 01:58:03',
        pair='STORMBTC',
        type_operation='SELL',
        order_price='0.0',
        order_amount='2200.0',
        avg_trading_price='0.00000126',
        filled='2200.0',
        total='0.002772',
        status='Filled'
    )

    assert tr.datetime_value
    with pytest.raises(ValueError):
        tr.datetime_value = 'a'
    assert tr.pair
    assert tr.type_operation
    assert tr.order_price
    assert tr.order_amount
    assert tr.avg_trading_price
    assert tr.filled
    assert tr.total
    assert tr.status

    with pytest.raises(InvalidOperation):
        tr.order_price = 'a'
    with pytest.raises(InvalidOperation):
        tr.order_amount = 'a'
    with pytest.raises(InvalidOperation):
        tr.avg_trading_price = 'a'
    with pytest.raises(InvalidOperation):
        tr.filled = 'a'
    with pytest.raises(InvalidOperation):
        tr.total = 'a'


def test_trading_attributes():
    tr = Trading(
        datetime_value='2018-11-13 01:58:03',
        filled='0.00000126',
        total='2200',
        fee='0.00277200',
        fee_coin='0.00141268BNB'
    )

    assert tr.datetime_value
    assert tr.filled
    assert tr.total
    assert tr.fee
    assert tr.fee_coin

    with pytest.raises(ValueError):
        tr.datetime_value = 'a'
    with pytest.raises(InvalidOperation):
        tr.filled = 'a'
    with pytest.raises(InvalidOperation):
        tr.total = 'a'
    with pytest.raises(InvalidOperation):
        tr.fee = 'a'


def test_format_fee():
    a, b = format_fee('0.01BTC')
    assert a == '0.01'
    assert b == 'BTC'

    a, b = format_fee('BTC')
    assert a is None
    assert b == 'BTC'

    a, b = format_fee('0.01')
    assert a == '0.01'
    assert b is None
