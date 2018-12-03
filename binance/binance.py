import os

import xlrd
from binance.types import Results, Trading
from datetime import datetime

class TradingResult:
    def __init__(self, file_name):
        if not os.path.isfile(file_name):
            raise OSError('File {} not found.'.format(file_name))
        self.file_name = file_name

        try:
            self.plan = xlrd.open_workbook(self.file_name)
        except Exception:
            raise Exception('Error while trying to open {}'.format(self.file_name))

        try:
            self.sheet = self.plan.sheet_by_index(0)
        except Exception:
            raise Exception('error while trying to read sheet by index 0')

        self.header = list()
        self.header.append('Date(UTC)')
        self.header.append('Pair')
        self.header.append('Type')
        self.header.append('Order Price')
        self.header.append('Order Amount')
        self.header.append('Avg Trading Price')
        self.header.append('Filled')
        self.header.append('Total')
        self.header.append('status')

        if not self.__valid_header():
            raise Exception('Invalid header')

    def import_file(self):
        results = []
        for rx in range(self.sheet.nrows)[1:]:
            line = self.sheet.row(rx)
            if (str(line[0].value) != self.header[0]) and (str(line[0]) != "empty:''"):
                results.append(Results(line[0].value,
                                       line[1].value,
                                       line[2].value,
                                       line[3].value,
                                       line[4].value,
                                       line[5].value,
                                       line[6].value,
                                       line[7].value,
                                       line[8].value
                                       )
                               )
            if len(str(line[0].value)) == 0:
                try:
                    date_read = datetime.strptime(line[1].value, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    date_read = None

                if date_read is not None:
                    trading = Trading(date_read,
                                      line[2].value,
                                      line[3].value,
                                      line[4].value,
                                      line[5].value)
                    results[-1].trading.append(trading)
        return results

    def __valid_header(self):
        header_read = [str(cell.value) for cell in self.sheet.row(0)]
        if self.header == header_read:
            return True
        return False
