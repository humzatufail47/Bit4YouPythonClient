from Bit4YouClient import GetAccesstoken, GetUserInfo, MarketList, MarketSummaries, GetMarketTicks, \
    GetMarketOrderBook, GetMarketHistory, WalletBalance, GetWalletTransaction, GetWalletFunds, GetOrderList, \
    GetOrderInfo, GetOrderPending, GetOrderCreate, GetOrderCancel, GetPortfolioSummary, GetPortfolioOpenOrder, \
    GetPortfolioHistory, GetPortfolioCreateOrder, GetPortfolioCancelOrder, GetPortfolioCloseOrder
from Models.Makret.Request.MarketHistory import MarketHistory
from Models.Makret.Request.MarketOrderBook import MarketOrderBook
from Models.Makret.Request.MarketTicks import MarketTicks
from Models.Order.Request.OrderCreate import CreateOrder
from Models.Order.Request.OrderCancel import OrderCancel
from Models.Order.Request.OrderInfo import OrderInfo
from Models.Order.Request.OrderList import OrderListRequest
from Models.Portfolio.Request.PorfolioCancelOrder import CancelPorfolioOrder
from Models.Portfolio.Request.PortfolioClosePosition import ClosePortfolioPosition
from Models.Portfolio.Request.PortfolioCreateOrder import PortfolioCreateOrder
from Models.Simulation import Simulation
from Models.Wallet.Request.WalletFunds import WalletFunds
from Models.Wallet.Request.WalletTransaction import WalletTransaction

print('--------------------------Print Access Token Object-----------------------------')
print(GetAccesstoken().toJSON())
print('--------------------------Print User Info Object-----------------------------')
print(GetUserInfo().toJSON())
print('--------------------------Print Market List Object-----------------------------')
for marketls in MarketList():
    print(marketls.toJSON())

print('--------------------------Print Market Summary Object-----------------------------')
for marketsummary in MarketSummaries():
    print(marketsummary.toJSON())

print('--------------------------Print Market Ticks Object-----------------------------')
for marketTicks in GetMarketTicks(MarketTicks("USDT-BTC", 60,"","")):
    print(marketTicks.toJSON())

print('--------------------------Print Market Order Book Object-----------------------------')
print(GetMarketOrderBook(MarketOrderBook("USDT-BTC", 50, False,"","")).toJSON())

print('--------------------------Print Market History Object-----------------------------')
for markethis in GetMarketHistory(MarketHistory("USDT-BTC", 50, "string", "string","","")):
    print(markethis.toJSON())


print('--------------------------Print Wallet Balance Object-----------------------------')
for walletbal in WalletBalance(Simulation(True,"","")):
    print(walletbal.toJSON())

print('--------------------------Print Wallet Transaction Book Object-----------------------------')
print(GetWalletTransaction(WalletTransaction("BTC", True,"","")).toJSON())
print('--------------------------Print Wallet Funds Object-----------------------------')
try:
    GetWalletFunds(WalletFunds("BTC", 1.05, "1CK6KHY6MHgYvmRQ4PAafKYDrg1eaaaaaa","",""))
except:
    print('401 unAuth')


print('--------------------------Print Order List Object-----------------------------')
for orderls in GetOrderList(OrderListRequest(0, 10, "USDT-BTC", True,"","")):
    print(orderls.toJSON())

print('--------------------------Print Order Info Object-----------------------------')
print(GetOrderInfo(OrderInfo("db78faa89f08062bfebeacb51365fadb08b63da6", True,"","")).toJSON())

print('--------------------------Print Pending Object-----------------------------')
for orderpen in GetOrderPending(Simulation(True,"","")):
    print(orderpen.toJSON())

print('--------------------------Print Order Create Object-----------------------------')
result=GetOrderCreate(CreateOrder("USDT-BTC", "buy", 10, "BTC", 1.5, True,"",""))
print(result.toJSON())

print('--------------------------Print Order Cancel Object-----------------------------')
print(GetOrderCancel(OrderCancel(result.txid, False,"","")).toJSON())

print('--------------------------Print Portfolio Summary Object-----------------------------')
print(GetPortfolioSummary(Simulation(True,"","")).toJSON())

print('--------------------------Print Portfolio open order Object-----------------------------')
for POpenOrder in GetPortfolioOpenOrder(Simulation(True,"","")):
    print(POpenOrder.toJSON())

print('--------------------------Print Portfolio History Object-----------------------------')
for POpenOrder in GetPortfolioHistory(Simulation(True,"","")):
    print(POpenOrder.toJSON())

print('--------------------------Print Portfolio Create Order Object-----------------------------')
print(GetPortfolioCreateOrder(PortfolioCreateOrder("USDT-BTC", 0.55, 3555.36, True,"","")).toJSON())

print('--------------------------Print Portfolio Cancel Order Object-----------------------------')
print(GetPortfolioCancelOrder(CancelPorfolioOrder(1, False,"","")).toJSON())

print('--------------------------Print Portfolio Close Order Object-----------------------------')
print(GetPortfolioCloseOrder(ClosePortfolioPosition(1, True,"","")).toJSON())
