import bitso
from secrets import bitso_api_key, bitso_api_secret
api = bitso.Api(bitso_api_key, bitso_api_secret)

def get_balance_mxn():
    balances = api.balances()
    mxn_available = float(balances.mxn.available)
    return mxn_available


def get_risk_level():
    risk_level = input("What level of risk are you comfortable with? high, medium, or low")
    if risk_level.lower() == "high" or "medium" or "low" or " high" or " medium" or " low":
        return risk_level
    else:
        get_risk_level()

def place_order(mxn_available, risk_level):
    if risk_level == "high":
        btc_to_buy = str(mxn_available)
        order = api.place_order(book='btc_mxn', side='buy', order_type='market', minor=btc_to_buy)

    elif risk_level == "medium":
        btc_to_buy = str(round(mxn_available * 0.50))
        tusd_tobuy = str(round(mxn_available * 0.50))
        order = api.place_order(book='btc_mxn', side='buy', order_type='market', minor=btc_to_buy)
        order = api.place_order(book='tusd_mxn', side='buy', order_type='market', minor=tusd_tobuy)

    elif risk_level == "low":
        tusd_tobuy = str(mxn_available)
        order = api.place_order(book='tusd_mxn', side='buy', order_type='market', minor=tusd_tobuy)


def main():
    mxn_available = get_balance_mxn()
    risk_level = get_risk_level()
    place_order(mxn_available, risk_level)

main()
