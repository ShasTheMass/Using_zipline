import pytz
from datetime import datetime
import zipline
from zipline.api import order, record, symbol
from zipline.algorithm import TradingAlgorithm
from zipline.utils.factory import load_bars_from_yahoo

start = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)
end = datetime(2016, 1, 1, 0, 0, 0, 0, pytz.utc)
data = load_bars_from_yahoo(stocks=['AAPL'], start=start,
                            end=end)

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 100)
    record(AAPL=data[symbol('AAPL')].price)

algo_obj = TradingAlgorithm(initialize=initialize,
                            handle_data=handle_data)

perf_manual = algo_obj.run(data)

print(perf_manual)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
perf_manual.ending_cash.plot(ax=ax)
#results.portfolio_value.plot(ax=ax)
ax.set_ylabel('Portfolio value (USD)')
plt.show()
print("The end.")
