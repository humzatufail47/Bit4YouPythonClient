from Models.Portfolio.Response.CancelPortfolioResponse import CancelPortfolioResponse
from Models.Portfolio.Request.CancelPorfolioOrder import CancelPorfolioOrder
from Models.Portfolio.Response.CreatePortfolioResponse import CreatePortfolioResponse
from Models.Portfolio.Response.PortfolioHistoryResponse import PortfolioHistoryResponse
from Models.Order.Response.OrderCancelResponse import OrderCancelResponse
from Models.Order.Response.CreateOrderResponse import CreateOrderResponse
from Models.Order.Response.OrderPendingResponse import OrderPendingResponse
from Models.Order.Response.OrderInfoResponse import OrderInfoResponse
from Models.Order.Response.OrderListResponse import OrderListResponse
from Models.Wallet.Response.WalletTransactionResponse import WalletTransactionResponse
from Models.Wallet.Response.WalletBalanceResponse import WalletBalanceResponse
from Models.Makret.Response.MarketHistoryResponse import MarketHistoryResponse
from Models.Makret.Response.MarketOrderBookResponse import MarketOrderBookResponse
from Models.Makret.Response.MarketTicksResponse import MarketTicksResponse
from Models.Makret.Response.MarketSummrieResponse import MarketSummrieResponse
from Models.Makret.Response.MarketListResponse import MarketListResponse
from Models.Portfolio.Request.ClosePortfolioPosition import ClosePortfolioPosition
from Models.Portfolio.Request.PortfolioCreateOrder import PortfolioCreateOrder
from Models.Order.Request.OrderCancel import OrderCancel
from Models.Order.Request.CreateOrder import CreateOrder
from Models.Order.Request.OrderInfo import OrderInfo
from Models.Order.Request.OrderListRequest import OrderListRequest
from Models.Wallet.Request.WalletFunds import WalletFunds
from Models.Wallet.Request.WalletTransaction import WalletTransaction
from Models.Simulation import Simulation
from Models.Makret.Request.MarketHistory import MarketHistory
from Models.Makret.Request.MarketOrderBook import MarketOrderBook
from Models.Makret.Request.MarketTicks import MarketTicks
from Models.OAuthRequest import OAuthRequest
from Models.OAuthResult import OAuthResult
from requests.models import Response
from Models.Portfolio.Response.PortfolioOpenOrderResponse import PortfolioOpenOrderResponse
from Models.UserInfo import UserInfo
from Models.Portfolio.Response.PortfolioListResponse import PortfolioListResponse
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import json
from cachetools import TTLCache
import re
cache = TTLCache(maxsize=10, ttl=1440)


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def GetAccesstoken():
    token = cache.get("access_token")
    if token is not None:
        return token
    url = (os.environ.get("AccessTokenUrl"))+'token'
    requestData = OAuthRequest(os.environ.get("grant_type"), os.environ.get(
        "scope"), os.environ.get("ClientId"), os.environ.get("clientSecret")).toJSON()
    header = {'Content-type': 'application/json'}
    response = requests.post(url, headers=header, data=requestData)
    result = OAuthResult.create_from_json(response.text)
    cache["access_token"] = result.access_token
    return result


def GetRequester(url: str, method: str, data=None):
    token = cache.get("access_token")
    if token is None:
        token = GetAccesstoken().access_token
    header = {'Content-type': 'application/json',
              'Authorization': 'Bearer '+token}
    if method == 'GET':
        result = requests.get(url=url, headers=header)
        validateResult(result)
        return result
    if method == 'POST':
        result = requests.post(url=url, headers=header, data=data)
        validateResult(result)
        return result
    if method == 'PUT':
        return
    if method == 'DELETE':
        return


def validateResult(result: requests.Response):
    result.raise_for_status()
    text = result.text
    error = re.search('error', text)
    code = re.search('code', text)
    if error is not None or code is not None:
        raise ValueError(text)

 # UserInfo


def GetUserInfo():
    url = (os.environ.get("AccessTokenUrl"))+'userinfo'
    userinfo = GetRequester(url=url, method='GET')
    return UserInfo.create_from_json(userinfo.text)


# Market
def MarketList():
    url = (os.environ.get("ApiUrl"))+'market/list'
    return MarketListResponse.create_from_json(GetRequester(url=url, method='GET').text)


def MarketSummaries():
    url = (os.environ.get("ApiUrl"))+'market/summaries'
    return MarketSummrieResponse.create_from_json(GetRequester(url=url, method='GET').text)


def PostMarketTicks(MarketTicks):
    url = (os.environ.get("ApiUrl"))+'market/ticks'
    return MarketTicksResponse.create_from_json(GetRequester(
        url=url, method='POST', data=MarketTicks.toJSON()).text)


def PostMarketOrderBook(MarketOrderBook):
    url = (os.environ.get("ApiUrl"))+'market/orderbook'
    return MarketOrderBookResponse.create_from_json(GetRequester(
        url=url, method='POST', data=MarketOrderBook.toJSON()).text)


def PostMarketHistory(MarketHistory):
    url = (os.environ.get("ApiUrl"))+'market/history'
    return MarketHistoryResponse.create_from_json(GetRequester(
        url=url, method='POST', data=MarketHistory.toJSON()).text)


# wallet

def WalletBalance(Simulation: Simulation):
    url = (os.environ.get("ApiUrl"))+'wallet/balances'
    return WalletBalanceResponse.create_from_json(GetRequester(
        url=url, method='POST', data=Simulation.toJSON()).text)


