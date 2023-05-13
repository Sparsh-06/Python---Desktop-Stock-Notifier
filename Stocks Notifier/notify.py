import datetime
import time
from plyer import notification
import yfinance as yf

msft = yf.Ticker("^NSEI")
data = msft.info
while True:
    notification.notify(
    title = "Nifty 50".format(datetime.date.today()),
    message = "Open Price = {cp} \n Previous Price = {dl} \nDay-Low = {dh}".format(cp = data["open"], dl = data["previousClose"], dh = data["dayLow"]),
    app_icon = "download.ico",
    timeout = 10
    )
    time.sleep(60*60*2)
