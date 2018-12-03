from datetime import datetime
from decimal import Decimal, InvalidOperation
import re

class Results(object):
    def __init__(self, datetime_value, pair, type_operation, order_price, order_amount, avg_trading_price, filled,
                 total, status):
        self._datetime = datetime_value
        self._pair = pair
        self._type_operation = type_operation
        self._order_price = order_price
        self._order_amount = order_amount
        self._avg_trading_price = avg_trading_price
        self._filled = filled
        self._total = total
        self._status = status
        self._trading = []

    @property
    def datetime_value(self):
        return self._datetime

    @datetime_value.setter
    def datetime_value(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise ValueError
        self._datetime = value

    @property
    def pair(self):
        return self._pair

    @pair.setter
    def pair(self, value):
        self._pair = value

    @property
    def type_operation(self):
        return self._type_operation

    @type_operation.setter
    def type_operation(self, value):
        self._type_operation = value

    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._order_price = value

    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._order_amount = value

    @property
    def avg_trading_price(self):
        return self._avg_trading_price

    @avg_trading_price.setter
    def avg_trading_price(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._avg_trading_price = value

    @property
    def filled(self):
        return self._filled

    @filled.setter
    def filled(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._filled = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._total = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def trading(self):
        return self._trading

    @trading.setter
    def trading(self, value):
        self._trading = value

    def get_json(self):
        value = self
        trading = self._trading
        if isinstance(trading, list):
            value.trading = []
            for item in trading:
                value.trading.append(item.__dict__)
            return value.__dict__
        else:
            value.trading = ''
            return value.__dict__


class Trading(object):
    def __init__(self, datetime_value, filled, total, fee, fee_coin):
        self._datetime = datetime_value
        self._filled = filled
        self._total = total
        self._fee = fee
        self._fee_coin = fee_coin

    @property
    def datetime_value(self):
        return self._datetime

    @datetime_value.setter
    def datetime_value(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise ValueError
        self._datetime = value

    @property
    def filled(self):
        return self._filled

    @filled.setter
    def filled(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._filled = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._total = value

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        if isinstance(value, str):
            try:
                value = Decimal(value)
            except InvalidOperation:
                raise InvalidOperation
        self._fee = value

    @property
    def fee_coin(self):
        return self._fee_coin

    @fee_coin.setter
    def fee_coin(self, value):
        self._fee_coin = value


def format_fee(text):
    pattern = re.compile('([0-9,.]+)')
    fee = pattern.findall(text)
    if len(fee) == 0:
        fee = None
    else:
        fee = Decimal(fee[0])

    pattern = re.compile('([A-Z,a-z]+)')
    fee_coin = pattern.findall(text)
    if len(fee_coin) == 0:
        fee_coin = None
    else:
        fee_coin = fee_coin[0]

    if fee is not None:
        fee = str(fee)

    return fee, fee_coin
