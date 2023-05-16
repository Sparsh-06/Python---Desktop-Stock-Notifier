import datetime
import time
from plyer import notification
import yfinance as yf

ask = input("Which stock do you want to keep your eye on ? [^NSEI , ^NSEBANK , RELIANCE>NS , ^BSESN]")
# Ticker of Stocks.
stk = yf.Ticker(f"{ask}")
data = stk.info
while True:
    notification.notify(
    title = "Nifty 50".format(datetime.date.today()),
    message = "Open Price = {cp} \n Previous Price = {dl} \nDay-Low = {dh}".format(cp = data["open"], dl = data["previousClose"], dh = data["dayLow"]),
    # Icon must be in "xyz.ico"
    app_icon = "download.ico",
    timeout = 10
    )
    # For every 2 hours
    time.sleep(60*60*2)