def PostWalletTransaction(walletTransaction: WalletTransaction):
    url = (os.environ.get("ApiUrl"))+'wallet/transactions'
    return WalletTransactionResponse.create_from_json(GetRequester(
        url=url, method='POST', data=walletTransaction.toJSON()).text)


def PostWalletFunds(walletFunds: WalletFunds):
    url = (os.environ.get("ApiUrl"))+'wallet/send'
    WalletFundsResponse = GetRequester(
        url=url, method='POST', data=walletFunds.toJSON())
    print(WalletFundsResponse.text)


# Order
def PostOrderList(orderListRequest: OrderListRequest):
    url = (os.environ.get("ApiUrl"))+'order/list'
    return OrderListResponse.create_from_json(GetRequester(
        url=url, method='POST', data=orderListRequest.toJSON()).text)


def PostOrderInfo(orderInfo: OrderInfo):
    url = (os.environ.get("ApiUrl"))+'order/info'
    return OrderInfoResponse.create_from_json(GetRequester(
        url=url, method='POST', data=orderInfo.toJSON()).text)


def PostOrderPending(simulation: Simulation):
    url = (os.environ.get("ApiUrl"))+'order/pending'
    return OrderPendingResponse.create_from_json(GetRequester(
        url=url, method='POST', data=simulation.toJSON()).text)


def PostOrderCreate(createOrder: CreateOrder):
    url = (os.environ.get("ApiUrl"))+'order/create'
    return CreateOrderResponse.create_from_json(GetRequester(
        url=url, method='POST', data=createOrder.toJSON()).text)


def PostOrderCancel(orderCancel: OrderCancel):
    url = (os.environ.get("ApiUrl"))+'order/cancel'
    return OrderCancelResponse.create_from_json(GetRequester(
        url=url, method='POST', data=orderCancel.toJSON()).text)


# portfolio


def PostPortfolioSummary(simulation: Simulation):
    url = (os.environ.get("ApiUrl"))+'portfolio/list'
    return PortfolioListResponse.create_from_json(GetRequester(
        url=url, method='POST', data=simulation.toJSON()).text)


def PostPortfolioOpenOrder(simulation:Simulation):
    url = (os.environ.get("ApiUrl"))+'portfolio/open-orders'
    return PortfolioOpenOrderResponse.create_from_json(GetRequester(
        url=url, method='POST', data=simulation.toJSON()).text)


def PostPortfolioHistory(simulation:Simulation):
    url = (os.environ.get("ApiUrl"))+'portfolio/history'
    return PortfolioHistoryResponse.create_from_json(GetRequester(
        url=url, method='POST', data=simulation.toJSON()).text)


def PostPortfolioCreateOrder(portfolioCreateOrder:PortfolioCreateOrder):
    url = (os.environ.get("ApiUrl"))+'portfolio/create-order'
    return CreatePortfolioResponse.create_from_json(GetRequester(
        url=url, method='POST', data=portfolioCreateOrder.toJSON()).text)


def PostPortfolioCancelOrder(cancelPorfolioOrder:CancelPorfolioOrder):
    url = (os.environ.get("ApiUrl"))+'portfolio/cancel-order'
    return CancelPortfolioResponse.create_from_json(GetRequester(
        url=url, method='POST', data=cancelPorfolioOrder.toJSON()).text)


def PostPortfolioCloseOrder(closePortfolioPosition:ClosePortfolioPosition):
    url = (os.environ.get("ApiUrl"))+'portfolio/close'
    PortfolioCloseOrderResponse = GetRequester(
        url=url, method='POST', data=closePortfolioPosition.toJSON())
    print(PortfolioCloseOrderResponse.text)


obj = GetAccesstoken()
# print(obj.access_token)
# GetUserInfo()
# print(result.name)
# MarketList()
# MarketSummaries()
#PostMarketTicks(MarketTicks("USDT-BTC", 60))
#PostMarketOrderBook(MarketOrderBook("USDT-BTC", 50, False))
#history=PostMarketHistory(MarketHistory("USDT-BTC", 50, "string", "string"))
#for his in history:
#    print(his.toJSON())
# WalletBalance(Simulation(True))
#PostWalletTransaction(WalletTransaction("BTC", True))
#PostWalletFunds(WalletFunds("BTC", 1.05, "1CK6KHY6MHgYvmRQ4PAafKYDrg1eaaaaaa"))
#PostOrderList(OrderListRequest(0, 10, "USDT-BTC", True))
#PostOrderInfo(OrderInfo("db78faa89f08062bfebeacb51365fadb08b63da6", True))
# PostOrderPending(Simulation(True))
result=PostOrderCreate(CreateOrder("USDT-BTC", "buy", 10, "BTC", 1.5, True))
print(result.toJSON())
#PostOrderCancel(OrderCancel("db78faa89f08062bfebeacb51365fadb08b63da6", False))
#PostPortfolioSummary(Simulation(True))
#PostPortfolioOpenOrder(Simulation(True))
#PostPortfolioHistory(Simulation(True))
#PostPortfolioCreateOrder(PortfolioCreateOrder("USDT-BTC", 0.55, 3555.36, True))
#PostPortfolioCancelOrder(CancelPorfolioOrder(1, False))
#PostPortfolioCloseOrder(ClosePortfolioPosition(1, True))
