

def price_updater(prices, increase_rate):
    updated_prices = []
    increase_rate = 1 + increase_rate

    for price in prices:
        updated_prices.append(increase_rate*price)

    return updated_prices