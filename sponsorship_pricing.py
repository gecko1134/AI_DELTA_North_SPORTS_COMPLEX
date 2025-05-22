
def suggest_pricing(zones, demand_scores):
    pricing = {}
    for zone in zones:
        demand = demand_scores.get(zone, 1)
        base_price = 1000
        pricing[zone] = base_price * demand
    return pricing
