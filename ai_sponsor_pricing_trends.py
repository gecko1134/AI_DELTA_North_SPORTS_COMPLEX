
def get_trend_adjusted_prices(base_prices, trend_factors):
    prices = {}
    for zone, base in base_prices.items():
        factor = trend_factors.get(zone, 1.0)
        prices[zone] = round(base * factor, 2)
    return prices
